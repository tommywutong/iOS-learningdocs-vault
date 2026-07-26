---
title: 'Friday Q&A 2014-03-14: Introduction to the Sockets API'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2014-03-14-introduction-to-the-sockets-api.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:293ec1fa6957bcc4'
translated: false
---

> 原文：[Friday Q&A 2014-03-14: Introduction to the Sockets API](https://www.mikeash.com/pyblog/friday-qa-2014-03-14-introduction-to-the-sockets-api.html)　·　mikeash.com Friday Q&A

Posted at 2014-03-14 13:52 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2014-05-09: When an Autorelease Isn't](https://www.mikeash.com/pyblog/friday-qa-2014-05-09-when-an-autorelease-isnt.html)  
Previous article: [Tales From The Crash Mines: Issue #1](https://www.mikeash.com/pyblog/tales-from-the-crash-mines-issue-1.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [networking](https://www.mikeash.com/pyblog/?tag=networking) [sockets](https://www.mikeash.com/pyblog/?tag=sockets)

Friday Q&A 2014-03-14: Introduction to the Sockets API

by [Mike Ash](https://www.mikeash.com/)

**Sockets**  
A _socket_, as far as this API is concerned, is a kind of UNIX file descriptor. That is to say, it's a (generally small) `int` that corresponds to a kernel structure. Like any file descriptor, you can `read` and `write` with it, but sockets also allow other operations.

To create a socket, call the `socket` function. It takes three arguments. The first argument is the domain of the socket, which is basically which IP-level protocol the socket will use. Common values for this parameter are `AF_INET`, which specifies IPv4, and `AF_INET6`, which specified IPv6. The second argument is the type of the socket, which essentially allows you to choose TCP or UDP. Pass `SOCK_STREAM` for TCP, and `SOCK_DGRAM` for UDP. The third parameter is more or less vestigial for normal uses these days, and you can just pass zero. Here's a line of code that creates a socket:

```
    int s = socket(AF_INET6, SOCK_STREAM, 0)
```

As is traditional, I will be mostly omitting error checking from my examples in this article. Don't omit it in your code.

This newly-created socket is not very useful on its own. It doesn't actually go anywhere, so you can't read or write. Using it requires more specialized calls. Those calls require _addresses_.

**Addresses**  
Addresses are represented with a family of `struct`s which are organized in a way that resembles object-oriented inheritance, if it was badly implemented in C.

The "base class" is `struct sockaddr`, which contains the address family (essentially, what kind of address this is) plus raw address data and the overall length:

```
    struct sockaddr {
        __uint8_t   sa_len;     /* total length */
        sa_family_t sa_family;  /* [XSI] address family */
        char        sa_data[14];    /* [XSI] addr value (actually larger) */
    };
```

Being only sixteen bytes long, this really doesn't have enough space for all uses, especially considering IPv6. This is not a problem when casting pointers to pass around, but it's troublesome when declaring a local `struct sockaddr` to _receive_ an address from a function. To remedy this problem, there's a newer (as in, only 15 or so years old) "base class" struct with more storage called, appropriately, `struct sockaddr_storage`:

```
    struct sockaddr_storage {
        __uint8_t   ss_len;     /* address length */
        sa_family_t ss_family;  /* [XSI] address family */
        char            __ss_pad1[_SS_PAD1SIZE];
        __int64_t   __ss_align; /* force structure storage alignment */
        char            __ss_pad2[_SS_PAD2SIZE];
    };
```

It's the same concept as `struct sockaddr`, just longer. It also has some fun business in the middle to ensure that the whole thing gets nicely aligned, but you can ignore that.

Individual address families then have individual "subclasses", which are compatible with the above layouts so you can cast pointers between the different types. For IPv4 addresses, the corresponding address type is `struct sockaddr_in`:

```
    struct sockaddr_in {
        __uint8_t   sin_len;
        sa_family_t sin_family;
        in_port_t   sin_port;
        struct  in_addr sin_addr;
        char        sin_zero[8];
    };
```

The `sin_port` field is the TCP or UDP port of the address, and `sin_addr` is the actual four-byte IPv4 address. Together, those make up a full IPv4 "address".

IPv6 is similar, but longer:

```
    struct sockaddr_in6 {
        __uint8_t   sin6_len;   /* length of this struct(sa_family_t) */
        sa_family_t sin6_family;    /* AF_INET6 (sa_family_t) */
        in_port_t   sin6_port;  /* Transport layer port # (in_port_t) */
        __uint32_t  sin6_flowinfo;  /* IP6 flow information */
        struct in6_addr sin6_addr;  /* IP6 address */
        __uint32_t  sin6_scope_id;  /* scope zone index */
    };
```

The `sin6_port` field serves the same purpose as the `sin_port` field above, and the `sin6_addr` field is the 16-byte IPv6 address. The `sin6_flowinfo` and `sin6_scope_id` fields are specialized fields you generally don't need to pay much attention to, and we'll skip over those.

**Listening For Connections**  
Let's look at how to listen for incoming TCP connections. After creating the socket, you must then bind it to an IP address. This can be a specific IP address belonging to the computer you're on, or it can just be a special address meaning "listen on everything" which is usually what you want.

To bind to an address, you need a socket address. In this case, we'll use a `struct sockaddr_in6` and create an IPv6 socket. This has the bonus of also accepting IPv4 connections, so one piece of code can accept both IPv4 and IPv6. We'll start off with the basic length and family information:

```
    struct sockaddr_in6 addr = {
        .sin6_len = sizeof(addr),
        .sin6_family = AF_INET6,
```

We'll hardcode the port number. Note that port numbers in socket address structs are always in _network byte order_, which is to say big-endian, so you need to use a byte-swapping function when putting a value in or getting a value out. The most natural functions to use here are the POSIX-level `htons` and friends, but any byte swapping function will do the job. Here we'll listen on port `12345`:

```
        .sin6_port = htons(12345),
```

Finally, we need to specify that this is the special "any" address by using the constant `in6addr_any` for the address field:

```
        .sin6_addr = in6addr_any
    };
```

Let's not forget to actually create the socket:

```
    int s = socket(AF_INET6, SOCK_STREAM, 0);
```

Now we're ready to bind it to the address. The call for this is named, naturally, `bind`. The `bind` function takes three parameters: the socket to operate on, the address to bind to, and the length of that address. Here's the call:

```
    bind(s, (void *)&addr, sizeof(addr));
```

The second parameter is cast to `void *` because the function takes a `struct sockaddr *` but `addr` is a `struct sockaddr_in6`. Such is the peril of trying to provide a family of multiple semi-compatible `struct`s.

You might be wondering why there's a length parameter, when the address itself also contains a length field. The POSIX standard doesn't actually require the length field, so some systems offer it and others don't. This means that any cross-platform code or interfaces (like the POSIX APIs themselves) can't assume the existence of the length field, and must pass it around separately.

With the socket bound, the next step is to tell the system to listen on it. This is done with, you guessed it, the `listen` function. It takes two parameters: the socket to operate on, and the desired length of the queue used for listening. This queue length tells the system how many incoming connections you want it to sit on while trying to hand those connections off to your program. Unless you have a good reason to use something else, passing the `SOMAXCONN` gives you a safe, large value. Here's the call:

```
    listen(s, SOMAXCONN);
```

The socket is now in the listening state and you can attempt to connect to it on port `12345`. The program must now accept incoming connections, which is done with the `accept` function. This function takes three parameters: the socket to operate on, a place to store the address of the incoming connection, and the length of that storage. This allows you to find out where incoming connections are coming from, but they're not strictly necessary, so we'll leave them as `NULL`. The function returns a socket for the incoming connection:

```
    int conn = accept(s, NULL, NULL);
```

You can then read data from this new socket:

```
    int count = read(conn, buf, sizeof(buf));
    printf("%.*s\n", count, buf);
```

When reading and writing data to a socket, you _must_ write your code to accept reading or writing less data than requested. The `read` and `write` function calls return the number of bytes actually read or written. You can get away with ignoring this value in a lot of situations, but not so with socket programming. The amount of data read or written will frequently be less than what you requested when dealing with sockets, so you must write the code to buffer the data and loop in order to make multiple calls. For example, to write the above data back out, you'd want a loop like this:

```
    int writeCursor = 0;
    int writeCount;
    do {
        writeCount = write(conn, buf + writeCursor, count - writeCursor);
        writeCursor += writeCount;
    } while(writeCursor < count);
```

Really, this is not quite correct. I'm trying to skip over error handling, but there is one error case that can't be ignored here. It is possible for a `read` or `write` call to return an `EINTR` error, which is a transient error that indicates that the system call was interrupted somehow. It doesn't indicate a failure, but rather just requires that you try the call again. Here's corrected code for that:

```
    int writeCursor = 0;
    int writeCount;
    do {
        writeCount = write(conn, buf + writeCursor, count - writeCursor);
        if(writeCount < 0) {
            if(errno != EINTR) {
                perror(write);
                break;
            }
        } else {
            writeCursor += writeCount;
        }
    } while(writeCursor < count);
```

When you're done with the socket, just `close` it:

```
    close(conn);
```

If you want finer-grained control, you can use the `shutdown` function instead. This allows closing only one direction of the socket, which can be useful for certain protocols.

**Making Connections**  
To make a connection, you first need an address to connect to. There are about sixteen billion different ways to obtain an address, from hardcoding it to writing code to parse IP addresses to asking the system to translate a human-readable string into a connectable address.

Fortunately for us, the APIs for getting the system to do the work for us are relatively easy to use. The modern call is `getaddrinfo`. It's a capable API with a lot of options, but basic usage is straightforward.

First, we need a hostname. You'd probably get this from a UI or something, but in this case we'll just hardcode it:

```
    const char *name = "mikeash.com";
```

We also need a port number. We could smash this into the address `struct` ourselves later, but it's easier to hand it to `getaddrinfo` and let it worry about that part:

```
    int port = 80;
```

`getaddrinfo` actually wants the port number to be in the form of a string. This makes it really convenient if your port number originates as a string, but in this case it means we need to do a small amount of extra work. I'll transform this integer port into a string using `asprintf`:

```
    char *portString;
    asprintf(&portString, "%d", port);
```

`getaddrinfo` takes a set of "hints", which allow control over what kind of results it will provide. There are many options, but the only one we care about here is the socket protocol. The call can provide results with different socket protocols, such as TCP or UDP, and we want to ensure we only look for TCP. If we don't do that, the call will return two results for each address it finds, one for each protocol. To specify TCP, we just specify `IPPROTO_TCP` in the `ai_protocol` field:

```
    struct addrinfo hints = {
        .ai_protocol = IPPROTO_TCP
    };
```

Everything is now ready to make the call to `getaddrinfo`:

```
    struct addrinfo *info;
    getaddrinfo(name, portString, &hints, &info);
```

One hostname can potentially have many addresses. The `struct addrinfo` returned from `getaddrinfo` is actually a linked list, which can be walked in order to enumerate all of the results:

```
    for(struct addrinfo *cursor = info; cursor; cursor = cursor->ai_next) {
```

Let's go ahead and print them all out. `struct addrinfo` contains an `ai_addr` field which points to a `struct sockaddr`. We can convert this into a human-readable string using `getnameinfo` like so:

```
        char addrStr[NI_MAXHOST];
        getnameinfo(cursor->ai_addr,
                    cursor->ai_addrlen,
                    addrStr,
                    sizeof(addrStr),
                    NULL,
                    0,
                    NI_NUMERICHOST));
```

We'll print it out along with some of the other pertinent fields:

```
        printf("flags=%x family=%d type=%d protocol=%d address=%s\n",
               cursor->ai_flags,
               cursor->ai_family,
               cursor->ai_socktype,
               cursor->ai_protocol,
               addrStr);
    }
```

For `google.com` this produces a nice list of addresses:

```
    flags=0 family=2 type=1 protocol=6 address=74.125.228.228
    flags=0 family=2 type=1 protocol=6 address=74.125.228.224
    flags=0 family=2 type=1 protocol=6 address=74.125.228.232
    flags=0 family=2 type=1 protocol=6 address=74.125.228.227
    flags=0 family=2 type=1 protocol=6 address=74.125.228.230
    flags=0 family=2 type=1 protocol=6 address=74.125.228.233
    flags=0 family=2 type=1 protocol=6 address=74.125.228.231
    flags=0 family=2 type=1 protocol=6 address=74.125.228.229
    flags=0 family=2 type=1 protocol=6 address=74.125.228.238
    flags=0 family=2 type=1 protocol=6 address=74.125.228.226
    flags=0 family=2 type=1 protocol=6 address=74.125.228.225
    flags=0 family=30 type=1 protocol=6 address=2607:f8b0:4004:803::1009
```

We're ready to create a socket now. We'll just grab the first value in the list for this part. In real code, you'd want to iterate over the list and try additional entries if one failed, and possibly try multiple entries simultaneously for better speed. The `ai_family`, `ai_socktype`, and `ai_protocol` fields provide everything we need to create the socket:

```
    int s = socket(info->ai_family, info->ai_socktype, info->ai_protocol);
```

Now we need to make it connect to the address. This is done with the aptly-named `connect` function, which takes the socket, the destination address, and its length:

```
    connect(s, info->ai_addr, info->ai_addrlen);
```

Upon successful completion of this call, we have a connected socket to the target address. We can now read and write using this socket. Before we do that, since we're all done with the address data at this point, we'll go ahead and free it:

```
    freeaddrinfo(info);
```

Let's not forget the port string:

```
    free(portString);
```

Since we're connecting to port 80, we can write an HTTP request to this socket:

```
    const char *toWrite = "GET /\r\n\r\n";
```

Since sockets are file descriptors, `write` works fine on them. As always, be sure to use a loop:

```
    while(*toWrite) {
        int written = write(s, toWrite, strlen(toWrite));
        if(writeCount < 0) {
            if(errno != EINTR) {
                perror(write);
                break;
            }
        } else {
            toWrite += written;
        }
    }
```

Now we can read the response, also using a loop:

```
    char buf[1024];
    int count;
    do {
        count = read(s, buf, sizeof(buf))) > 0);
        if(count < 0) {
            if(errno != EINTR) {
                perror("read");
                break;
            }
        } else {
            printf("%.*s", count, buf);
        }
    } while(count > 0);
```

When `read` returns `0`, that indicates that the server has closed the connection and we can then close our end of things:

```
    close(s);
```

**Conclusion**  
The POSIX sockets API is a bit old and crusty, but it's ultimately not too bad. You should use higher-level APIs whenever it's reasonable, but it's good to understand what the low-level API does and how to use it even if you don't actually use it too often.

That's it for today. Come back next time for more amusing adventures. Friday Q&A is driven by reader suggestions, so if you have a suggestion for a topic to cover in the meantime, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2014-03-14-introduction-to-the-sockets-api.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
