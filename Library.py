# Author: Andrew Kamand
# Date: 1/22/2020
# Description: Code for a Library that is made up of 6 classes: LibraryItem, and three classes that inherit from
# LibraryItem -- Book, Album and Movie --, Patron, and Library. Contains a list of members and holdings (items)
# and can execute simple checkout and request item methods, and calculate fines for overdue items.


class LibraryItem:
    """A LibraryItem object represents a library item with an id code and title. It also contains information pertaining
     to who last checked out said item, who requested said item, and the date it was checked out."""
    def __init__(self, id_code, title):
        self._id_code = id_code
        self._title = title
        # a LibraryItem can be "ON_SHELF", "ON_HOLD_SHELF", or "CHECKED_OUT"
        self._location = "ON_SHELF"
        self._checked_out_by = None
        self._requested_by = None
        # date_checked_out will be set to the current_date of the Library which is an integer value, use 0 as placeholder
        self._date_checked_out = 0

    def set_id_code(self, id_code):
        """Sets the LibraryItem's id_code."""
        self._id_code = id_code

    def set_title(self, title):
        """Sets the LibraryItem's title."""
        self._title = title

    def set_location(self, location):
        """Sets the LibraryItem's location."""
        self._location = location

    def set_checked_out_by(self, checked_out_by):
        """Sets the LibraryItem's checked_out_by."""
        self._checked_out_by = checked_out_by

    def set_requested_by(self, requested_by):
        """Sets the LibraryItem's requested_by."""
        self._requested_by = requested_by

    def set_date_checked_out(self, date_checked_out):
        """Sets the LibraryItem's date_checked_out."""
        self._date_checked_out = date_checked_out

    def get_id_code(self):
        """Returns the LibraryItem's id_code."""
        return self._id_code

    def get_title(self):
        """Returns the LibraryItem's title."""
        return self._title

    def get_location(self):
        """Returns the LibraryItem's location."""
        return self._location

    def get_checked_out_by(self):
        """Returns the LibraryItem's checked_out_by."""
        return self._checked_out_by

    def get_requested_by(self):
        """Returns the LibraryItem's requested_by."""
        return self._requested_by

    def get_date_checked_out(self):
        """Returns the LibraryItem's date_checked_out."""
        return self._date_checked_out


class Book(LibraryItem):
    def __init__(self, id_code, title, author):
        """A Book represents a LibraryItem sub-object with the addition of an author field."""
        super().__init__(id_code, title)
        self._author = author

    def set_author(self, author):
        """Sets the Book's author."""
        self._author = author

    def get_check_out_length(self):
        """Returns the Book's checkout length, which by default, is 21 days."""
        return 21

    def get_author(self):
        """Returns the Book's author."""
        return self._author


class Album(LibraryItem):
    def __init__(self, id_code, title, artist):
        """An Album represents a LibraryItem sub-object with the addition of an artist field."""
        super().__init__(id_code, title)
        self._artist = artist

    def set_artist(self, artist):
        """Sets the Album's artist."""
        self._artist = artist

    def get_check_out_length(self):
        """Returns the Album's checkout length, which by default, is 14 days."""
        return 14

    def get_artist(self):
        """Returns the Album's artist."""
        return self._artist


class Movie(LibraryItem):
    def __init__(self, id_code, title, director):
        """A Movie represents a LibraryItem sub-object with the addition of an director field."""
        super().__init__(id_code, title)
        self._director = director

    def set_director(self, director):
        """Sets the Movie's director."""
        self._director = director

    def get_check_out_length(self):
        """Returns the Movie's checkout length, which by default, is 14 days."""
        return 7

    def get_director(self):
        """Returns the Movie's director."""
        return self._director


class Patron:
    def __init__(self, id_num, name):
        """A Patron represents an object with an id_num and name, and other associated fields."""
        self._id_num = id_num
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def set_id_num(self, id_num):
        """Sets the Patron's id_num."""
        self._id_num = id_num

    def set_name(self, name):
        """Sets the Patron's name."""
        self._name = name

    def set_fine_amount(self, fine_amount):
        """Sets the Patron's fine amount."""
        self._fine_amount = fine_amount

    def get_id_num(self):
        """Returns the Patron's id_num."""
        return self._id_num

    def get_name(self):
        """Returns the Patron's name."""
        return self._name

    def get_checked_out_items(self):
        """Returns the Patron's checked_out_items."""
        return self._checked_out_items

    def get_fine_amount(self):
        """Returns the Patron's fine_amount."""
        return self._fine_amount

    def add_library_item(self, library_item):
        """Adds the specified LibraryItem to checked_out_items."""
        self._checked_out_items.append(library_item)

    def remove_library_item(self, library_item):
        """Removes the specified LibraryItem from checked_out_items."""
        self._checked_out_items.remove(library_item)

    def amend_fine(self, fine_change):
        """Amends fine_amount by fine_change, either + or -."""
        self._fine_amount += fine_change


class Library:
    def __init__(self):
        """A Library represents an object with a collection of holdings and members, and a current date."""
        self._current_date = 0
        self._holdings = []
        self._members = []

    def set_current_date(self, current_date):
        """Sets the Library's current_date."""
        self._current_date = current_date

    def get_current_date(self):
        """Returns the Library's current_date."""
        return self._current_date

    def get_holdings(self):
        """Returns the Library's list of holdings."""
        return self._holdings

    def get_members(self):
        """Returns the Library's list of members."""
        return self._members

    def add_library_item(self, library_item):
        """Adds a LibraryItem to list of holdings"""
        self._holdings.append(library_item)

    def add_patron(self, patron):
        """Adds a patron to list of members."""
        self._members.append(patron)

    def get_library_item(self, item_id):
        """Returns the LibraryItem corresponding to the ID parameter, or None if no such LibraryItem is found in holdings."""
        # check holdings for a LibraryItem id match
        for x in self._holdings:
            if item_id == x.get_id_code():
                return x
        else:
            return None

    def get_patron(self, patron_id):
        """Returns the Patron corresponding to the ID parameter, or None if no such Patron is a member."""
        # check members for a Patron id match
        for x in self._members:
            if patron_id == x.get_id_num():
                return x
        else:
            return None

    def check_out_library_item(self, patron_id, item_id):
        """Update the LibraryItem's checked_out_by, date_checked_out, location, and return "check out successful" if id's are valid.
        Otherwise, if patron or item id's are invalid, return appropriate notification messages."""
        # find Patron and LibraryItem in members and holdings (respectively) that match given id's
        patron_match = self.get_patron(patron_id)
        item_match = self.get_library_item(item_id)

        # if the specified Patron is not in the Library's members, return "patron not found"
        if patron_match == None:
            return "patron not found"

        # if the specified LibraryItem is not in the Library's holdings, return "item not found"
        if item_match == None:
            return "item not found"

        # reminder, a LibraryItem can be "ON_SHELF", "ON_HOLD_SHELF", or "CHECKED_OUT"
        # if the specified LibraryItem is already checked out, return "item already checked out"
        if item_match.get_location() == "CHECKED_OUT":
            return "item already checked out"

        # if the specified LibraryItem is on hold by another Patron, return "item on hold by other patron"
        if item_match.get_location() == "ON_HOLD_SHELF" and item_match.get_requested_by() != patron_match:
            return "item on hold by other patron"

        else:
            # update the LibraryItem's checkedOutBy, dateCheckedOut and Location
            item_match.set_checked_out_by(patron_id)
            item_match.set_date_checked_out(self._current_date)
            item_match.set_location("CHECKED_OUT")

            # if the LibraryItem was on hold for this Patron, update requestedBy
            if item_match.get_requested_by() == patron_match:
                item_match.set_requested_by(None)

            # update the Patron's checkedOutItems and return "check out successful"
            patron_match.add_library_item(item_id)
            return "check out successful"

    def return_library_item(self, item_id):
        """Update a Library to reflect a returned LibraryItem if the specified id is valid. Otherwise, return appropriate
        notifications."""
        # find LibraryItem in holdings
        item_match = self.get_library_item(item_id)

        # if the specified LibraryItem is not in the Library's holdings, return "item not found"
        if item_match == None:
            return "item not found"

        # if the LibraryItem is not checked out, return "item already in library"
        if item_match.get_location() != "CHECKED_OUT":
            return "item already in library"

        else:
            # update the Patron's checkedOutItems
            patron_id = item_match.get_checked_out_by()
            patron_match = self.get_patron(patron_id)
            patron_match.remove_library_item(item_id)

            # update the LibraryItem's location depending on whether another Patron has requested it (if so, it should
            # go on the hold shelf)
            if item_match.get_requested_by() == None:
                item_match.set_location("ON_SHELF")
            else:
                item_match.set_location("ON_HOLD_SHELF")

            # update the LibraryItem's checkedOutBy and return "return successful"
            item_match.set_checked_out_by(None)
            return "return successful"

    def request_library_item(self, patron_id, item_id):
        """Updates a LibraryItem's requested_by to specified patron, if id's are valid. Otherwise, return appropriate
        notifications."""
        # find Patron and LibraryItem in members and holdings (respectively) that match given id's
        patron_match = self.get_patron(patron_id)
        item_match = self.get_library_item(item_id)

        # if the specified Patron is not in the Library's members, return "patron not found"
        if patron_match == None:
            return "patron not found"

        # if the specified LibraryItem is not in the Library's holdings, return "item not found"
        if item_match == None:
            return "item not found"

        # if the specified LibraryItem is already requested, return "item already on hold"
        if item_match.get_location() == "ON_HOLD_SHELF":
            return "item already on hold"

        else:
            # update the LibraryItem's requestedBy
            item_match.set_requested_by(patron_id)

            # if the LibraryItem is on the shelf, update its location to on hold and return "request successful"
            if item_match.get_location() == "ON_SHELF":
                item_match.set_location("ON_HOLD_SHELF")
            return "request successful"

    def pay_fine(self, patron_id, fine_amount):
        """Reduces a patron's total fine by specified fine_amount, provided the patron id is valid."""
        # find Patron in members that matches given id
        patron_match = self.get_patron(patron_id)

        # if the specified Patron is not in the Library's members, return "patron not found"
        if patron_match == None:
            return "patron not found"

        # use amendFine to update the Patron's fine; return "payment successful"
        patron_match.amend_fine(fine_amount*-1)
        return "payment successful"

    def increment_current_date(self):
        """Increments current date and increases each Patron's fines by 10 cents for each overdue LibraryItem they have
        checked out (using amendFine)"""
        self._current_date += 1

        # increase each Patron's fines by 10 cents for each overdue LibraryItem they have checked out (using amendFine)
        for x in self._members:
            for item in x.get_checked_out_items():
                item = self.get_library_item(item)
                if self._current_date - item.get_date_checked_out() > item.get_check_out_length():
                    x.amend_fine(0.10)

b1 = Book("345", "Phantom Tollbooth", "Juster")
a1 = Album("456", "...And His Orchestra", "The Fastbacks")
m1 = Movie("567", "Laputa", "Miyazaki")
print("The author of b1 is: ")
print(b1.get_author())
print("The artist of a1 is: ")
print(a1.get_artist())
print("The director of m1 is: ")
print(m1.get_director())


p1 = Patron("abc", "Felicity")
print("The name of patron 1 is: (should be Felicity)")
print(p1.get_name())
p2 = Patron("bcd", "Waldo")
print("The name of patron 2 is: (should be Waldo)")
print(p2.get_name())

lib = Library()
lib.add_library_item(b1)
lib.add_library_item(a1)
lib.add_library_item(m1)
lib.add_patron(p1)
lib.add_patron(p2)

print(lib.check_out_library_item("bcd", "345"))
print(lib.request_library_item("abc", "345"))
print(lib.return_library_item("345"))
print(lib.check_out_library_item("abc","345"))