import queue

# Create a FIFO queue
q = queue.Queue()

# Add items to the queue
q.put(1)
q.put(2)
q.put(3)

print()

# Remove and return items from the queue
print(q.get())  # Outputs: 1
print(q.get())  # Outputs: 2
print(q.get())  # Outputs: 3

# Check if the queue is empty
print(q.empty())  # Outputs: True

