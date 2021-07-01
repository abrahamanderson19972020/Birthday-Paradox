import datetime
import random


def get_birthdays(number_of_birthdays):
    birthdays = []
    for i in range(number_of_birthdays):
        # The year is unimportant for our simulation, as long as all birthdays have the same year.
        start_date = datetime.date(1983, 1, 1)
        # Get a random day into the year:
        random_number_of_days = datetime.timedelta(random.randint(0, 364))
        birthday = start_date + random_number_of_days
        birthdays.append(birthday)

    return birthdays


def determine_probability(number_of_people, run_amount=1_000):
    dups_found = 0
    for _ in range(run_amount):
        birthdays = get_birthdays(number_of_people)
        duplicates = set(x for x in birthdays if birthdays.count(x) > 1)
        if len(duplicates) >= 1:
            dups_found += 1

    return dups_found/run_amount * 100


def repeat(birthday):
    repeated = []
    for i in range(len(birthday)):
        k = i + 1
        for j in range(k, len(birthday)):
            if birthday[i] == birthday[j] and birthday[i] not in repeated:
                repeated.append(birthday[i])
    return repeated


def main():
    while True:
        print("How many birthdays do you want to match?")
        response = input(">>>")
        if response.isdecimal():
            number_of_birthdays = int(response)
            break
    birthdays = get_birthdays(number_of_birthdays)
    dublicate_birtdays = repeat(birthdays)
    if len(dublicate_birtdays) > 0:
        print(
            f"There are {len(dublicate_birtdays)} duplicate birthdays. "
            f"This is the list of birthdays : {dublicate_birtdays}")
    else:
        print("There are no matching birthdays")

    probability = determine_probability(number_of_birthdays)

    print(f'Out of {number_of_birthdays} simulations, there was a')

    print('matching birthday in that group', len(dublicate_birtdays), 'times. This means')

    print('that', 'people have a', probability, '% chance of')

    print('having a matching birthday in their group.')

    print('That\'s probably more than you would think!')


if __name__ == '__main__':
    main()
