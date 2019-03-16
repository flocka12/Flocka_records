'''Module containing sample data for testing'''
USER_REGISTRATION = dict(
    firstname="test_first",
    lastname="test_last",
    email="tester@example.com",
    username="tester_user",
    password="12345abcsde"
)

NEW_USER_REGISTRATION = dict(
    firstname="test_first",
    lastname="test_last",
    email="tester@example.com",
    username="tester_user",
    password="12345abcsde"
)

USER_DUPLICATE_USERNAME = dict(
    firstname="test_first",
    lastname="test_last",
    email="tester@example.com",
    username="tester_user",
    password="12345abcsde"
)

USER_DUPLICATE_EMAIL = dict(
    firstname="test_first",
    lastname="test_last",
    email="tester@example.com",
    username="tester_user",
    password="12345abcsde"
)

USER_DIGIT_USERNAME = dict(
    firstname="test_first",
    lastname="test_last",
    email="tester@example.com",
    username="1234",
    password="12345abcsde"
)

USER_EMPTY_USERNAME = dict(
    firstname="test_first",
    lastname="test_last",
    email="tester@example.com",
    username="",
    password="12345abcsde"
)

USER_EMPTY_PASSWORD = dict(
    firstname="test_first",
    lastname="test_last",
    email="tester@example.com",
    username="tester_user",
    password=""
)

USER_LOGIN = dict(username="tester_user", password="12345abcsde")

NEW_USER_LOGIN = dict(username="tester_user_new", password="abcdqwqs11234")

USER_LOGIN_INCORRECT_PASSWORD = dict(username="tester_user", password="abcde122edasda")
