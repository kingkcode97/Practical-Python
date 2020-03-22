import sqlite3

class ContactDatabase(object):
    """Contact Database base class"""

    def __init__(self, filename='example-contact.db'):
        self.database_filename = filename
        conn = sqlite3.connect(self.database_filename)
        curs = conn.cursor()
        curs.execute(
            "CREATE TABLE IF NOT EXISTS contacts \
                (   name        TEXT PRIMARY KEY, \
                    email       TEXT, \
                    phone       TEXT \
                    )"
            )
        conn.commit()
        curs.close()

    def add_contact(self, name='', email='', phone=''):
        try:
            conn = sqlite3.connect(self.database_filename)
            curs = conn.cursor()
            curs.execute(
                "INSERT INTO contacts(name, email, phone) \
                    VALUES(?,?,?)", (name, email, phone)
            )
            conn.commit()
            print('Add contact successfully.')
        except:
            print('Error while adding contact.')
        finally:
            curs.close()

    def update_contact(self, name_to_update='', name='', email='', phone=''):
        try:
            conn = sqlite3.connect(self.database_filename)
            curs = conn.cursor()
            curs.execute(
                "UPDATE contacts SET name=?, email=?, phone=? \
                    WHERE name=?", (name, email, phone, name_to_update)
            )
            conn.commit()
            if curs.rowcount == 0:
                raise Exception
            print("Contact updated successfully.")
        except:
            print("Error while updating contact.")
        finally:
            curs.close()

    def delete_contact(self, name_to_delete=''):
        try:
            conn = sqlite3.connect(self.database_filename)
            curs = conn.cursor()
            curs.execute(
                "DELETE FROM contacts WHERE name=?", (name_to_delete, )
            )
            conn.commit()
            if curs.rowcount == 0:
                raise Exception
            print("Contact deleled successfully.")
        except:
            print('Error while deleting contact.')
        finally:
            curs.close()

    def delete_all_contact(self):
        try:
            conn = sqlite3.connect(self.database_filename)
            curs = conn.cursor()
            curs.execute(
                "DELETE FROM contacts"
            )
            conn.commit()
            if curs.rowcount == 0:
                raise Exception
            print("Contact deleted successfully.")
        except:
            print("Error while deleting contact.")
        finally:
            curs.close()

    def list_all_contacts(self):
        try:
            conn = sqlite3.connect(self.database_filename)
            curs = conn.cursor()
            curs.execute(
                "SELECT * FROM contacts"
            )
            contacts = curs.fetchall()
            print("Contact retrieved successfully.")
            return contacts
        except:
            print("Error while retrieving contacts.")
        finally:
            curs.close()

    def get_contact(self, name_to_get):
        try:
            conn = sqlite3.connect(self.database_filename)
            curs = conn.cursor()
            curs.execute(
                "SELECT * FROM contacts WHERE name=?", name_to_get
            )
            contacts = curs.fetchall()
            if len(contacts) == 0:
                raise Exception
            print("Contact retrieved successfully.")
            return contacts[0]
        except:
            print("Error while retrieving contact.")
        finally:
            curs.close()


class Application(object):
    """Application base class"""

    def __init__(self, filename):
        self.database = ContactDatabase(filename)

    def add(self):
        name, email, phone = self.get_info()
        self.database.add_contact(name=name, email=email, phone=phone)

    def update(self):
        name_to_update = input("Enter the name to update: ")
        print("Enter updated information.")
        name, email, phone = self.get_info()
        self.database.update_contact(name_to_update=name_to_update, name=name, email=email, phone=phone)

    def delete(self):
        name_to_delete = input("Enter the name to delete: ")
        print("Enter deleted information.")
        self.database.delete_contact(name_to_delete=name_to_delete)

    def reset(self):
        print("Deleted contacts.")
        self.database.delete_all_contact()

    def view_all(self):
        print("Viewed all contacts.")
        contacts = self.database.list_all_contacts()
        for contact in contacts:
            self.print_contact(contact)

    def get_info(self):
        name = input("Name: ")
        email = input('Email: ')
        phone = input('Phone: ')
        return name, email, phone

    def print_contact(self, contact):
        print()
        print(f'Name: {contact[0]}')
        print(f'Email: {contact[1]}')
        print(f'Phone: {contact[2]}')

    def search(self):
        name_to_search = input("Enter the name to search: ")
        contact = self.database.get_contact(name_to_search)
        if contact:
            self.print_contact(contact)

    def __str__(self):
        return """
                1. Add a new contact.
                2. Update a contact.
                3. Delete a contact.
                4. View all contacts.
                5. Find a contact.
                6. Reset all contacts.
                7. Exit.
        """

def main():
    app = Application('contact-book.db')
    choice = ''
    while choice != 7:
        print(app)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            app.add()
        elif choice == 2:
            app.update()
        elif choice == 3:
            app.delete()
        elif choice == 4:
            app.view_all()
        elif choice == 5:
            app.search()
        elif choice == 6:
            app.reset()
        elif choice == 7:
            print("Exiting...")
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()