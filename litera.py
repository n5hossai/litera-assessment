# // Input: []
# // Input: [[1,2], [2,3]]
# // Input: [[2, 10], [3, 4], [6, 9]]; 
# // Input: [[1, 3], [2, 4], [2, 5], [3, 4], [3, 6], [4, 5], [5, 6]]

#compares to events(consisting of start and end times) and checks for
#       -negative values
#       -if start time > end time
def isOverlap(event1, event2):
    for i in [event1[0], event1[1], event2[0], event2[1]]:
        if i < 0:#checks if time is negative
            raise ValueError("Time cannot be negative")
        elif  event1[0] > event1[1] or event2[0] > event2[1]:#checks if start time is greater than end time
            raise ValueError("Start time cannot be greater than end time")
    #if overlap happens:
    if (event1[0] < event2[1] and event1[1] > event2[0]) or (event2[0]< event1[1] and event2[1] > event1[0]):
        return True
    else:
        return False

#double_booked() will return the sequence of all pairs of overlapping events
def double_booked(lst):
    res_seq = [] #result sequence
    #sorted start & end list in ascending order with key
    intervals = lst.sort(key = lambda i: i[0])
    l = len(lst)
    i = 0
    while i < l: #iterates the whole list
        keyEvent = lst[i]
        j = i +1
        while j < l:
            if isOverlap(keyEvent, lst[j]):#calling helper function to compare the events
                res_seq.append([keyEvent, lst[j]])#if overlap is found, it is added to the result sequence
            j+=1
        i+=1
    return res_seq
'''
double_booked([[2, 10], [3, 4], [6, 9]])
double_booked([[1, 3], [2, 4], [2, 5], [3, 4], [3, 6], [4, 5], [5, 6]])

double_booked([[1,2], [2,3]])
double_booked([])
'''