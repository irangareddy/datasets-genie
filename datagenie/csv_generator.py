"""CSV Generator"""

import faker

fake = faker.Faker()


def get_fake_name():
    """returns fake name"""
    return fake.name()


print(get_fake_name())
