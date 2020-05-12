import proto_first_pb2
from google.protobuf import text_format


def file_series(filename):
    address_book = proto_first_pb2.AddressBook()
    person = address_book.people.add()

    person.id = 1
    person.name = "safly"
    person.email = "safly@qq.com"
    person.money = 1000.11
    person.work_status = True

    phone_number = person.phones.add()
    phone_number.number = "123456"
    phone_number.type = proto_first_pb2.MOBILE

    maps = person.maps
    maps.mapfield[1] = 1
    maps.mapfield[2] = 2

    with open(filename, 'w') as f:
        f.write(str(address_book))

def read_proto(new_filename):
    address_book = proto_first_pb2.AddressBook()
    # print(address_book)
    f = open(new_filename, "rb")
    text_format.Parse(f.read(),address_book)
    # address_book.ParseFromString(f.read)
    f.close()
    
    for person in address_book.people:
        print("p_id{},p_name{},p_email{},p_money{},p_workstatu{}".format(person.id,person.name,     person.email,person.money,person.work_status))

    for phone_number in person.phones:
        print(phone_number.number,phone_number.type)


    for key in person.maps.mapfield:
        print(key,person.maps.mapfield[key])
#序列化
# serializeToString = address_book.SerializeToString()
# print(serializeToString,type(serializeToString))

# address_book.ParseFromString(serializeToString)


if __name__ == "__main__":
    filename ="./person.pb"
    # file_series(filename)
    read_proto(filename)


