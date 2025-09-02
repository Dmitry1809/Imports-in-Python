import datetime
from application.salary import calculate_salary
from application.db.people import get_employees
import numpy as np

dt = datetime.datetime.today()

a = np.array([1, 2, 3])

if __name__ == '__main__':
    calculate_salary(2,2)
    get_employees(3,4)
    print(dt)
    print(a)
