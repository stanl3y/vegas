# Vegas: notes

#### Custom (naive) hash function
```
import sys

num_list = map(lambda x: str(ord(x)), self.name)
num = int("".join(num_list))
return num % sys.hash_info.modulus
```

#### Use version control on .pyc files?
No, these are compiled versions of the source code, so there is no need. Add `*.pyc` to `.gitignore`.

#### Test constructor that just saves parameters?
Yes, only takes a moment, and prevents regression issues.
