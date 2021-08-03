


class Node():
    def __init__(self, data, head):
        self.data = data
        self.next = head  
        

    


        
class LinkedList():
    def __init__(self):
        self.head = None
        
    def __str__(self):
        
        if self.head is None:
            print('Linked List is empty')
            
        else:
            
            itter = self.head
            
            string = str(itter.data)
            
            while itter:
                
                
                itter = itter.next
                
                if itter is not None:
                    string = string + ' ---> '+ str(itter.data)
                
            return string
    
    def __len__(self):
        
        count = 0
        itter = self.head
        while itter:
            count += 1
            itter = itter.next
        return count
    
    
    def add_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def add_at_end(self, data):
        if self.head == None:
            self.add_at_beginning(data)
            
        else:
            
            itter = self.head
            
            
            while itter.next is not None:
                itter = itter.next
                
            
            itter.next = Node(data, None)
            
            
    def add_at_position(self, data, pos):
        
        if pos == 0:
            self.add_at_beginning(data)
        
        elif pos == -1 or pos == len(self):
            self.add_at_end(data)
        
        else:
            
            counter = 1
            
            itter = self.head
            
            while itter.next is not None:
                itter = itter.next
                counter += 1
                
                if counter == pos:
                    break
                
            node = Node(data, itter.next)
                
            
            itter.next = node
            
    
    def remove_at_position(self, pos):
        
        count = 0
        
        itter = self.head
        
        while itter is not None:
            
            
            if count == (pos -1):
                
                itter.next = itter.next.next
                break
                
            itter = itter.next
            count += 1
        
                
    def split_at_position(self, pos):
        
        if pos == 0:
            self = LinkedList()
        
        elif pos == (len(self) -1):
            pass
        
        
        else:
                
            count = 0
            
            itter = self.head
            
            while itter is not None:
                
                if count == (pos):
                    
                    break
                
                else:
                    itter = itter.next 
                    count += 1
            
            itter.next = None
    
    
    def check_values(self):
        itter = self.head
        
        uniques = set()
        
        while itter:
            uniques.add( itter.data)
            
            itter = itter.next
            
        return uniques
    
    def insert_after_value(self, data_after, data_to_insert):
        
        if data_after not in self.check_values():
            raise TypeError('{0} does not exist in the list'.format(data_after))
        
        itter = self.head
        
        while itter:
            
            if itter.data == data_after:
                node = Node(data_to_insert, itter.next)
                
            
                itter.next = node
            else:
                pass
            itter = itter.next
            
            
    def remove_by_value(self, data):
        
        if data not in self.check_values():
            raise TypeError('{0} does not exist in the list'.format(data))
        
        itter = self.head
        counter = 0
        while itter is not None:
            
            if data == (itter.data):
                self.remove_at_position(counter)   
                
            counter += 1    
            itter = itter.next
                
        
                 
                
                    
            
        
        
        
    
if '__main__' == __name__:
    
    LL = LinkedList()
    LL.add_at_beginning(2)
    LL.add_at_beginning(4)
    LL.add_at_beginning(1)
    LL.add_at_end('end_1')
    LL.add_at_end('end_2')
    
    LL.add_at_position(555, 3)
    LL.add_at_position(111, 3)
    
    
    print('Prior removal: \t', LL)
    
    
    LL.remove_at_position(3)
    print('After removal: \t', LL)
    
    LL.split_at_position(4)
    
    print('Spliting at position 4: \t', LL
          )
    
    LL.insert_after_value(555, 'data after 555')
    LL.insert_after_value(4, 'after_data_inserted')
    
    print('LL after value insertion: \t', LL)
    
    
    for key in ['data after 555', 'after_data_inserted']:
    
        print('Removing by value "{0}"'.format(key))
        
        LL.remove_by_value(key)
        
        print('\t', LL)
        

                
                    
            
        
        