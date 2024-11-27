import pytest
@pytest.fixture()
def first_entry():
   return "a"

# Arrange
@pytest.fixture
def order(first_entry,append_first):
    return first_entry+append_first

@pytest.fixture
def append_first():
  return 'c'

def test_string_only(order,first_entry,append_first):
    # Assert
    print(append_first)
    #assert order == [first_entry]
    print(order)
    print(first_entry)
    #pass