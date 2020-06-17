from short_it import db
from short_it.models import URL, User
from datetime import datetime


test_URL = URL(
    shortened="test1",
    URL="www.test_url.com",
)
test_URL.save()

test_User = User(
    user_name="nisarg123",
    first_name="Nisarg",
    last_name="Shah",
)
test_User.save()

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
