class Student:
    def __init__(self):
        self.id_ = ...
        self.group_id = ...


class Lecturer:
    def __init__(self):
        self.id_ = ...
        self.subject_id = ...
        self.amount_of_hours = ...
        self.group_id = ...


class Room:  # sala
    def __init__(self):
        self.id_ = ...
        self.capacity = ...
        self.week_schedule = ...


class Group:  # grupa
    def __init__(self):
        self.id_ = ...
        self.students_ids = ...
        self.subjects_ids = ...
        self.week_schedule = ...


class Subject:  # przedmiot
    def __init__(self):
        self.id_ = ...
        self.week_classes_duration = ...
        self.week_lecture_duration = ...
        self.lecturers_ids = ...
        self.groups_ids = ...


class Classes:  # zajęcia - ogólnie
    pass


class Lecture(Classes):  # wykład
    def __init__(self):
        self.id_ = ...
        self.lecturer_id = ...
        self.duration = ...
        self.field_id = ...
        self.start_time = ...
        self.end_time = self.start_time + self.duration


class Exercises(Classes):  # ćwiczenia
    def __init__(self):
        self.id_ = ...
        self.lecturer_id = ...
        self.duration = ...
        self.group_id = ...
        self.start_time = ...
        self.end_time = self.start_time + self.duration


class Field:  # kierunek
    def __init__(self):
        self.groups_ids = ...
        self.subjects_ids = ...


class WeekSchedule:
    def __init__(self):
        self.day_schedules = ...


class DaySchedule:
    def __init__(self):
        self.classes = ...


class GlobalSchedule:
    def __init__(self):
        self.lecturers = ...
        self.students = ...
        self.rooms = ...
