---
title: 'Friday Q&A 2011-09-16: Let''s Build Reference Counting'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-09-16-lets-build-reference-counting.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a787a3653b86b426'
translated: false
---

> 原文：[Friday Q&A 2011-09-16: Let's Build Reference Counting](https://www.mikeash.com/pyblog/friday-qa-2011-09-16-lets-build-reference-counting.html)　·　mikeash.com Friday Q&A

Posted at 2011-09-16 14:00 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2011-09-30: Automatic Reference Counting](https://www.mikeash.com/pyblog/friday-qa-2011-09-30-automatic-reference-counting.html)  
Previous article: [Friday Q&A 2011-09-02: Let's Build NSAutoreleasePool](https://www.mikeash.com/pyblog/friday-qa-2011-09-02-lets-build-nsautoreleasepool.html)  
Tags: [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [memory](https://www.mikeash.com/pyblog/?tag=memory)

Friday Q&A 2011-09-16: Let's Build Reference Counting

by [Mike Ash](https://www.mikeash.com/)

**Background**  
Everyone reading this probably already has a basic grasp of what reference counting is, but it's good to discuss it in detail to make sure the relevant concepts are clear.

Every Objective-C object has an associated reference count. In Cocoa terminology this is referred to as a "retain count", but I think that just confuses matters so I'll use "reference count". A newly created object starts out with a reference count of `1`. A `retain` message increments it, and a `release` message decrements it. If `release` decrements the reference count to zero, the object is destroyed by sending it the `dealloc` message.

Because reference counting is implemented with plain Objective-C messages, it can be overridden by a particular class. As long as that override follows the above semantics, everything still works.

For what are now largely historical reasons, the default reference counting implementation in `NSObject` does not store the reference count in the object itself. Instead, the reference count is stored in an external table. This can save some memory at the cost of speed. I will replicate this table-based approach in my reimplementation of reference counting.

CoreFoundation objects and many other Cocoa objects override `retain` and `release` in order to store the reference count in the object itself instead, which increases performance a bit.

**Lion and ARC**  
Lion and ARC both saw some substantial changes in the Cocoa memory management system, but the basics discussed above still hold true. Lion reimplemented the table-based reference count system to make it significantly faster, but the fundamental idea is still the same.

ARC still ends up doing `retain` and `release` behind the scenes. For performance reasons, it actually calls runtime functions to retain and release which are able to bypass Objective-C message sends in some cases. However, it still respects `retain` and `release` overrides and _conceptually_ ARC is still just sending `retain` and `release` messages to the objects that it manages.

**Source Code**  
As usual, the code for today is available on GitHub here: [https://github.com/mikeash/refcounting](https://github.com/mikeash/refcounting)

**Design**  
Before I get into the code itself, let's talk about the specifics of this design. There are two methods which need to be implemented. To keep mine separate from Cocoa's, I'll call mine `ma_retain` and `ma_release`.

The reference count table will be implemented using a `CFMutableDictionary` mapping object pointers to integers. This provides a reasonably fast and direct approach.

To make life simpler, the reference count of `1` will be indicated by not having an entry in the table at all. In other words, any pointer's reference count is `1` by default. This means that new objects get the correct reference count of `1` automatically. This is how Cocoa's implementation works as well.

Thread safety is critical for any reference counting implementation. A class typically has no control over which threads it gets retained and released on, and even an otherwise thread-unsafe class needs to be able to withstand being retained and released on separate threads simultaneously, since it's extremely difficult to track and control where retains and releases happen. To make the `CFMutableDictionary` safe, I protect it with an `OSSpinLock`. Any lock will do, but spinlocks are well suited to this case, since they are cheap as long as the critical region is fast.

There are two primitive operations on the table: `GetRefcount` and `SetRefcount`. These take care of the grunt work of manipulating the table, of treating the lack of an entry as `1`, removing objects from the table when their reference count drops below `2`, and such. They do not lock the spinlock, and that is left up to the caller. This is necessary because both `ma_retain` and `ma_release` need to perform two operations on the table atomically, so they need to lock around both.

Building on top of these two primitives are two slightly higher level functions: `IncrementRefcount` and `DecrementRefcount`. `IncrementRefcount` takes a pointer and simply increases that pointer's reference count in the table. `DecrementRefcount` takes a pointer and decrement its reference count. It also returns the new count, which is important for implementing deallocation.

Finally, there are the methods, which are thin wrappers around these higher level functions. `ma_retain` just calls `IncrementRefcount`. `ma_release` calls `DecrementRefcount`, and if the return value is `0`, calls `[self dealloc]`.

**Code**  
Tired of words? Let's do some code.

Two global variables are used for the reference count table. One is the dictionary for the table itself, and the other is the spinlock:

```
    static CFMutableDictionaryRef gRefcountDict;
    static OSSpinLock gRefcountDictLock;
```

The `GetRefcount` function retrieves the current reference count for the given pointer. The `gRefcountDict` variable is initialized lazily, on demand, so the first thing this function does is check to see if the dictionary has been initialized yet. If it hasn't, then it knows that _no_ object has a reference count yet, so the reference count for this object _must_ be `1`:

```
    static uintptr_t GetRefcount(void *key)
    {
        if(!gRefcountDict)
            return 1;
```

If the dictionary does exist, it grabs the value out of it. If the value isn't present, it returns `1` again. Otherwise it returns whatever value is in the dictionary:

```
        const void *value;
        if(!CFDictionaryGetValueIfPresent(gRefcountDict, key, &value))
            return 1;

        return (uintptr_t)value;
    }
```

The `SetRefcount` function sets the reference count for the given pointer to the given value. If the value is `1` or `0`, it simply removes the object from the table:

```
    static void SetRefcount(void *key, uintptr_t count)
    {
        if(count <= 1)
        {
            if(gRefcountDict)
                CFDictionaryRemoveValue(gRefcountDict, key);
        }
```

If the table hasn't been created yet then there's nothing to do, since there can't be any entry to remove.

If the value to set is greater than `1`, it first lazily initializes the table, then sets the object's value in it:

```
        else
        {
            if(!gRefcountDict)
                gRefcountDict = CFDictionaryCreateMutable(NULL, 0, NULL, NULL);
            CFDictionarySetValue(gRefcountDict, key, (void *)count);
        }
    }
```

The `IncrementRefcount` function takes a pointer and increments its value in the table. To do this, it first acquires the spinlock. With the lock held, it fetches the current value, adds one, and then sets that new value. Finally, it releases the spinlock:

```
    static void IncrementRefcount(void *key)
    {
        OSSpinLockLock(&gRefcountDictLock);
        uintptr_t count = GetRefcount(key);
        SetRefcount(key, count + 1);
        OSSpinLockUnlock(&gRefcountDictLock);
    }
```

The `DecrementRefcount` function is much the same. The only real difference is that it needs to return the new count. To make this work, it saves the new count in a temporary variable, then returns it at the end of the function:

```
    static uintptr_t DecrementRefcount(void *key)
    {
        OSSpinLockLock(&gRefcountDictLock);
        uintptr_t count = GetRefcount(key);
        uintptr_t newCount = count - 1;
        SetRefcount(key, newCount);
        OSSpinLockUnlock(&gRefcountDictLock);

        return newCount;
    }
```

Next up are the methods which wrap these functions. These are simple and mostly self explanatory:

```
    @implementation NSObject (MARefcounting)

    - (id)ma_retain
    {
        IncrementRefcount(self);
        return self;
    }

    - (void)ma_release
    {
        uintptr_t newCount = DecrementRefcount(self);
        if(newCount == 0)
            [self dealloc];
    }

    @end
```

Note that `ma_retain` returns `self` to stick with the Cocoa tradition of allowing statements like this:

```
    object = [otherObject retain];
```

It's not an intrinsic requirement of the reference counting system.

That's all there is to the custom reference counting system!

To test it, I wrote some quick code that generates a bunch of objects, retains and releases them in a stress test, and makes sure that they get deallocated. I won't reproduce it here, but you can view that code on GitHub here: [https://github.com/mikeash/refcounting/blob/master/refcounting.m#L80](https://github.com/mikeash/refcounting/blob/master/refcounting.m#L80)

**Conclusion**  
As with autorelease pools, with this simple implementation we can pull back the curtain from Cocoa memory management and see that there is no wizard and no mystery behind the scenes. It's just a simple counting system using standard Objective-C messaging. Cocoa's system has plenty of tricks to make it fast, but fundamentally it's the same as this quick and simple version. Again, we can see the answers to simple questions like "What happens if I retain an object twice?" or "Can I retain an object on one thread and release it on another thread?" If you retain an object twice, you need to release it twice, since it's just a simple increment and decrement. Retain and release don't care what thread you're on, so as long as they balance and synchronize correctly, everything works fine.

That wraps up today's expedition. Come back in two weeks for part three of this journey through the Cocoa memory management system with a discussion of ARC, how it works, and how to use it. As always, Friday Q&A is driven by reader suggestions, so if you have a topic that you would like to see covered, [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-09-16-lets-build-reference-counting.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
