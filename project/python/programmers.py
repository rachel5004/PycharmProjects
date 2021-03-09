def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]


def solution2(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant, completion):
        if p != c:
            return p

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

#2
def solution3(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] in phone_book[i + 1]:
            return False
    return True
def solution4(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True
p = ["12","123","1235","567","88"]
print(solution3(p))