from collections import deque

# Function to search for a seller in a person's friend list


def check_for_seller(person):
    return person[0].lower() == 's'


def breadth_first_search(person_list, person_name):
    # Create a queue to search
    search_queue = deque()
    # Add first neighbours of the person in the queue for searching
    search_queue += person_list[person_name]
    # This is necessary as without this if both person have relation to each other the loop will be infinite
    person_searched = []
    # Search queue if it is not empty

    # Pop a item from a queue and check if if the person is seller
    # If the person is seller return the person
    # Else Add his adjecent item (frinds) to the queue

    while (search_queue):
        person = search_queue.popleft()
        if (person not in person_searched):
            if (check_for_seller(person)):
                print(" Seller found. Seller is", person)
                return person
            else:
                search_queue += person_list[person]
                person_searched.append(person)
        return False


person_list = {
    "Suman": ["Awan", "Santa", "Kristina", "Michael", "Agya"],
    "Awan": ["Suman", "Agya"],
    "Agya": ["Awan"],
    "Michael": ["Agya"],
    "Krish": []
}

breadth_first_search(person_list, "Awan")
