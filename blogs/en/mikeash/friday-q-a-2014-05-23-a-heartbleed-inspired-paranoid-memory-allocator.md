---
title: 'Friday Q&A 2014-05-23: A Heartbleed-Inspired Paranoid Memory Allocator'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2014-05-23-a-heartbleed-inspired-paranoid-memory-allocator.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5891cd01d0a66c02'
translated: false
---

> 原文：[Friday Q&A 2014-05-23: A Heartbleed-Inspired Paranoid Memory Allocator](https://www.mikeash.com/pyblog/friday-qa-2014-05-23-a-heartbleed-inspired-paranoid-memory-allocator.html)　·　mikeash.com Friday Q&A

Posted at 2014-05-23 13:46 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2014-06-06: Secrets of dispatch_once](https://www.mikeash.com/pyblog/friday-qa-2014-06-06-secrets-of-dispatch_once.html)  
Previous article: [Friday Q&A 2014-05-09: When an Autorelease Isn't](https://www.mikeash.com/pyblog/friday-qa-2014-05-09-when-an-autorelease-isnt.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [heartbleed](https://www.mikeash.com/pyblog/?tag=heartbleed) [memory](https://www.mikeash.com/pyblog/?tag=memory)

Friday Q&A 2014-05-23: A Heartbleed-Inspired Paranoid Memory Allocator

by [Mike Ash](https://www.mikeash.com/)

**Background**  
The Heartbleed bug involves a heartbeat message added to the TLS protocol used for secure HTTP connections and many other encrypted internet protocols. The message is a simple ping, where one side can ask, "Are you still there?" and the other side will respond with, "Yes." As with many pings, the requester can include a payload which the other side will repeat back to it. The payload consists of a string of bytes prefixed with a 16-bit length to indicate how many bytes are in the payload.

The Heartbleed bug is fundamentally due to mishandling the length prefix. It's possible for the requester to send a request with a large value in the length field but with a shorter payload. The proper response to this would be to treat it as a fatal error and terminate the connection.

OpenSSL failed to check, and so proceeded with the response in this case. It copied the payload from the request to the response, using the length field to determine how many bytes to copy. If the actual payload is shorter than what the length field says, it ended up copying whatever data was sitting beyond the incoming packet data.

OpenSSL uses an internal allocator for this and other tasks, and that allocator doesn't zero memory when it's allocated or freed. Thus, the extra data that's copied into the response ends up being whatever arbitrary data happened to be stored there from the last allocation at that spot. Since that same allocator is used for things like private key storage, that data can end up being sent back to the requester.

To scoop up as much data as possible, the attacker can specify the a long length field with no payload. A vulnerable TLS implementation will then reply with kilobytes of data from its internal memory. Depending on luck, the attacker stands a good chance of getting something interesting in that dump. If there's no interesting data, the attacker can just try again. The process is quick and can be repeated without limit.

**A Paranoid Allocator**  
The proper fix for Heartbleed is to validate the length against the provided payload before sending a reply. There are various ways to try to avoid this whole class of security vulnerabilities.

One way is to have better processes for developing security-critical software. There was no particularly good reason to add the heartbeat extension to TLS in the first place, or to implement it in OpenSSL, so the whole thing should have been stopped before it even got started.

Another way is to use static analysis tools that are able to detect when too much trust is placed in input data. Unfortunately, the Heartbleed bug was too subtle for most static analyzers to detect, and while it's prompted a lot of work in that area, it's hard to know how much of that work will help to detect similar bugs in the future, and how much of it really just helps them detect Heartbleed specifically.

Finally, another way to avoid these vulnerabilities is to program in a safer language than C. C can be enormously unforgiving, and its concept of [undefined behavior](http://www.catb.org/jargon/html/N/nasal-demons.html) means that mistakes can easily turn into security vulnerabilities. The use of a safer language has been suggested for ages, but security-critical code keeps being written in C despite the problems.

Interestingly, I'm not too sure if a better language would have prevented this particular bug. It would be relatively natural to recycle buffers even in a language with more guarantees, and that could end up recycling the contents as well. If the buffer isn't truncated to the actual length of each incoming packet, bounds checking won't catch the excessively large copy. That said, better languages will shut out whole classes of security vulnerabilities and it would probably be wise to start seriously looking at alternatives to C.

In theory, the above should be enough. In practice, it's a good idea to take a layered approach to security and not only try to avoid vulnerabilities, but also try to mitigate them if and when they do occur. For example, OS X and most other operating systems will mark memory as being non-executable by default. This means that even if an attacker is able to write out machine code into your process's memory and jump to it, the attempt to take control will fail unless the attacker can first arrange for that code to be marked as executable.

Given that, I thought about what measures could be taken when allocating memory for sensitive data, such as private keys, that could help keep it safe even after a vulnerability is exploited. I came up with these features:

1. Memory should be zeroed when allocated, and again when freed.
2. Guard pages with no read or write permission should be placed before and after the memory allocation so that any overflow from an adjacent allocation turns into a crash.
3. The memory used for storage should be kept with minimal permissions. It should be unreadable or unwriteable by default. When a read is requested, it should be changed to read-only, and when a write is requested, it should be changed to read-write.
4. The API should be designed such that it's difficult to leave read or write permissions enabled for longer than necessary, and especially to accidentally leave them enabled permanently.

**Code**  
The code is available on GitHub as usual:

[https://github.com/mikeash/MAParanoidAllocator](https://github.com/mikeash/MAParanoidAllocator)

**API**  
This is the public-facing API for the class:

```
    @interface MAParanoidAllocator : NSObject

    - (id)init;
    - (id)initWithSize: (size_t)size;

    - (size_t)size;
    - (void)setSize: (size_t)size;

    - (void)read: (void (^)(const void *ptr))block;
    - (void)write: (void (^)(void *ptr))block;

    @end
```

Most of it is obvious, but `read:` and `write:` need some explaining.

Conceptually, this class is similar to `NSMutableData`. It's an object wrapper around an arbitrary chunk of bytes. The `NSMutableData` API provides the `bytes` method for reading, and the `mutableBytes` method for reading and writing. However, these methods make it impossible for the data object to know when the caller is done reading or writing. It would be possible to add a method that's called at the end to explicitly signal that the operation is done, so that calling code would look like:

```
    const void *ptr = [dataObject bytes];
    // ...use ptr here...
    [dataObject recycleBytes: ptr];
```

However, it would be too easy to forget the `recycleBytes:` call and thus leave the memory readable forever.

The `read:` and `write:` methods each take a block as a parameter. The block is called synchronously and is passed in a pointer to the memory held by the object. This pointer is only valid inside the block, and the permissions are automatically reset to make the memory unreadable and unwriteable as soon as the block returns.

**Implementation Strategy**  
The usual memory allocation APIs like `malloc` and `free` won't suffice for this class.

Instead, it will allocate memory using `mmap`. This allows it to use `mprotect` to change permissions on the memory. Both `mmap` and `mprotect` work with page granularity, meaning that the class has to allocate memory in 4kB chunks. When allocating memory, it will round the requested size up to the nearest multiple of 4kB. It will add two more 4kB pages to the size, one for a guard page before and after. The guard pages will be permantly marked as unreadable and unwriteable. The allocated memory in the middle will normally be marked as unreadable and unwriteable, but the permissions will be temporarily changed using `mprotect` when necessary.

To resize an existing allocation, the approach is nothing special: allocate new memory, copy the contents across, deallocate the old memory. Since the memory is allocated with `mmap`, it's deallocated with `munmap`, and for the sake of paranoia, the code will zero out the allocated memory before returning it to the operating system.

**Instance Variables**  
The class needs three instance variables: the current allocation size, a pointer to the allocated memory, and the system's page size. The page size could be a global variable, but it's mildly more convenient to keep it as an instance variable:

```
    @implementation MAParanoidAllocator {
        size_t _size;
        char *_memory;
        size_t _pageSize;
    }
```

**Error Checking**  
This code doesn't try too hard to report or recover from errors. The calls generally shouldn't fail, and if they do, something has gone terribly wrong. If they fail, the code just logs the error and then calls `abort()`. Error checking is essential in all code, but it's especially true for security-critical code, as unchecked errors can easily turn into exploitable vulnerabilities. (See for example [Exploitable Userland NULL Pointer Dereference](http://tk-blog.blogspot.com/2009/01/exploitable-userland-null-pointer.html).)

I wrote a simple error checking macro that's little more than a custom `assert`:

```
    #define CHECK(condition) do { \
            if(!(condition)) { \
                NSLog(@"%s: %s (%d)", #condition, strerror(errno), errno); \
                abort(); \
            } \
        } while(0)
```

In addition to logging the failed condition and calling `abort()`, it also prints out the value of `errno` to help indicate what went wrong.

**Initialization and Deallocation**  
The `init` method calls `super`, then sets the page size variable:

```
    - (id)init {
        if((self = [super init])) {
            CHECK((_pageSize = sysconf(_SC_PAGESIZE)) > 0);
        }
        return self;
    }
```

The other variables are left as zero, indicating that a freshly initialized instance has a size of zero. The class will be built so that a size of zero means no memory is allocated and no resources need to be freed. This means that making the first allocation can be done by just calling `setSize:` with the desired size, and that cleaning up in `dealloc` can be done by setting the size back to zero.

The `initWithSize:` method therefore just calls `init`, then `setSize:`

```
    - (id)initWithSize: (size_t)size {
        self = [self init];
        [self setSize: size];
        return self;
    }
```

The `dealloc` method again just calls `setSize:`

```
    - (void)dealloc {
        [self setSize: 0];
    }
```

**Page Size Rounding**  
The API promises byte granularity, but all of the calls behind the scenes have to work with entire pages. This isn't a problem, but it does require rounding the requested sizes up to the nearest multiple of the page size. This simple method takes care of that:

```
    - (size_t)roundToPageSize: (size_t)size {
        size_t pageCount = (size + _pageSize - 1) / _pageSize;
        return pageCount * _pageSize;
    }
```

**Changing Memory Permissions**  
Several places in the code need to call `mprotect` on the entire chunk of allocated memory. This entails rounding the allocation size up to the nearest page size, calling `mprotect`, and checking for errors. That process is wrapped in a small helper method:

```
    - (void)mprotect: (int)prot {
        size_t size = [self roundToPageSize: _size];
        if(size > 0) {
            CHECK(mprotect(_memory, size, prot) == 0);
        }
    }
```

**Setting the Size**  
Most of the complexity of this class is in `setSize:`. That's where memory is allocated, deallocated, and copied from an old allocation to a new one.

The first thing it does is round both new and old sizes to multiples of the page size:

```
    - (void)setSize: (size_t)newSize {
        size_t beforeSize = [self roundToPageSize: _size];
        size_t afterSize = [self roundToPageSize: newSize];
```

These values get used a lot, so it's easiest to compute them once up front. Next, check if they're actually different. If the rounded sizes are equal, no memory needs to be reallocated:

```
        if(beforeSize != afterSize) {
```

If they are different, then the next task is to allocate a new chunk of memory with the new size. Since size zero is handled by having no memory allocated at all, this is only done if the new size is not zero:

```
            char *afterPointer = NULL;
            if(afterSize > 0) {
```

The total amount of memory to allocate is the new size plus two additional guard pages:

```
                size_t guardPagesSize = _pageSize * 2;
                size_t toAllocate = afterSize + guardPagesSize;
```

Then it's time to call `mmap`. It requests an anonymous, private mapping (in other words, it's not trying to memory map a file or anything like that) with read and write permissions. It needs to copy the existing data into the new allocation, so making the new memory unreadable and unwriteable comes later.

```
                char *allocatedPointer;
                CHECK((allocatedPointer = mmap(NULL, toAllocate, PROT_READ | PROT_WRITE, MAP_ANON | MAP_PRIVATE, 0, 0)) != MAP_FAILED);
```

The pointer returned by `mmap` points to the leading guard page. The pointer to the memory that's actually used to store data is one page beyond that:

```
                afterPointer = allocatedPointer + _pageSize;
```

The memory returned from `mmap` is already zeroed by the operating system, so it's not necessary to explicitly clear it in code.

With the new allocation in place, the leading and trailing pages are set to be unreadable and unwriteable so that they act as guard pages:

```
                CHECK(mprotect(allocatedPointer, _pageSize, PROT_NONE) == 0);
                CHECK(mprotect(afterPointer + afterSize, _pageSize, PROT_NONE) == 0);
            }
```

If there's an existing allocation and a new allocation, then the data needs to be copied across. The new allocation is currently writeable, but the existing allocation is completely inaccessible. Thus, the copy is done inside of a call to the `read:` method:

```
            if(beforeSize > 0 && afterSize > 0) {
                [self read: ^(const void *ptr) {
                    memcpy(afterPointer, ptr, MIN(beforeSize, afterSize));
                }];
            }
```

At this point, the new memory is allocated (if necessary) and the existing data (if any) has been copied into it. The next step is to deallocate the old memory, if there is any:

```
            if(beforeSize > 0) {
```

Before returning it to the operating system, zero it out:

```
                [self write: ^(void *ptr) {
                    memset(ptr, 0, beforeSize);
                }];
```

This is probably unnecessary. The `munmap` documentation doesn't guarantee that memory is zeroed out, but it should be safe since the only way to get the memory back again is with a call to `mmap`, and `mmap` zeroes all memory before providing it to the caller. However, this is a class with "paranoid" in its name, and that guarantee is a little too indirect for my comfort.

(Aside: there's a common problem in code like this where the `memset` call gets optimized away by the compiler. Compilers are intelligent enough to know that writing to a buffer that is then immediately passed to `free()` is pointless, and the write can be eliminated. While this is correct according to the language standard, it's undesirable behavior for paranoid, security-conscious code like this. To work around that problem, the `memset_s` function was introduced in the C11 standard. It does the same thing as `memset`, but is guaranteed not to be optimized away. It's available on Apple platforms starting with Mac OS X 10.9 and iOS 7. Fortunately, `memset_s` is unnecessary here, as the indirection of calling `memset` in a block, and the fact that the memory is freed using `munmap` rather than `free`, mean that it can't be optimized away. Using plain `memset` here allows the code to be compatible with earlier OS releases.)

Now that the memory is zeroed, it has to calculate the total size of the original allocation, and the pointer to the beginning of the allocation, taking into account the leading and trailing guard pages:

```
                size_t guardPagesSize = _pageSize * 2;
                size_t toDeallocate = beforeSize + guardPagesSize;
                char *pointerWithGuards = _memory - _pageSize;
```

Then a call to `munmap` deallocates the memory.

```
                CHECK(munmap(pointerWithGuards, toDeallocate) == 0);
            }
```

With the new memory allocated and the old memory deallocated, it's time to update the instance variables:

```
            _memory = afterPointer;
            _size = newSize;
```

Finally, the newly allocated memory can be made unreadable and unwriteable.:

```
            [self mprotect: PROT_NONE];
```

In the case where the two allocations are the same (rounded) size, not much needs to be done. In addition to updating the `_size` instance variable, it also zeroes out any extra memory beyond the end of the new size in the case where the size shrinks. This ensures that leftover, potentially sensitive data doesn't remain after the caller expected it to be gone:

```
        } else {
            if (newSize < _size) {
                [self write:^(void *ptr) {
                    memset((char *)ptr + newSize, 0, _size - newSize);
                }];
            }
            _size = newSize;
        }
    }
```

**Size Getter**  
Compared to `setSize:`, the implementation of the `size` method is somewhat less exciting:

```
    - (size_t)size {
        return _size;
    }
```

**Reading and Writing**  
Let's look at the implementation of `read:` and `write:`. Both methods follow the same basic pattern: `mprotect` the allocation to have some permissions, call a block, then `mprotect` the allocation again to make it inaccessible. This pattern can be wrapped up in a common method:

```
    - (void)withProtections: (int)prot call: (void (^)(void))block {
        [self mprotect: prot];
        block();
        [self mprotect: PROT_NONE];
    }
```

With that available, the `read:` method just calls `withProtections:call:` with `PROT_READ`:

```
    - (void)read: (void (^)(const void *))block {
        [self withProtections: PROT_READ call: ^{
            block(_memory);
        }];
    }
```

The `write:` method is nearly identical, just with `PROT_READ | PROT_WRITE`:

```
    - (void)write: (void (^)(void *))block {
        [self withProtections: PROT_READ | PROT_WRITE call: ^{
            block(_memory);
        }];
    }
```

**Tests**  
I wanted to be sure to test all of the features of this code. A lot of those features involve ensuring that code crashes when it tries to access stuff outside of the provided API. My first approach was to write code that would crash, then use something like [PLCrashReporter](https://www.plcrashreporter.org/) to catch the crash and resume execution. Unfortunately, this doesn't play well with the debugger, as `lldb` strongly insists on stopping execution when the program crashes even if the crash was going to be caught. Since debugging tests is really useful, I didn't want to settle for that approach.

After a lot of pain and suffering trying to get a custom mach exception handler set up, I realized that I could use mach calls like `mach_vm_read` and `mach_vm_write` to perform illegal memory reads and writes without crashing. These calls allow reading and writing memory, but when the given address is inaccessible, they return an error instead of raising a signal. This simplified the test code a lot. I won't get into details here, but if you're interested, you can [read through the test code on GitHub](https://github.com/mikeash/MAParanoidAllocator/blob/master/MAParanoidAllocator%20Tests/MAParanoidAllocator_Tests.m#L44).

**Conclusion**  
This code defends against a scenario that should never happen, and where you've effectively already lost the game. Bugs which allow an attacker to bump into the various protections used here shouldn't happen in the first place. However, since bugs are inevitable, a layered approach to security can help mitigate their effects. I'm not sure if it's truly useful in this case, but it's an interesting exercise to work through, and it doesn't seem unreasonable to make sensitive data unreadable when it's not explicitly being used. The techniques used to do that are all fairly straightforward POSIX calls, albeit ones that don't see a lot of use in normal code.

That's it for today. Come back next time for more frightening adventures. Friday Q&A is driven by reader ideas, so as always, if you have an idea for a topic that you'd like to see covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
