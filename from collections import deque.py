from collections import deque

class ClinicQueueManager:
    def __init__(self):
        self.queue = deque()
        self.total_seen = 0

    def register_patient(self, name):
        self.queue.append(name)
        print(f"{name} has been added to the queue.")

    def view_queue(self):
        if not self.queue:
            print("No patients in the queue.")
        else:
            print("\nCurrent Waiting List:")
            for i, patient in enumerate(self.queue, start=1):
                print(f"{i}. {patient}")

    def attend_patient(self):
        if not self.queue:
            print("No patients to attend.")
        else:
            patient = self.queue.popleft()
            self.total_seen += 1
            print(f"{patient} is being attended.")

    def total_patients_seen(self):
        print(f"Total patients seen today: {self.total_seen}")


def main():
    clinic = ClinicQueueManager()

    while True:
        print("\n--- Health Clinic Queue Manager ---")
        print("1. Register Patient")
        print("2. View Waiting List")
        print("3. Attend Patient")
        print("4. Total Patients Seen Today")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter patient name: ")
            clinic.register_patient(name)

        elif choice == "2":
            clinic.view_queue()

        elif choice == "3":
            clinic.attend_patient()

        elif choice == "4":
            clinic.total_patients_seen()

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()clinic-queue-manager/
│
├── clinic_queue.py
├── README.md# Health Clinic Queue Manager

A simple Python app to manage patients in a clinic using FIFO (First-In, First-Out).

## Features
- Register patients
- View waiting list
- Attend patients
- Track total patients seen

## How to Run
1. Install Python
2. Run the program:

```bash
python clinic_queue.py