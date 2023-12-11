#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
   def __init__(self, name, job):
        self._name = None
        self._job = None

        # Validate and set the job using the property setter
        self.job = job

        # Validate and set the name using the property setter
        self.name = name

        @property
        def name(self):
         return self._name

        @name.setter
        def name(self, value):
         if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be a string under 25 characters.")
         else:
            self._name = value.title()

        @property
        def job(self):
         return self._job

        @job.setter
        def job(self, value):
          if value not in APPROVED_JOBS:
            print("Job must be in the list of approved jobs.")
          else:
            self._job = value

# Example usage:
person_instance = Person(name="John Doe", job="Doctor")
print(person_instance.name)  # Output: John Doe
print(person_instance.job)   # Output: Doctor

# Trying to set an invalid job
person_instance.job = "Plumber"  # Output: Job must be in the list of approved jobs.
pass
