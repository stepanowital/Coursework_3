import pytest

from utils import get_posts_all


def test_get_posts_all():
	assert type(get_posts_all()) == list


# def test_get_posts_by_user(user_name):
# 	assert type
