import pytest

from online_status import onlineStatus

people_list = [
    ({'Alice': 'online', 'Bob': 'offline'}, 1),
    ({'Alice': 'online', 'Bob': 'offline', 'Eve': 'online'}, 2),
    ({'Alice': 'online', 'Bob': 'offline', 'Jack': 'offline'}, 1),
    ({'Alice': 'online', 'Bob': 'offline', 'Jack': 'offline', 'Eve': 'online'}, 2)
]

addition_names = (f"From {persons} - {online} is online." for persons,online in people_list)

@pytest.mark.parametrize("persons, online", people_list, ids=addition_names)
def test_online_status(persons, online):

    result = onlineStatus(persons)

    assert result == online