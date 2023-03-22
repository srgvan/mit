#!/usr/bin/env python3


lastname = input("Enter your last name: ")
firstname = input("Enter your first name: ")

# Three different ways of formating a string
version_one = f"{firstname} {lastname}"
version_two = "{0} {1}".format(firstname, lastname)
version_three = "%s %s" % (firstname, lastname)
