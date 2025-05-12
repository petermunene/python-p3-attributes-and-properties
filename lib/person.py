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
    def __init__(self, name="John",job="Admin"):
        self.name=name
        self.job=job
    @property
    def name (self):
        return self._name
    @name.setter
    def name (self,value):
        if not isinstance(value, str) or not (1<len(value)<25):
            print("Name must be string between 1 and 25 characters.")
        else :
            new_name=value.title()
            self._name=new_name
    @property
    def job(self):
        return self._job
    @job.setter
    def job (self,job_name):
        if job_name in (APPROVED_JOBS):
            self._job=job_name
        else :
            print("Job must be in list of approved jobs.")
    pass
