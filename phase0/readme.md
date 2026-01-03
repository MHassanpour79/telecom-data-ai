# telecom-data-ai
1- Core Unit of Design & Organization
    Normal (OOP) Programming: The fundamental unit of design is the "Object" or "Class." Code is organized around modeling real-world entities and bundling their related data (state) and the functions that operate on that data (behavior) into a single, encapsulated unit.
    Data Programming: The fundamental unit of design is the "Data" itself and its flow. Code is organized around the structure of data (e.g., records, lists, maps) and the pure functions that transform this data from one shape to another.

2- State Management & Mutability
    Normal (OOP) Programming: Objects are typically stateful and mutable. An object holds an internal state that its methods can directly modify over time. This is efficient but can lead to side effects and complexity in concurrent scenarios.
    Data Programming: Data is treated as immutable and often stateless. Functions do not change the original data. Instead, they take data as input and produce new, transformed data as output. The system's state is represented by the current collection of immutable data structures.

3- Modeling Relationships Between Entities
    Normal (OOP) Programming: Relationships are modeled through object references and hierarchies. One object directly holds a reference to another, creating a web of interconnected objects.
    Data Programming: Relationships are modeled through simple keys and values in generic data structures. Data is often kept in a more normalized, "flat" format, and relationships are established by linking data via unique identifiers (IDs).


Aspect	            Normal (OOP) Programming	                            Data Programming (DOP)
=========================================================================================================================
Core Unit	        Object/Class (encapsulates state & behavior)	          Data Structure + Pure Transform Function
State	            Mutable, Stateful Objects	                              Immutable, Often Stateless Data
Relationships	    Object References & Hierarchies	                        Keys, IDs, and Generic Collections
Primary Goal	    Model real-world behavior, encapsulation	              Efficient data transformation, simplicity, clarity
Typical Use Case	Business applications, UI frameworks, complex domains	  Data pipelines, game engines, high-performance systems, analytics



Quiz#01
=========
1-What is the difference between list and generator in terms of memory?
Answer.
    A list stores all elements in memory at once, which can consume significant memory for large datasets.
    A generator produces elements one at a time on-the-fly (lazily) using the yield keyword, keeping only the current element in memory. This makes generators memory-efficient for large or infinite sequences.
        list_nums = [x for x in range(1000000)]
        gen_nums = (x for x in range(1000000))

2-Why is dict suitable for network data?
Answer.
    1- Fast Lookups: O(1) average time complexity for accessing values by keys (e.g., looking up a device by IP address).
    2- Flexible Structure: Can represent structured network data naturally (e.g., {"ip": "192.168.1.1", "status": "active", "traffic": 500}).
    3- Easy Aggregation: Efficient grouping and counting using keys (e.g., traffic per link, devices per subnet).
    4- JSON Compatibility: Direct mapping to JSON format, the standard for network API responses and configurations.
        device = {"ip": "10.0.0.1", "mac": "00:1A:2B:3C:4D:5E", "status": "up"}

3-Explain mutable vs immutable with example.
Answer.
    Mutable objects can be changed after creation, while immutable objects cannot be modified.
        my_list = [1, 2, 3]
        my_list[0] = 99  # Allowed: list is mutable
        print(my_list)   # [99, 2, 3]

        my_tuple = (1, 2, 3)
        # my_tuple[0] = 99  # ERROR: tuple is immutable

4-If the data becomes 1 milion records, which structure becomes problematic?
Answer.
    For 1 million records, these structures could become problematic:
    1- Large lists holding all data in memory → high memory consumption.
    2- Deeply nested structures (e.g., lists of lists with many levels) → slow access and high memory overhead.
    3- Inefficient data types like storing numeric IDs as strings → unnecessary memory bloat.
    4- Structures with O(n) lookup time (e.g., searching in an unsorted list) → very slow operations.
    5- Most problematic: A list of complex objects where all 1 million records are loaded simultaneously into memory instead of using generators, databases, or streaming processing.
