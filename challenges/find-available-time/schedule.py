
# OBJECTIVE: Given a list of appointments from a Calendar, determine when a person is available

class Appointment:
    def __init__(self, start, end):
        self.start = start
        self.end = end

appointments = [
    Appointment(1,2), Appointment(1,3), Appointment(3,4),  Appointment(4,5), Appointment(6,8)
]

def available(t):
    availability = []

    # Sort appointments in case they are no ordered
    sorted_times = sorted(t, key=lambda item: (item.start, item.end))

    # Generate the first appointment's conclusion so we can be determining when to check for free time
    current_end = sorted_times[0].end

    for slot in sorted_times[1:]:
        if slot.start > current_end: # Gap is found if start time happens after our last meeting ends
            # Add found gap in schedule to availability
            availability.append([current_end, slot.start])
        current_end = max(slot.end, current_end) 
    return availability

if __name__ == '__main__':
    answer = available(appointments)
    print(answer)

