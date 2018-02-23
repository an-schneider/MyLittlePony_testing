def test_ListOperations_OOP():
    from ListOperations_OOP import ListOperations
    import pytest
    import numpy
    import math

    # Test MinMax
    list1 = ListOperations([0, -1.5, -2, -7, -53])
    list2 = ListOperations([0, 3.2, 2, 10, 6])
    list3 = ListOperations([2, -3, 54, 6, 10])
    list4 = ListOperations([3 + 2j, 4])
    list5 = ListOperations([])
    list6 = ListOperations('Hello World!')

    list1.main()
    list2.main()
    list3.main()

    assert list1.extremes == [-53.0, 0.0]
    assert list2.extremes == [0, 10]
    assert list3.extremes == [-3.0, 54.0]

    with pytest.raises(ValueError):
        list4.main()
    with pytest.raises(TypeError):
        list5.main()
    with pytest.raises(TypeError):
        list6.main()

    # Test sum_num
    list1 = ListOperations([1, 5, 8, 3, 6, 3])
    list2 = ListOperations([-4, 5, 7, 5, 3, -5])
    list3 = ListOperations([0.5, -0.3, 0.2, -0.5])
    list4 = ListOperations([3+2j, math.sqrt(4), math.sqrt(2)])
    list5 = ListOperations(["1", 2, 3])

    list1.main()
    list2.main()
    list3.main()

    assert list1.sum_num == 26
    assert list2.sum_num == 11
    assert list3.sum_num - 0.1 < 0.0001

    with pytest.raises(ValueError):
        list4.main()
    with pytest.raises(TypeError):
        list5.main()
    with pytest.raises(ImportError):
        import MyLittlePony

    # Test max_diff
    list1 = ListOperations([-5, 2, 6, 1, -7, 10])
    list2 = ListOperations([9, 8, -7, 6, 5, -4])
    list3 = ListOperations([0.5, -0.9, 0.1, -0.2])
    list4 = ListOperations([math.sqrt(2), 5+3j, math.sqrt(8)])
    list5 = ListOperations(['9', 5, 9, 5, 9, 5])

    list1.main()
    list2.main()
    list3.main()

    assert list1.max_difference == 17
    assert list2.max_difference == 15
    assert list3.max_difference - 1.4 < 0.0001

    with pytest.raises(ValueError):
        list4.main()
    with pytest.raises(TypeError):
        list5.main()
    with pytest.raises(ImportError):
        import MyLittlePony_testing
