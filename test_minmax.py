def test_minmax():
    from ListOperations_OOP import ListOperations
    import pytest
    import numpy

    list1 = ListOperations([0, -1.5, -2, -7, -53])
    list2 = ListOperations([0, 3.2, 2, 10, 6])
    list3 = ListOperations([2, -3, 54, 6, 10])

    list1.findextremes()
    list2.findextremes()
    list3.findextremes()

    assert list1.extremes == [-53.0, 0.0]
    assert list2.extremes == [0, 10]
    assert list3.extremes == [-3.0, 54.0]

    #def test_imaginary_input():
    #    with pytest.raises(ValueError):
    #        findextremes([3+2j, 4])

    #def test_empty_input():
    #    with pytest.raises(TypeError):
    #        findextremes([])

    #def test_non_list_in():
    #    with pytest.raises(TypeError):
    #        findextremes('Hello World')
