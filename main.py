import random
import string

def hashtag_generator(n):
    """
    Instagram uchun hashtaglar generatsiyasi
    """
    hashtags = []
    for _ in range(n):
        hashtag = ''
        for _ in range(random.randint(1, 10)):
            hashtag += random.choice(string.ascii_lowercase)
        hashtags.append('#' + hashtag)
    return hashtags

def main():
    n = int(input("Istalgan miqdorda hashtaglar sonini kiriting: "))
    print(hashtag_generator(n))

if __name__ == "__main__":
    main()
```

```python
import random
import string

def hashtag_generator(n):
    hashtags = []
    for _ in range(n):
        hashtag = ''
        for _ in range(random.randint(1, 10)):
            hashtag += random.choice(string.ascii_lowercase)
        hashtags.append('#' + hashtag)
    return hashtags

def main():
    n = int(input("Istalgan miqdorda hashtaglar sonini kiriting: "))
    print(hashtag_generator(n))

if __name__ == "__main__":
    main()
