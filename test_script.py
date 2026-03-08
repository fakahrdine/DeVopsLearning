from unittest.mock import Mock, patch

from script import (
    add_numbers,
    subtract_numbers,
    pocket_message,
    website_is_working,
    count_invalid_lines,
)


def test_add_numbers():
    assert add_numbers(200, 400) == 600


def test_subtract_numbers():
    assert subtract_numbers(200, 400) == -200


def test_pocket_message():
    assert pocket_message(200) == "there is 200 in my pocket"


@patch("script.requests.get")
def test_website_is_working_true(mock_get):
    mock_get.return_value = Mock(status_code=200)
    assert website_is_working() is True


@patch("script.requests.get")
def test_website_is_working_false(mock_get):
    mock_get.return_value = Mock(status_code=500)
    assert website_is_working() is False


def test_count_invalid_lines(tmp_path):
    file_path = tmp_path / "notes.txt"
    file_path.write_text("ok\nnot valid\nnot valid\n", encoding="utf-8")
    assert count_invalid_lines(str(file_path)) == 2