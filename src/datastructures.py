
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""

from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        # fill this method and update the return
        member['id'] = self._generateId()
        self._members.append(member)
        return member
    

    def delete_member(self, id):
        for member in self._members:
            if member.get('id') == id:
                self._members.remove(member)
                return {'done': True}
        # fill this method and update the return


    def get_member(self, id):
        for member in self._members:
            if member.get('id') == id:
                return member
        # fill this method and update the return
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        (print(self._generateId()))
        return self._members
