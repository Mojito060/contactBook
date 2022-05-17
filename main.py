import sqlite3

con = sqlite3.connect('contacts.db')

cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS contacts
               (name text, phone text, address text)''')
con.commit()
x = 0
clear = "\n" * 100  # Andere Lösung wär cool

while x == 0:
    print(clear)
    option = input("Was möchtest du machen? \n1: Neuen Kontakt erstellen \n2: Kontakt suchen")

    if option == "1":
        contactName = input("Wie heißt der Kontakt?")
        contactNumber = input("Wie lautet die Telefonnummer?")
        contactAddress = input("Wie lautet die Adresse des Kontakts?")
        cur.execute("INSERT INTO contacts (name, phone, address)VALUES (?, ?, ?)",
                    (contactName, contactNumber, contactAddress))
        con.commit()
        enter = input("Der Kontakt wurde erstellt \nDrücke irgendeine Taste um wieder ins Menü zu kommen")

    if option == "2":
        contactName = input("Wie heißt der Kontakt?")
        sql = '''SELECT * FROM contacts WHERE name=\"''' + contactName + "\";"
        for row in cur.execute(sql):
            print(row)
        enter = input("Drücke irgendeine Taste um wieder ins Menü zu kommen")
