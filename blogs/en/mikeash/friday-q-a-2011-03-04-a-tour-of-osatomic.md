---
title: 'Friday Q&A 2011-03-04: A Tour of OSAtomic'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-03-04-a-tour-of-osatomic.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:adfc834d710a1a58'
translated: false
---

> 原文：[Friday Q&A 2011-03-04: A Tour of OSAtomic](https://www.mikeash.com/pyblog/friday-qa-2011-03-04-a-tour-of-osatomic.html)　·　mikeash.com Friday Q&A

Posted at 2011-03-04 18:24 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [See Me Speak at Voices That Matter in Seattle](https://www.mikeash.com/pyblog/see-me-speak-at-voices-that-matter-in-seattle.html)  
Previous article: [Friday Q&A 2011-02-18: Compound Literals](https://www.mikeash.com/pyblog/friday-qa-2011-02-18-compound-literals.html)  
Tags: [atomic](https://www.mikeash.com/pyblog/?tag=atomic) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [threading](https://www.mikeash.com/pyblog/?tag=threading)

Friday Q&A 2011-03-04: A Tour of OSAtomic

by [Mike Ash](https://www.mikeash.com/)

**Threaded Programming and Atomic Operations**  
 As anyone who does threaded programming knows, it's difficult. Really difficult. Threaded execution results in highly unpredictable timing with how multiple threads interact with each other. The result is that code which appears to be correct and passes tests can be subtly flawed in such a way that it fails rarely and mysteriously.

There are many rules to follow when writing threaded code, but the most important one is this: **lock all access to shared data**.

Shared data is any data which more than one thread can access. If you have any, then you _must_ use locks to synchronize that access. Another approach to threaded programming is to forego shared data and instead use message passing, which means that only one thread at a time will be accessing the message and any shared data.

Atomic operations allow you to sidestep this requirement and access shared data without using locks. The word "atomic" here is not used in the sense of bombs or reactors, but in the ancient Greek sense of "indivisible". An atomic operation is one which happens all in one shot, and which can't be interrupted by another thread while in progress. OSAtomic is OS X's library of such atomic operations.

**The Header**  
 OSAtomic functions are located in the `OSAtomic.h` header, located at `/usr/include/libkern/OSAtomic.h`. note that despite that `kern` part, these functions are perfectly usable and useful from regular userland code. You can import the file with:

```
    #import <libkern/OSAtomic.h>
```

The functions can be divided into five essential categories:

- Integer operations
- Fundamental operations
- Spinlocks
- Queues
- Memory barriers

I will discuss these categories one by one in this order.

Before I begin that, I want to briefly discuss memory barriers. All of the functions in the first two categories have two variants. One is a basic function, and the other is that same function but with `Barrier` at the end of the name. I will ignore the difference between these two types for now, and cover it all in the section about memory barriers. Until then, I will state one simple fact about the variants: it's always safe to use the `Barrier` variant instead of the base variant, with the only problem being a small performance penalty, so use `Barrier` unless you really know what you're doing.

**A Quick Note on Data Types and Alignment**  
 Due to the finnicky and low-level nature of atomic operations, there are significant limits on data types and alignments. Atomic operations are only available for 32-bit and 64-bit data types, and on some platforms (PowerPC being the only OS X one that I know of) they are only available for 32-bit. Always use data types with a guaranteed size, such as `int32_t`, rather than built-in types ilke `int`.

The values must also be aligned to their size. This means that the address of the value has to be a multiple of the value's size. Normally this is done for you. Objects and memory allocations are aligned on 16-byte boundaries on OS X, and the compiler ensures that the individual data members are allocated within that. Alignment should only be a worry if you're messing around with addresses trying to set up your own packing or using packed structs. And, well, don't use atomic operations with those.

**Integer Operations**  
 The integer operations are the first ones found in the header and they operate similarly to standard C integer operations. They all modify a value in-place, so they are really equivalent to the C augmented assigment operators like `+=`.

Since C already has these operators, why are these functions needed? As with the rest of this header, atomicity is the name of the game. Consider the following code:

```
    x += 1;
```

And then consider what can happen if multiple threads execute it, with the same `x`, simultaneously. At a low level, this single line of code breaks down into multiple operations:

```
    fetch value of x
    add 1
    store new value of x
```

On some architectures this happens in assembly language, and in some it happens at the hardware level, but it can happen. Two threads may both fetch the current value of x, add 1, and store, resulting in a missed increment. The equivalent OSAtomic function does not suffer from this problem and the result after having two threads execute it is guaranteed to be correct.

The atomic equivalent of `+=` is `OSAtomicAdd32` (as well as one for 64-bit values on platforms that support it). It takes an amount to add and a pointer to the value to modify. It also returns the new value, which allows you to better coordinate between threads. For example, you might have several threads that each want to work on a single element of an array. By using the return value, you can assign a unique index to each one:

```
    // initialization, before the threads go
    int32_t sharedIndex = 0;
    
    // in each thread to get the index
    int index = OSAtomicAdd32(1, &sharedIndex) - 1;
    // subtract 1 because it returns the NEW value
```

If necessary, you can perform a subtraction using this method simply by passing a negative value.

There are also convenience functions equivalent to `++` and `--`, `OSAtomicIncrement` and `OSAtomicDecrement`. Using `OSAtomicIncrement32` would make the above code slightly simpler.

There are also functions for doing bitwise logical options. The `|=`, `&=`, and `^=` operators have atomic equivalents in `OSAtomicOr`, `OSAtomicAnd`, and `OSAtomicXor`. These have somewhat more exotic uses, but can be handy for manipulating bitfields in a thread-safe manner.

**Fundamental Operations**  
 The above integer operations are all, at least conceptually, built on top of a single fundamental atomic operation: compare and swap. A compare and swap function takes an old value, a new value, and a pointer to a variable. It replaces the variable's contents with the new value if and only if the variable currently matches the old value. It also returns whether the operation succeeded (the variable matched the old value) or failed (the variable didn't match). To make this more clear, imagine a function like this:

```
    bool CompareAndSwap(int old, int new, int *value)
    {
        if(*value == old)
        {
            *value = new;
            return true;
        }
        else
            return false;
    }
```

This is how a compare and swap operation works, except that compare and swap is an atomic operation. It cannot be interrupted or preempted in the middle. If the new value is assigned and the function returns `true` then you can be absolutely certain that the value transitioned directly from `old` to `new` without any other intermediate value.

This gives us the building blocks to create more complex and useful atomic operations. The basic model of using compare and swap is that of a transaction, as you might find in databases. Conceptually, you build code that begins a transaction, carries out a local modification, then attempts to commit the transaction. The commit is done using a compare and swap. If the commit fails, which is indicated by the compare and swap returning `false`, then you go back to the beginning and start a new transaction to try it again.

OSAtomic provides this operation with the `OSAtomicCompareAndSwap` family of functions. There is one for 32-bit integers, for pointers, and for `int` and `long`. There is also one, on platforms which support it, for 64-bit integers.

To see how you can use these, let's consider how you would write `OSAtomicAdd32` using compare and swap. Again, it works using a transaction model. First, fetch the original value. Then add to obtain a new value. Finally, use compare and swap with the original and new values. If it failed, go back and try everything again. In code:

```
    int32_t OSAtomicAdd32(int32_t howmuch, volatile int32_t *value)
    {
        bool success;
        int32_t new;
        
        do {
            int32_t orig = *value;
            new = orig + howmuch;
            success = OSAtomicCompareAndSwap32(orig, new, value);
        } while(!success);
        
        return new;
    }
```

The real thing may be implemented more efficiently, for example using a CPU primitive which directly does an atomic addition. For that reason, and simply to avoid duplicating code, you'd want to call the built-in function rather than writing out the long version above. However, the existence of compare and swap creates flexibility because you aren't limited to just add, or, and, and xor. You could write a similar function to perform an atomic multiplication or division. Additionally, you can use compare and swap on pointers, which is where things start to get really useful.

For example, here is a function which adds a node to the head of a linked list:

```
    void AddNode(ListNode *node, ListNode * volatile *head)
    {
        bool success;
        
        do {
            ListNode *orig = *head;
            node->next = orig;
            success = OSAtomicCompareAndSwapPtrBarrier(orig, node, (void *)head);
        } while(!success);
    }
```

Note that I use the `Barrier` variant here. This is because the compare and swap operation makes the data contained inside `node` visible to other threads, and the barrier is necessary to ensure that that data is properly updated for all threads before they can see it. As I mentioned before, I will go into more detail about barriers later.

Here is a companion function which "steals" the list. This replaces the list with an empty list (which is to say, `NULL`) and returns the old list head so that it can be operated on:

```
    ListNode *StealList(ListNode * volatile *head)
    {
        bool success;
        ListNode *orig;
        
        do {
            orig = *head;
            success = OSAtomicCompareAndSwapPtrBarrier(orig, NULL, (void *)head);
        } while(!success);
        
        return orig;
    }
```

This kind of structure can be really useful in multithreaded programming. Many threads can safely use `AddNode` to add new nodes to the structure. A worker thread can then use `StealList` to grab the list and process it.

**ABA Problem**  
 You might wonder why I implemented `StealList` instead of, say, `RemoveNode`. The answer is that `RemoveNode` is harder than it looks. You might think that you could implement it like so:

```
    ListNode *RemoveNode(ListNode * volatile *head)
    {
        bool success;
        ListNode *orig;
        
        do {
            orig = *head;
            ListNode *next = orig->next;
            success = OSAtomicCompareAndSwapPtrBarrier(orig, next, (void *)head);
        } while(!success);
        
        return orig;
    }
```

Trouble is, there's a subtle scenario where this fails badly. Let's imagine that the list starts out looking like this:

```
    A -> B -> C
```

This function executes. `orig` points to A, and `next` points to B. However, before it gets to the compare and swap, it is preempted and another thread runs. That thread then calls `RemoveNode` twice, leaving the list like this:

```
    C
```

That thread then adds A back to the list, and destroys B. The list now looks like this:

```
    A -> C
```

Finally, the original thread resumes execution. It executes the compare and swap to replace A with B. Since the list head is A, the compare and swap succeeds. However, the result is a disaster! The list head is now set to B, which has been destroyed. C is lost, and the next bit of code that manipulates the list will try to access B and will crash. Oops.

This is a fairly rare scenario, but that very rarity makes it serious. The last thing you want when writing multithreaded code is to create code which fails rarely. It had better fail frequently or not at all, otherwise it's going to be really hard to track down and fix.

**Test and Set**  
 Test and set is a somewhat specialized fundamental atomic operation. It is not as useful as compare and swap, but can be handy for certain things. I have not ever had an occasion to use it myself, though, and it's generally limited to implementing locks and semaphores. It's generally better to use higher-level abstractions of those than to try to implement them yourself.

**Spinlocks**  
 A spinlock is a primitive type of lock that does not use any OS facilities. A lock in general is a facility which provides mutual exclusion between threads. Two threads attempt to acquire a lock. One succeeds, the other waits. When the first one unlocks the lock, the second one then acquires it.

Generally, when the second thread is waiting, we want it to be blocked so that it does not take any CPU time while it's blocked. This requires intervention by the OS to stop the thread, and start it again when unlocking. This OS intervention comes with a certain amount of overhead that is not always desirable.

Spinlocks are extremely lightweight and operate entirely in userland. The downside is that when a thread waits, it's not blocked, but continues to check the spinlock until it comes unlocked. Spinlocks perform very well when a lock is not contended (only one thread at a time is accessing it) but perform poorly when a lock is contended for an extended period.

A spinlock is a primitive value of type `OSSpinLock`. You then pass a pointer to the spinlock to `OSSpinLockTry`, `OSSpinLockLock`, or `OSSpinLockUnlock` to accomplish the various operations. In terms of the basic semantics, these are the same as those of `pthread_mutex` or `NSLock`, only the implementation differs. You should generally use those higher-level abstractions, but spin locks are useful when performance is absolutely critical and contention is rare.

**Queues**  
 This is something of a misname, as the facility provided is actually a stack, not a queue. However, OSAtomic calls them `OSQueue`, so "queues" they are.

Unfortunately, after some additional investigation, I discovered that `OSQueue` is not entirely thread safe and thus should not be used. Since I have no idea if or when this will be fixed, you should avoid the use of `OSQueue`.

**Memory Barriers**  
 A major challenge with multithreaded programming is dealing with the fact that, not only is there a great deal of strange behavior due to timing and OS issues, but the hardware sometimes causes problems as well. Some architectures reorder memory reads and writes for extra speed. These reorderings are hidden from the program by the CPU, but they are _not_ hidden from code executing on other CPUs at the same time. This can cause serious problems.

For an example scenario where this could cause trouble, consider the following code:

```
    volatile Structure *gStructure;
    
    // thread 1
    Structure *s = malloc(sizeof(s));
    s->field1 = 0;
    s->field2 = 42;
    gStructure = s;
    
    // thread 2
    Structure *s;
    while((s = gStructure) == NULL)
        /* poll */;
    printf("%d\n", s->field2);
```

There is the very real possibility with this code that thread 2 will not print the correct value. This could happen if the CPU reorders the writes in thread 1 such that the assignment to `gStructure` happens before the assignments to the fields. Marking things as `volatile` doesn't do anything to fix this, as that only controls potential _compiler_ reordering, not CPU reordering.

Memory barriers are a way to solve this. A memory barrier forces all all reads before the barrier to complete before any reads after the barrier complete. The same goes for writes. Technically, there can be separate barriers for reads and writes, but OSAtomic rolls them both into a single concept.

If you just want a plain memory barrier, you can get one by using `OSMemoryBarrier`. This function takes no parameters and returns nothing, as its sole purpose is to act as a memory barrier. The above code could then be restructured as:

```
    // thread 1
    Structure *s = malloc(sizeof(s));
    s->field1 = 0;
    s->field2 = 42;
    OSMemoryBarrier();
    gStructure = s;
    
    // thread 2
    Structure *s;
    while((s = gStructure) == NULL)
        /* poll */;
    OSMemoryBarrier();
    printf("%d\n", s->field2);
```

This is safe. Technically, the barrier in the second thread should not be necassary, as the second read depends on the first. (The value of `s` needs to be available before the value of `s->field2` can be retrieved.) However, these things can be difficult to reason through and I often prefer to simply be safe rather than try to figure out whether it's _really_ needed.

In addition to this function, OSAtomic also offers memory barriers with all of its atomic operations. The `Barrier` variants of all the atomic functions means that they not only accomplish the given atomic operation, but also incorporate a memory barrier. This is extremely useful when you're performing an atomic operation which has implications about data beyond the single chunk that you're operating on.

As a general rule of thumb, standalone counters, flags, and other self-contained bits of data which exist within the single 32-bit or 64-bit value that you're operating on don't need barriers. Anything where the atomic operation signals something about data not included in the value that you're operating on needs a barrier.

When in doubt, use a barrier. The only downside to using one when you don't need it is a small performance cost.

**Conclusion**  
 Threaded programming is difficult. Shared data makes it harder. Shared data without locks makes it even harder still. However, there are cases where it can be useful to program that way, and when you absolutely need lockless threaded code, OSAtomic gives you the building blocks.

That's it for today. Come back in another 14 days for the next exciting edition of your friendly neighborhood Friday Q&A. As always, Friday Q&A is driven by the readers, so if you have an idea for a topic you would like to see covered here, [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-03-04-a-tour-of-osatomic.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
