friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

import random

# first option
random_friends = random.choice(friends)
print(random_friends)

# second option
random_index = random.randint(0, 4)
print(random_index)
