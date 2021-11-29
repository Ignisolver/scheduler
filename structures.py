from typing import Iterable



class Classes:  # zajęcia - ogólnie
    pass


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
        self.week_schedule: WeekSchedule = ...


class Room:  # sala
    def __init__(self):
        self.id_ = ...
        self.capacity = ...
        self.week_schedule: WeekSchedule = ...


class Group:  # grupa
    def __init__(self):
        self.id_ = ...
        self.students_ids = ...
        self.subjects_ids = ...
        self.week_schedule: WeekSchedule = ...


class Subject:  # przedmiot
    def __init__(self):
        self.id_ = ...
        self.week_classes_duration = ...
        self.week_lecture_duration = ...
        self.lecturers_ids = ...
        self.groups_ids = ...


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

    def calc_goal_function(self):
        pass

    def _calc_week_FO(self):
        pass

    def _calc_week_FD(self):
        pass

    def calc_week_FP(self):
        pass

    def _calc_week_FR(self):
        pass


class DaySchedule:
    def __init__(self):
        self.classes: Iterable[Classes] = ...

    def add_classes(self):
        pass

    def check_daily_maximum(self):
        pass

    def calc_day_FO(self):
        pass

    def calc_day_FP(self):
        pass

    def calc_day_FR(self):
        pass


class GlobalSchedule:
    def __init__(self):
        self.lecturers: Iterable[Lecturer] = ...
        self.groups: Iterable[Group] = ...
        self.rooms: Iterable[Room] = ...
