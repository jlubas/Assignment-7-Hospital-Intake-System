class Patient:
    
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency




class MinHeap:
    
    def __init__(self):
        self.data = []
    

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2

            if self.data[index].urgency < self.data[parent_index].urgency:
                temp = self.data[index]
                self.data[index] = self.data[parent_index]
                self.data[parent_index] = temp

                index = parent_index
            else:
                break

    
    def heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(self.data) and self.data[left].urgency < self.data[smallest].urgency:
            smallest = left

        if right < len(self.data) and self.data[right].urgency < self.data[smallest].urgency:
            smallest = right

        if smallest != index:
            temp = self.data[index]
            self.data[index] = self.data[smallest]
            self.data[smallest] = temp

            self.heapify_down(smallest)
     
    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")

    def peek(self):
        if not self.data:
            return None
        return self.data[0]

    def remove_min(self):
        if not self.data:
            return None

        if len(self.data) == 1:
            return self.data.pop()

        min_patient = self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)

        return min_patient
       






# Test your MinHeap class here including edge cases


p1 = Patient("Riley", 2)
print(p1.name)
print(p1.urgency)


heap = MinHeap()
print(heap.data)


heap = MinHeap()

heap.insert(Patient("Jordan", 3))
heap.insert(Patient("Taylor", 1))
heap.insert(Patient("Avery", 5))

heap.print_heap()


next_up = heap.peek()
print(next_up.name, next_up.urgency)

served = heap.remove_min()
print(served.name)

heap.print_heap()

# Test edge cases for MinHeap

# Test an empty heap
empty_heap = MinHeap()
print(empty_heap.peek())
print(empty_heap.remove_min())

# Test a heap with only one patient
single_heap = MinHeap()
single_heap.insert(Patient("Riley", 2))
print(single_heap.remove_min().name)
print(single_heap.peek())
# Test heapify_down with multiple patients
test_heap = MinHeap()

test_heap.insert(Patient("Alex", 1))
test_heap.insert(Patient("Blake", 3))
test_heap.insert(Patient("Casey", 2))
test_heap.insert(Patient("Drew", 7))
test_heap.insert(Patient("Evan", 4))

print("\nTest heapify_down:")
print("Removed:", test_heap.remove_min().name)
test_heap.print_heap()
