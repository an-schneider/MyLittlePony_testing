def test_sum_numbers():
    from ListOperations_OOP import ListOperations
    import pytest
    import math

    list1 = ListOperations([1, 5, 8, 3, 6, 3])
    list2 = ListOperations([-4, 5, 7, 5, 3, -5])
    list3 = ListOperations([0.5, -0.3, 0.2, -0.5])

    list1.sum_numbers()
    list2.sum_numbers()
    list3.sum_numbers()
    assert list1.sum_num == 26
    assert list2.sum_num == 11
    assert list3.sum_num - 0.1 < 0.0001

    with pytest.raises(ValueError):
        list4 = ListOperations([math.sqrt(-2),math.sqrt(4),math.sqrt(2)])
        list4.sum_numbers()
    with pytest.raises(TypeError):
        list5 = ListOperations(["1", 2, 3])
        list5.sum_numbers()
    with pytest.raises(ImportError):
        import MyLittlePony
