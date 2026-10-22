from faker import Faker
def generate_fake_names(count=50000):
    fake = Faker()
    return [fake.name() for _ in range(count)]
names_list = generate_fake_names()
print(names_list[:50000])
