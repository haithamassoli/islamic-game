#!/usr/bin/env python3
"""Planning tool. Task files (tasks/Mxx/TASK-*.md) are the source of truth for task data.

  python3 tools/plan.py check   validate fields, IDs, deps, cycles, statuses, relative links, AUTO markers
  python3 tools/plan.py sync    promote Todo<->Ready, regenerate planning/TASKS.csv, planning/TASK_INDEX.md,
                                AUTO blocks in milestones/*.md and PROJECT_STATUS.md, then check
"""
import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIELDS = ["Task ID", "Title", "Milestone", "Epic", "Priority", "Status", "Type",
          "Complexity", "Level", "Dependencies", "Religious Review"]
SECTIONS = ["Objective", "Description", "Implementation Plan", "Expected Files", "Acceptance Criteria",
            "Testing", "Definition of Done", "Potential Issues", "Related Tasks", "Notes", "Religious Review"]
PRIORITIES = ["Critical", "High", "Medium", "Low"]
STATUSES = ["Todo", "Ready", "In Progress", "Blocked", "In Review", "Done"]
ALLOWED = {
    "Priority": set(PRIORITIES),
    "Status": set(STATUSES),
    "Type": {"Programming", "Art", "Design", "Audio", "Writing", "Religious Review", "QA", "DevOps"},
    "Complexity": {"S", "M", "L", "XL"},
    "Level": {"Foundation", "Prototype", "VerticalSlice", "MVP", "PostMVP"},
    "Religious Review": {"Yes", "No"},
}
WEIGHT = {"S": 1, "M": 2, "L": 4, "XL": 8}  # ponytail: effort proxy, replace with estimates if the team tracks them
ROW = re.compile(r"^\|\s*\*\*(.+?)\*\*\s*\|\s*(.*?)\s*\|\s*$")
TASK_ID = re.compile(r"TASK-M\d{2}-\d{3}")
LINK = re.compile(r"\]\(([^)\s]+)\)")
SKIP_DIRS = {".git", "Library", "Temp", "Obj", "Logs", "node_modules", ".codex"}


def load():
    tasks, errors = {}, []
    for f in sorted(ROOT.glob("tasks/M*/TASK-*.md")):
        text = f.read_text(encoding="utf-8")
        head = {}
        for line in text.splitlines()[:25]:
            m = ROW.match(line)
            if m:
                head.setdefault(m[1], m[2])
        missing = [k for k in FIELDS if k not in head]
        if missing:
            errors.append(f"{rel(f)}: missing header fields {missing}")
            continue
        t = dict(head)
        tid = t["Task ID"]
        t["path"] = f
        t["milestone"] = tid[5:8]
        t["deps"] = list(dict.fromkeys(TASK_ID.findall(t["Dependencies"])))  # link text + URL repeat each ID
        if f.stem != tid:
            errors.append(f"{rel(f)}: file name != Task ID {tid}")
        if f.parent.name != t["milestone"] or f"milestones/{t['milestone']}.md" not in t["Milestone"]:
            errors.append(f"{rel(f)}: milestone folder/link mismatch")
        for k, allowed in ALLOWED.items():
            if t[k] not in allowed:
                errors.append(f"{rel(f)}: {k}='{t[k]}' not in {sorted(allowed)}")
        for s in SECTIONS:
            if not re.search(rf"^## {re.escape(s)}\s*$", text, re.M):
                errors.append(f"{rel(f)}: missing section '## {s}'")
        if tid in tasks:
            errors.append(f"{rel(f)}: duplicate Task ID {tid}")
        tasks[tid] = t
    return tasks, errors


def rel(p):
    return str(Path(p).relative_to(ROOT))


def check_graph(tasks):
    errors, warnings = [], []
    for tid, t in tasks.items():
        for d in t["deps"]:
            if d not in tasks:
                errors.append(f"{tid}: dependency {d} does not exist")
            elif d == tid:
                errors.append(f"{tid}: depends on itself")
        done = all(tasks[d]["Status"] == "Done" for d in t["deps"] if d in tasks)
        if t["Status"] in ("Ready", "In Progress", "In Review", "Done") and not done:
            errors.append(f"{tid}: status {t['Status']} but not all dependencies are Done")
        if t["Status"] == "Todo" and done:
            warnings.append(f"{tid}: all dependencies Done, should be Ready (run sync)")
    state = {}  # 1 = on current path, 2 = finished

    def visit(node, path):
        state[node] = 1
        for d in tasks[node]["deps"]:
            if d not in tasks:
                continue
            if state.get(d) == 1:
                errors.append("dependency cycle: " + " -> ".join(path[path.index(d):] + [d]))
            elif d not in state:
                visit(d, path + [d])
        state[node] = 2

    for tid in tasks:
        if tid not in state:
            visit(tid, [tid])
    return errors, warnings


def strip_code(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def check_links():
    errors = []
    for f in ROOT.rglob("*.md"):
        if SKIP_DIRS & set(f.relative_to(ROOT).parts):
            continue
        for target in LINK.findall(strip_code(f.read_text(encoding="utf-8"))):
            if re.match(r"^(https?:|mailto:|#|t3-thread:)", target):
                continue
            path = target.split("#")[0]
            if path and not (f.parent / path).resolve().exists():
                errors.append(f"{rel(f)}: broken link -> {target}")
    return errors


def check_markers():
    errors = []
    for f in sorted(ROOT.glob("milestones/M*.md")):
        text = f.read_text(encoding="utf-8")
        for name in ("EXTDEPS", "TASKS", "PROGRESS"):
            if text.count(f"<!-- AUTO:{name}:START -->") != 1 or text.count(f"<!-- AUTO:{name}:END -->") != 1:
                errors.append(f"{rel(f)}: AUTO:{name} markers missing or duplicated")
    status = ROOT / "PROJECT_STATUS.md"
    if status.exists() and "<!-- AUTO:PROGRESS:START -->" not in status.read_text(encoding="utf-8"):
        errors.append("PROJECT_STATUS.md: AUTO:PROGRESS markers missing")
    return errors


def set_status(t, new):
    text = t["path"].read_text(encoding="utf-8")
    text = re.sub(r"^(\|\s*\*\*Status\*\*\s*\|\s*)" + re.escape(t["Status"]) + r"(\s*\|)",
                  lambda m: m[1] + new + m[2], text, count=1, flags=re.M)
    t["path"].write_text(text, encoding="utf-8")
    t["Status"] = new


def promote(tasks):
    changed = True
    while changed:
        changed = False
        for t in tasks.values():
            done = all(tasks[d]["Status"] == "Done" for d in t["deps"] if d in tasks)
            if t["Status"] == "Todo" and done:
                set_status(t, "Ready"); changed = True
            elif t["Status"] == "Ready" and not done:
                set_status(t, "Todo"); changed = True


def sort_key(t):
    return (t["milestone"], PRIORITIES.index(t["Priority"]), t["Task ID"])


def link(t, base):
    return f"[{t['Task ID']}]({base}{t['milestone']}/{t['Task ID']}.md)"


def pct(part, whole):
    return f"{(100 * part / whole):.1f}%" if whole else "0%"


def progress(ts):
    done = [t for t in ts if t["Status"] == "Done"]
    w_all = sum(WEIGHT[t["Complexity"]] for t in ts)
    w_done = sum(WEIGHT[t["Complexity"]] for t in done)
    return len(done), len(ts), pct(len(done), len(ts)), pct(w_done, w_all)


def task_table(ts, base):
    out = ["| ID | العنوان | الحالة | الأولوية | النوع | الحجم | الاعتمادات | مراجعة شرعية |", "|---|---|---|---|---|---|---|---|"]
    for t in ts:
        deps = ", ".join(t["deps"]) or "—"
        out.append(f"| {link(t, base)} | {t['Title']} | {t['Status']} | {t['Priority']} | {t['Type']} | "
                   f"{t['Complexity']} | {deps} | {t['Religious Review']} |")
    return "\n".join(out)


def replace_block(path, name, body):
    text = path.read_text(encoding="utf-8")
    start, end = f"<!-- AUTO:{name}:START -->", f"<!-- AUTO:{name}:END -->"
    if start not in text:
        return
    new = re.sub(re.escape(start) + r".*?" + re.escape(end),
                 lambda _: f"{start}\n{body}\n{end}", text, count=1, flags=re.S)
    path.write_text(new, encoding="utf-8")


def write_outputs(tasks):
    ordered = sorted(tasks.values(), key=lambda t: t["Task ID"])
    by_ms = defaultdict(list)
    for t in ordered:
        by_ms[t["milestone"]].append(t)

    with open(ROOT / "planning/TASKS.csv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["id", "title", "milestone", "epic", "priority", "status", "type", "complexity",
                    "level", "religious_review", "dependencies", "path"])
        for t in ordered:
            w.writerow([t["Task ID"], t["Title"], t["milestone"], t["Epic"], t["Priority"], t["Status"], t["Type"],
                        t["Complexity"], t["Level"], t["Religious Review"], ";".join(t["deps"]), rel(t["path"])])

    counts = Counter(t["Status"] for t in ordered)
    d, n, p_count, p_effort = progress(ordered)
    ready = sorted((t for t in ordered if t["Status"] == "Ready"), key=sort_key)
    idx = ["# فهرس المهام", "",
           "> مولَّد آلياً بواسطة `python3 tools/plan.py sync` من ملفات `tasks/`. لا تعدّله يدوياً.", "",
           f"**الإجمالي:** {n} مهمة. **المكتمل:** {d} ({p_count} بالعدد، {p_effort} بالجهد).", "",
           "| الحالة | العدد |", "|---|---|"] + [f"| {s} | {counts.get(s, 0)} |" for s in STATUSES]
    idx += ["", "## جاهزة للبدء الآن", ""] + ([task_table(ready, "../tasks/")] if ready else ["لا شيء."])
    for ms, ts in sorted(by_ms.items()):
        md, mn, mp, me = progress(ts)
        idx += ["", f"## [{ms}](../milestones/{ms}.md) — {md}/{mn} ({mp} بالعدد، {me} بالجهد)", "",
                task_table(ts, "../tasks/")]
    (ROOT / "planning/TASK_INDEX.md").write_text("\n".join(idx) + "\n", encoding="utf-8")

    for ms, ts in by_ms.items():
        f = ROOT / f"milestones/{ms}.md"
        if not f.exists():
            continue
        replace_block(f, "TASKS", task_table(ts, "../tasks/"))
        ext = sorted({d for t in ts for d in t["deps"] if d in tasks and tasks[d]["milestone"] != ms})
        replace_block(f, "EXTDEPS", "**مهام من مراحل أخرى تحجب هذه المرحلة:**\n\n" + (
            "\n".join(f"- {link(tasks[d], '../tasks/')} — {tasks[d]['Title']} ({tasks[d]['Status']})" for d in ext)
            or "لا شيء."))
        md, mn, mp, me = progress(ts)
        c = Counter(t["Status"] for t in ts)
        replace_block(f, "PROGRESS", f"المهام المكتملة: **{md}/{mn}** ({mp} بالعدد، {me} بالجهد). "
                      + "، ".join(f"{s}: {c[s]}" for s in STATUSES if c[s]))

    status = ROOT / "PROJECT_STATUS.md"
    if status.exists():
        current = next((ms for ms, ts in sorted(by_ms.items()) if any(t["Status"] != "Done" for t in ts)), "—")
        body = [f"_آخر مزامنة بواسطة `tools/plan.py sync`._", "",
                f"**المرحلة الحالية (أقدم مرحلة غير مكتملة المهام):** [{current}](milestones/{current}.md)", "",
                f"**التقدم الإجمالي:** {d}/{n} مهمة ({p_count} بالعدد، {p_effort} بالجهد)", "",
                "| الحالة | العدد |", "|---|---|"] + [f"| {s} | {counts.get(s, 0)} |" for s in STATUSES]
        body += ["", "| المرحلة | المكتمل | بالعدد | بالجهد |", "|---|---|---|---|"]
        for ms, ts in sorted(by_ms.items()):
            md, mn, mp, me = progress(ts)
            body.append(f"| [{ms}](milestones/{ms}.md) | {md}/{mn} | {mp} | {me} |")
        for label, st in [("قيد التنفيذ", "In Progress"), ("قيد المراجعة", "In Review"),
                          ("متوقفة", "Blocked"), ("جاهزة للبدء", "Ready"), ("مكتملة", "Done")]:
            ts = sorted((t for t in ordered if t["Status"] == st), key=sort_key)
            body += ["", f"### {label} ({len(ts)})", ""]
            body += [f"- {link(t, 'tasks/')} — {t['Title']} ({t['Priority']})" for t in ts] or ["لا شيء."]
        replace_block(status, "PROGRESS", "\n".join(body))


def main(cmd):
    tasks, errors = load()
    if cmd == "sync" and not errors:
        promote(tasks)
        write_outputs(tasks)
    g_err, warnings = check_graph(tasks)
    errors += g_err + check_links() + check_markers()
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    c = Counter(t["Status"] for t in tasks.values())
    print(f"{len(tasks)} tasks | " + " | ".join(f"{s}: {c.get(s, 0)}" for s in STATUSES)
          + f" | {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ("check", "sync"):
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
