"""Run: python3 tools/test_plan.py"""
from plan import check_graph

def t(tid, deps, status="Todo"):
    return tid, {"deps": deps, "Status": status}

tasks = dict([t("A", []), t("B", ["A"]), t("C", ["B", "X"])])
err, _ = check_graph(tasks)
assert any("X does not exist" in e for e in err), err

tasks = dict([t("A", ["C"]), t("B", ["A"]), t("C", ["B"])])
err, _ = check_graph(tasks)
assert any("cycle" in e for e in err), err

tasks = dict([t("A", [], "Done"), t("B", ["A"], "Ready"), t("C", ["B"], "Ready")])
err, warn = check_graph(tasks)
assert err == ["C: status Ready but not all dependencies are Done"], err

tasks = dict([t("A", [], "Done"), t("B", ["A"], "Todo")])
_, warn = check_graph(tasks)
assert warn and "should be Ready" in warn[0], warn
print("ok")
