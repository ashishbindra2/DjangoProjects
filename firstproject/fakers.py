from  faker import Faker
fak = Faker()
def make_dummy(n):
    for i in range(n):
        print(fak.name(),fak.date(),fak.company(),fak.address(),fak.email())

make_dummy(25)
