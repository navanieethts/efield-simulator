# Dependencies and modules
import numpy as np

# Constants
k = 8.9875517923 * (10**9)

listOfCharges = []  # The location of all charges are stored here

while True:
    status = int(
        input(
            "Enter 1 for adding charge, 2 for finding Electric field and -1 for exit: "
        )
    )
    if status == 1:
        qq = int(input("Charge: "))
        qx = int(input("x-component: "))
        qy = int(input("y-component: "))
        qz = int(input("z-component: "))

        qloc = np.array([qx, qy, qz])
        listOfCharges.append((qq, qloc))
    elif status == 2:
        Elecfield = np.zeros(3)
        locationx = int(input("x-component of the test-point: "))
        locationy = int(input("y-component of the test-point: "))
        locationz = int(input("z-component of the test-point: "))

        testloc = np.array([locationx, locationy, locationz])
        for i in listOfCharges:
            rvector = testloc - i[1]
            elec = ((k * i[0]) / (np.linalg.norm(rvector)) ** 2) * rvector
            Elecfield += elec

        print(
            f"The Electric field at point {testloc} is {Elecfield}",
        )

    elif status == -1:
        break
