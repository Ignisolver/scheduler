import random
from pandas import DataFrame

"""
Dane oparte mniej więcej na podstawie wydziału EAIiIB AGH, policzone na "oko"
"""

ROOM_FILE_NAME = "sale_test414.csv"
ROOM_NUMBER = 68  # 68
ROOM_NUMBER_WITH_MAX_AVAILABILITY = 40  # 40
MIN_AVAILABILITY = 2500
MAX_AVAILABILITY = 3000  # 3000

LECTURER_FILE_NAME = "prowadzacy_test414.csv"
LECTURER_NUMBER = 66  # 66

GROUPS_FILE_NAME = "grupy_test414.csv"
GROUP_NUMBER = 92  # 92
MIN_GROUP_SIZE = 20
MAX_GROUP_SIZE = 30

CLASSES_FILE_NAME = "zajecia_test414.csv"
FIELD1_NUMBER = 7  # 7
FIELD2_NUMBER = 15  # 15

MIN_NUM_GROUPS = 4  # 4
MAX_NUM_GROUPS = 19  # 19
AVER_NUM_GROUPS = 11
MAX_GROUPS_IN_YEAR = 6  # 6

SEM1_NUMBER = 4  # 4
SEM2_NUMBER = 1  # 1

MEAN_SUBJECT_NUM = 10  # 7

EXERCISES_IN_SUBJECT = [1, 2, 3]  # [1, 2]
EIS_DISTR = [0.4, 0.8, 1]  # [0.7, 1]
SUBJECTS_WITH_LECTURES_RATIO = 0.9  # 0.9

DURATION = [90, 135]  # [90, 135]
DUR_DISTR = [0.9, 1]  # [0.9, 1]
MAX_AVLBL_ROOMS = 4  # 4


def generate_rooms_file():
    availability = [-1] * ROOM_NUMBER
    for i in random.sample(range(ROOM_NUMBER), ROOM_NUMBER_WITH_MAX_AVAILABILITY):
        availability[i] = MAX_AVAILABILITY
    for i, aroom in enumerate(availability):
        if aroom < 0:
            availability[i] = random.randrange(MIN_AVAILABILITY, MAX_AVAILABILITY, 10)
    DataFrame({"availability": availability}).to_csv("../sample data/" + ROOM_FILE_NAME)


def generate_lecturers_file():
    lecturers = ["lec{0}".format(i) for i in range(LECTURER_NUMBER)]
    DataFrame({"name": lecturers}).to_csv("../sample data/" + LECTURER_FILE_NAME)


def generate_groups_file():
    group_size = [random.randint(MIN_GROUP_SIZE, MAX_GROUP_SIZE) for _ in range(GROUP_NUMBER)]
    DataFrame({"group size": group_size}).to_csv("../sample data/" + GROUPS_FILE_NAME)


def generate_classes_file():
    # wyznaczam liczbę zajęć
    n_semesters = (SEM1_NUMBER * FIELD1_NUMBER) + (SEM2_NUMBER * FIELD2_NUMBER)  # liczba semestrów w sumie
    n_subjects = MEAN_SUBJECT_NUM * n_semesters  # liczba przedmiotów prowadzonych do przeprowadzenia
    n_exercises = 0
    for _ in range(n_subjects):
        for i, n in enumerate(EXERCISES_IN_SUBJECT):
            if random.random() <= EIS_DISTR[i]:
                n_exercises += n
                break
    n_classes = int(n_subjects * SUBJECTS_WITH_LECTURES_RATIO) + n_exercises

    # przygotowuję miejsce do wpisania danych
    lecturer = [-1] * n_classes
    classes_type = [""] * n_classes
    duration = [-1] * n_classes
    rooms = [[]] * n_classes
    groups = [[]] * n_classes

    # przypisanie prowadzących każdy co najmniej jedne, reszta losowo
    idxs = random.sample(range(n_classes), LECTURER_NUMBER)
    for id_ in range(LECTURER_NUMBER):
        lecturer[idxs[id_]] = id_
    for i, id_ in enumerate(lecturer):
        if id_ < 0:
            lecturer[i] = random.randint(0, LECTURER_NUMBER - 1)

    # przypisanie typu zajęć
    idxs = random.sample(range(n_classes), int(n_subjects * SUBJECTS_WITH_LECTURES_RATIO))
    for i in range(len(classes_type)):
        if i in idxs:
            classes_type[i] = "Lecture"
        else:
            classes_type[i] = "Exercises"

    # przypisanie długości
    for i in range(len(duration)):
        for j, n in enumerate(DURATION):
            if random.random() <= DUR_DISTR[j]:
                duration[i] = n
                break

    # przypisanie sal
    for i in range(n_classes):
        rooms[i] = random.sample(range(ROOM_NUMBER), random.randint(1, MAX_AVLBL_ROOMS))

    # przypisanie grup
    gid = 0
    for i in range(n_classes):
        if classes_type[i] == "Lecture":
            groups[i] = random.sample(range(GROUP_NUMBER), random.randint(1, MAX_GROUPS_IN_YEAR))
        else:
            if gid == GROUP_NUMBER:
                gid = 0
            groups[i] = [gid]
            gid += 1

    data = {"lecturer": lecturer, "type": classes_type, "duration": duration, "rooms": rooms, "groups": groups}
    DataFrame(data).to_csv("../sample data/" + CLASSES_FILE_NAME)


generate_groups_file()
generate_lecturers_file()
generate_rooms_file()
generate_classes_file()
