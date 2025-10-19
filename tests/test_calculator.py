# tests/test_calculator.py
import pytest
from calculator import add


# 正常情况测试用例
def test_add_normal():
    assert add(1, 2) == 3
    assert add(0, 0) == 0
    assert add(-1, 1) == 0


# 边界情况测试用例
def test_add_boundary():
    # 大数相加
    assert add(1000000, 2000000) == 3000000
    # 小数相加
    assert add(0.1, 0.2) == pytest.approx(0.3)  # 浮点数比较用approx


# 异常情况测试用例
def test_add_exception():
    with pytest.raises(TypeError):
        add(1, "2")  # 整数和字符串相加，预期抛出TypeError
