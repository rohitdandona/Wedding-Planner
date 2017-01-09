# wedding.py : Place people on tables of n size such that no person knows another on a table.
# 
# Authors: Rohit Dandona, Rahul Velayutham, Mihir Thatte
#
# A relationship dictionary is implemented storing a list of friends for each individual. The place_people function 
# selects a person randomly and places him/her with a group using the relationship dictionary such that 
# no person is friends with another in the group. This is repeated till all the people are placed in groups.
#
# The code creates multiple (100) possible solutions and selects the one with the least number of
# tables required to place people.


import copy
import os
import sys
import random

# Compute relationship dictionary
def make_relations(filename):
    f=open(filename,'r')
    linecount=sum(1 for line in f)
    relations={}
    f.seek(0,0)
    while linecount!=0:
        linetext=f.readline().rstrip('\n').rstrip('\r')
        data=linetext.split(" ",)
        if data!=[""]:
            n=len(data)
            i=1
            if n==1:
                if relations.has_key(data[0]):
                    h=[]
                    h=relations[data[0]]
                    h.append(data[0])
                    relations[data[0]]=h
                else:
                    relations[data[0]]=[data[0]]
            while i<n:
                if relations.has_key(data[0]):
                    h=relations[data[0]]
                    h.append(data[i])
                    relations[data[0]]=h
                else:
                    relations[data[0]]=[data[i]]
                i=i+1
            i=n-1
            while i!=0:
                if relations.has_key(data[i]):
                    h=relations[data[i]]
                    h.append(data[0])
                    relations[data[i]]=h
                else:
                    relations[data[i]]=[data[0]]
                i=i-1
        linecount=linecount-1
    return relations

# Place people
def place_people(relationship, table_size):

    solutions = []
    answer = []
    for i in range (100):
        people = filter(lambda a: a != '', relationship.keys())
	table_groups = []
        while len(people) > 0:
            group = []
            p1 = random.choice(people)
            group.append(p1)
            people.remove(p1)
            dup_people = copy.deepcopy(people)
            while len(dup_people) > 0:
                if len(group) == table_size:
                    table_groups.append(group)
                    for p in group:
                        if p in people:
                            people.remove(p)
                    group = []
                    break
                else:
                    person = random.choice(dup_people)
                    dup_people.remove(person)
                    fit = True
                    for existing_person in group:
                        if person in relationship[existing_person]:
                            fit = False
                            break
                    if fit:
                        group.append(person)

            if (len(group) != table_size or len(group) == table_size) and len(group) != 0:
                table_groups.append(group)
                for p in group:
                    if p in people:
                        people.remove(p)

        solutions.append(table_groups)

    m = min(map(len, solutions))
    for sol in solutions:
        if len(sol) == m:
            answer = sol
            break

    return answer

filename = sys.argv[1]
table_size = int(sys.argv[2])

relationship = make_relations(filename)
table_groups = place_people(relationship, table_size)

print "Placements: "
print "Number of tables: ", len(table_groups)
print table_size,
for table in table_groups:
    comma_separated_list = ",".join(table)
    print comma_separated_list,





