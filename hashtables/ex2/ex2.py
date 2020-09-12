#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []
    trip_dict = {}
    for each_ticket in tickets:
        #print(each_ticket.source, each_ticket.destination)
        trip_dict[each_ticket.source] = each_ticket.destination

    print(trip_dict)

    point_of_trip = trip_dict["NONE"]

    while len(route) < length:
        route.append(point_of_trip)
        point_of_trip = trip_dict[point_of_trip]
    return route


if __name__ == "__main__":

    mytickets = [
        Ticket("PIT", "ORD"),
        Ticket("XNA",  "CID"),
        Ticket("SFO",  "BHM"),
        Ticket("FLG",  "XNA"),
        Ticket("NONE",  "LAX"),
        Ticket("LAX",  "SFO"),
        Ticket("CID",  "SLC"),
        Ticket("ORD",  "NONE"),
        Ticket("SLC",  "PIT"),
        Ticket("BHM",  "FLG")
    ]
    print(reconstruct_trip(mytickets, 10))
