from DataStructures.List import array_list as arr
def new_queue():
    return arr.new_list()

def enqueue(my_queue,element):
    if is_empty(my_queue):
        arr.add_first(my_queue,element)
    else:
        arr.add_last(my_queue,element)
    return my_queue

def is_empty(my_queue):
    return arr.is_empty(my_queue)

def size(my_queue):
    return arr.size(my_queue)

def dequeue(my_queue):
    dev = arr.get_element(my_queue,0)
    arr.remove_last(my_queue)
    return dev

def peek(my_queue):
    if not is_empty(my_queue):
        return my_queue['elements'][0]
    else:
        raise Exception('EmptyStructureError: queue is empty')
