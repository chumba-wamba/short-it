from short_it import db
from short_it.models import URL, User
from datetime import datetime


test_URL = URL(
    shortened="test1",
    URL="www.test_url.com",
)
test_URL.save()

test_user_one = User(
    user_name="nisarg42",
    email="test0@test.com",
    first_name="Nisarg0",
    last_name="Shah0",
)
test_user_one.save()

test_user_two = User(
    user_name="nisarg123",
    email="test1@test.com",
    first_name="Nisarg1",
    last_name="Shah1",
)
test_user_two.save()

for document in URL.objects:
    # print(document.to_json()) # to_json() converts the docuemnt object to a readable json format
    print(document.shortened)
    print(document.URL)
    print(document.date_defined)
    print(document.counter)
    date_array = document.date_array
    print(type(date_array), end="\n\n")

for document in User.objects:
    # print(document.to_json()) # to_json() converts the docuemnt object to a readable json format
    print(document.id)
    print(document.first_name)
    print(document.last_name)
    print(type(date_array), end="\n\n")
