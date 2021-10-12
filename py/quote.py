#!/usr/bin/python3

import re
import sys

# Constants
Male = 0
Female = 1

EmployeeOnly = 0
Dependents = 1
LifeOnly = 2

class Employee:
    def __init__(self, line):
        (name, sex, age, coverage) = line.split()
        self.name = name

        sex = sex.lower()
        if sex == 'm':
            self.sex = Male
        elif sex == 'f':
            self.sex = Female
        else:
            raise Exception("Unknown sex ({}) for employee {}".format(sex, name))
        self.age = int(age)
        coverage = coverage.lower()
        if coverage == 'e':
            self.coverage = EmployeeOnly
        elif coverage == 'd':
            self.coverage = Dependents
        elif coverage == 'l':
            self.coverage = LifeOnly
        else:
            raise Exception("Unknown coverage ({}) for employee {}".format(coverage, name))

class AgeGroup:
    _rates = []
    def __init__(self, line):
        # AGE MALE    FEMALE  DEPENDENT   LIFE/MALE LIFE/FEMALE WDI/MALE WDI/FEMALE
        (age, mcost, fcost, mlife, flife, mwdi, fwdi, dcost) = line.split()
        self.age = int(age)
        self.employee = [float(mcost), float(fcost)]
        self.life = [float(mlife), float(flife)]
        self.wdi = [float(mwdi), float(fwdi)]
        self.dependent = float(dcost)
        AgeGroup._rates.append(self)

    def find(age):
        rate = None
        for r in AgeGroup._rates:
            if r.age > age:
                break
            rate = r
        return rate

if len(sys.argv) != 3:
    print("Usage: quote.py Company.txt Rates.dat\n")
    exit(1)

# Variables for a single run
company = None
coverage = None
employees = []
carrier = None
dentalWithLifePlusEmployee = None
dentalForDependents = None
rates = []

def parseCoverage(str):
    cov = { 'dental' : False, 'wdi' : False }
    for arg in str.split():
        cov[arg] = True
    return cov

def cleanup(str):
    return re.sub('#.*', '', str).strip()

# read company data, should be:
# Company Name
# dental wdi
# emp 1
# emp 2

with open(sys.argv[1]) as file:
    for l in file:
        l = cleanup(l)
        if not l:
            continue
        if not company:
            company = l
        elif coverage == None:
            coverage = parseCoverage(l.lower())
        else:
            employees.append(Employee(l))

# DENTAL FOR LIFE + EMPLOYEE
1.50
# DENTAL FOR DEPENDENT
1.75

with open(sys.argv[2]) as file:
    for l in file:
        l = cleanup(l)
        if not l:
            continue
        if not carrier:
            carrier = l
        elif not dentalWithLifePlusEmployee:
            dentalWithLifePlusEmployee = float(l)
        elif not dentalForDependents:
            dentalForDependents = float(l)
        else:
            rates.append(AgeGroup(l.lower()))

print("Proposal for {}".format(company))
print("Carrier: {}".format(carrier))
print('')
print('Name        |Age|Sex|Emp Cost|Dep Cost|     WDI|     DNT|   Total')
for e in employees:
    rate = AgeGroup.find(e.age)
    emp = rate.employee[e.sex] if e.coverage != LifeOnly else 0
    dep = rate.dependent if e.coverage == Dependents else 0
    wdi = rate.wdi[e.sex] if coverage['wdi'] else 0
    dental = 0
    if coverage['dental']:
        dental = 0

    empTotal = emp + dep + wdi + dental
    print("{:12}|{:>3}|{:^3}|{:8.2f}|{:8.2f}|{:8.2f}|{:8.2f}|{:8.2f}".format(
        e.name,
        e.age,
        'MF'[e.sex],
        emp,
        dep,
        wdi,
        dental,
        empTotal
        ))
