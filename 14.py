class Team:
    def __init__(self, team_id, team_name, event, members):
        self.team_id = team_id
        self.team_name = team_name
        self.event = event
        self.members = members
        self.next = None
class EventManager:
    def __init__(self):
        self.head = None
        self.events = [
            "Hackathon",
            "Paper Presentation",
            "Coding Contest"
        ]
        self.team_id = 1001
    def register_event(self):
        print("\nAvailable Events:")
        for i, event in enumerate(self.events, 1):
            print(i, ".", event)
        try:
            choice = int(input("Enter event number: "))
            if choice < 1 or choice > len(self.events):
                print("Invalid event.")
                return
            event = self.events[choice - 1]
            team_name = input("Enter team name: ")
            n = int(input("Enter number of members (1-4): "))
            if n < 1 or n > 4:
                print("Team can have maximum 4 members.")
                return
            members = []
            for i in range(n):
                print("\nMember", i + 1)
                name = input("Enter name: ")
                roll = input("Enter roll number: ")
                dept = input("Enter department: ")
                current = self.head
                while current is not None:
                    for member in current.members:
                        if member[1] == roll:
                            print("Student already registered.")
                            return
                    current = current.next
                members.append((name, roll, dept))
            new_team = Team(
                "T" + str(self.team_id),
                team_name,
                event,
                members
            )
            self.team_id += 1
            if self.head is None:
                self.head = new_team
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = new_team
            print("\nTeam registered successfully.")
            print("Team ID:", new_team.team_id)
        except ValueError:
            print("Please enter a valid number.")
    def cancel_registration(self):
        team_id = input("Enter Team ID: ")
        current = self.head
        previous = None
        while current is not None:
            if current.team_id == team_id:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                print("Registration cancelled successfully.")
                print("Team:", current.team_name)
                return
            previous = current
            current = current.next
        print("Team ID not found.")
    def display_events(self):
        print("\nAvailable Events:")
        for i, event in enumerate(self.events, 1):
            print(i, ".", event)
    def event_wise_participants(self):
        event = input("Enter event name: ")
        current = self.head
        found = False
        print("\nParticipants in", event)
        while current is not None:
            if current.event.lower() == event.lower():
                print("\nTeam ID:", current.team_id)
                print("Team Name:", current.team_name)
                for member in current.members:
                    print(member[0],"-", member[1], "-",member[2])
                   found = True
current = current.next
if not found:
            print("No participants found.")
    def count_participants(self):
        event = input("Enter event name: ")
        current = self.head
        team_count = 0
        member_count = 0
        while current is not None:
            if current.event.lower() == event.lower():
                team_count += 1
                member_count += len(current.members)
            current = current.next
        print("\nEvent:", event)
        print("Total Teams:", team_count)
        print("Total Participants:", member_count)
    def search_student(self):
        roll = input("Enter roll number: ")
        current = self.head
        while current is not None:
            for member in current.members:
                if member[1] == roll:
                    print("\nStudent found.")
                    print("Name:", member[0])
                    print("Roll Number:", member[1])
                    print("Department:", member[2])
                    print("Team ID:", current.team_id)
                    print("Team Name:", current.team_name)
                    print("Event:", current.event)
                    return
            current = current.next
        print("Student not found.")
    def view_registration(self):
        team_id = input("Enter Team ID: ")
        current = self.head
        while current is not None:
            if current.team_id == team_id:
                print("\nTeam Registration Details")
                print("Team ID:", current.team_id)
                print("Team Name:", current.team_name)
                print("Event:", current.event)
                print("Number of Members:", len(current.members))
                print("\nMembers:")
                for i, member in enumerate(current.members, 1):
                    print(i, ".",member[0], "-",member[1], "-",member[2])
                   return
                  current = current.next
           print("Team ID not found.")
manager = EventManager()
while True:
    print("\nDigital Campus Event Management System")
    print("1. Register for Event")
    print("2. Cancel Registration")
    print("3. Display Events")
    print("4. Event-wise Participants")
    print("5. Count Participants by Event")
    print("6. Search Student")
    print("7. View Registration")
    print("8. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        manager.register_event()
    elif choice == "2":
        manager.cancel_registration()
    elif choice == "3":
        manager.display_events()
    elif choice == "4":
        manager.event_wise_participants()
    elif choice == "5":
        manager.count_participants()
    elif choice == "6":
        manager.search_student()
    elif choice == "7":
        manager.view_registration()
    elif choice == "8":
        print("Thank you.")
        break
    else:
        print("Invalid choice.")
