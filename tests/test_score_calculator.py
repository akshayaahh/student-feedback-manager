from score_calculator import calculate_average

def test_calculate_average():
    data = [{"name": "A", "score": 8}, {"name": "B", "score": 6}]
    assert calculate_average(data) == 7.0
    assert calculate_average([]) == 0.0
