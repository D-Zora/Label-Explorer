# Label Explorer 测试版
# 创建人：曾逸夫
# 创建时间：2024-02-11
# python label_explorer_test.py


import subprocess

import pytest

TASK_ARGS = [
    (0.8),
    (0.7),
    (0.75),
    (0.9),
]  # (prob)


def run(cmd):
    """Execute a shell command using subprocess."""
    subprocess.run(cmd.split(), check=True)


def test_label_explorer():
    run(f"label-explorer")


@pytest.mark.parametrize("prob", TASK_ARGS)
def test_le_p(prob):
    run(f"label-explorer -p {prob}")


if __name__ == "__main__":
    pytest.main(["-s", "-v", "le_test.py::test_label_explorer"])  # 一般测试
    # pytest.main(["-s", "-v", "le_test.py::test_le_p"])  # 测试不同比例
