import bangir_pb2
from google.protobuf import text_format


def file_series(filename):
    node_def = bangir_pb2.FusedNode()
    node = node_def.node.add()

    node.name = "convolution_first"
    node.op = "conv"
    node.op_index = 1
    node.data_type = bangir_pb2.FLOAT16
    node.input.extend(["1", "2","3"])
    ints_list = bangir_pb2.ListOfInteger()
    ints_list.ints.extend([1,2,3,4])
    node.input_datashape.extend([ints_list])
    node.input_datashape.extend([ints_list])
    node.input_datashape.extend([ints_list])
    # node.listOfinteger.append(app)
    # convparam = bangir_pb2.ConvParam()
    node.dataparam.layout = bangir_pb2.NHWC
    node.convparam.kernel_size.extend([3,3])
    node.convparam.pad.extend([0,0])
    node.convparam.stride.extend([1,1])
    node.convparam.dilation.extend([1,1])
    node.convparam.bias = True
    node.convparam.relu = True

    with open(filename, 'w') as f:
        f.write(str(node_def))

def read_proto(new_filename):
    node_def = bangir_pb2.FusedNode()
    # print(address_book)
    f = open(new_filename, "rb")
    text_format.Parse(f.read(),node_def)
    # address_book.ParseFromString(f.read)
    f.close()
    
    for node in node_def.node:
        print("p_op = {},p_name = {},p_index = {},p_data_type = {}".format(node.op,node.name,node.op_index,node.data_type))

    # for phone_number in person.phones:
    #     print(phone_number.number,phone_number.type)


    # for key in person.maps.mapfield:
    #     print(key,person.maps.mapfield[key])
#序列化
# serializeToString = address_book.SerializeToString()
# print(serializeToString,type(serializeToString))

# address_book.ParseFromString(serializeToString)


if __name__ == "__main__":
    filename ="./bangir.pbtxt"
    file_series(filename)
    # read_proto(filename)



