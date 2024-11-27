import pytest
class TimeLine:
    def __init__(self, instances):
        self.instance = instances
@pytest.fixture
def list():
    print("hiii")
    return [0, 0, 0]
@pytest.fixture
def timeline(list):
    return TimeLine(list)

@pytest.mark.parametrize('list', [[2, 4, 6], [6, 8, 10]])
def test_timeline(timeline):
    print(timeline.instance)
    for l in timeline.instance:
         assert l % 2 == 0
@pytest.fixture
def multiply_fixture(request):
    return request.param
    #print("hiiiiiiii")

    #yield factor
    #print("byeee")

@pytest.mark.parametrize("multiply_fixture", [2, 3, 4], indirect=True)
def test_multiplication(multiply_fixture):
    print(multiply_fixture)
    result = multiply_fixture * 5
    print(result)
    #assert result % multiply_fixture == 0

