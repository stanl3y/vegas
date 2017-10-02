# Vegas: notes

#### Custom (naive) hash function
```
import sys

num_list = map(lambda x: str(ord(x)), self.name)
num = int("".join(num_list))
return num % sys.hash_info.modulus
```

    