from faker import Faker

faker = Faker()

def get_user_data():
    return {
        "name": faker.first_name(),
        "email": faker.unique.email(),
        "password": "Test@1234",
        "address": faker.address(),
        "city": faker.city(),
        "state": faker.state(),
        "zipcode": faker.postcode(),
        "phone": faker.phone_number()
    }
