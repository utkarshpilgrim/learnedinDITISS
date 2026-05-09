# Linux Internals 

Awesome question — and very important for understanding Linux internals as a future server administrator.

### What is `/dev/urandom`?

-	/dev/urandom is a built-in pseudo-random number generator provided by the Linux kernel.
-	You do not need to create it — it’s already there on every standard Linux system (including Fedora).
-	It is a special file, not a regular file you edit.

You can verify it using:
```
ls -l /dev/urandom
```
Expected output:
```
crw-rw-rw- 1 root root 1, 9 Oct 22 14:45 /dev/urandom
```
-	The c at the beginning means character device.
-	It’s used to generate randomness — commonly used in security, scripting, or password generation.

### What Does `/dev/urandom` Actually Do?

When you read from it like this:
```
cat /dev/urandom | head -c 10
```

It gives you 10 random bytes — could be anything: binary junk, special characters, etc. That’s why we usually filter it:
```
tr -dc 'a-zA-Z0-9'
```

To get readable stuff.


### Related Linux Programs That Use /dev/urandom

You don’t need to install a separate program, but these tools use /dev/urandom or provide randomness:

|Tool|	Purpose|
|----|---------|
|openssl rand|	Secure random bytes|
|uuidgen|	Generate unique identifiers|
|pwgen|	Generate passwords|
|tr + head|	Simple filtering for readable random strings|

Example:

```
openssl rand -hex 6
```

### Server Admin Perspective:
- Random numbers are critical in key generation, cryptography, and secure file names.
-	`/dev/random` is a similar file, but blocks if there’s not enough entropy. /dev/urandom is non-blocking.
