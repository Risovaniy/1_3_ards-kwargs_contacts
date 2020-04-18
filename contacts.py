class Contact:

    def __init__(self, first_name, last_name, phone, *args, favorite=False, **kwargs) -> None:
        # self.id_number = len(my_book.contacts)
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.phone = str(phone)
        self.favorite = bool(favorite)
        self.notes = ''.join(args)
        self.add_data = kwargs

    def favorite(self) -> str:
        if self.favorite:
            return "да"
        else:
            return "нет"

    def __str__(self) -> str:
        add_datas = []
        for key, value in self.add_data.items():
            add_datas.append('\t')
            add_datas.append(key)
            add_datas.append(' : ')
            add_datas.append(value)
            add_datas.append('\n')
        add_datas = ''.join(add_datas)
        if not self.notes:
            """Delete new line bofore additional data, when there are no notes."""

            return (f'Имя: {self.first_name}\nФамилия: {self.last_name}\nТелефон: {self.phone}\n'
                    f'В избранных: {Contact.favorite(self)}\nДополнительная информация:\n'
                    f'{add_datas}\n')
        else:
            return (f'Имя: {self.first_name}\nФамилия: {self.last_name}\nТелефон: {self.phone}\n'
                    f'В избранных: {Contact.favorite(self)}\nДополнительная информация:\n'
                    f'\t{self.notes}\n{add_datas}\n')


class PhoneBook:

    def __init__(self, name) -> None:
        self.name = name
        self.contacts = {}

    def informashion(self) -> None:
        for contact in self.contacts:
            print(self.contacts[contact])

    def new_contact(self, first_name, last_name, phone, *args, favorite=False, **kwargs):
        self.contacts[len(self.contacts)] = Contact(first_name, last_name, phone, *args, favorite=favorite, **kwargs)
        print(f'Contact {self.contacts[len(self.contacts)-1].first_name} added successfully\n')

    def del_contact(self, phone_number):
        for contact in self.contacts:
            if self.contacts[contact].phone == phone_number:
                print('\t', self.contacts[contact].phone)
                del self.contacts[contact]
                return None
        print(f'Contact with phone number {phone_number} not found')

    def favorite_contact(self):
        for contact in self.contacts:
            if self.contacts[contact].favorite:
                print(self.contacts[contact])

    def find_contact(self, first_name, last_name):
        for contact in self.contacts:
            if self.contacts[contact].first_name == first_name and self.contacts[contact].last_name == last_name:
                print(self.contacts[contact])
                return None
        print(f'Contact {first_name} {last_name} not found')