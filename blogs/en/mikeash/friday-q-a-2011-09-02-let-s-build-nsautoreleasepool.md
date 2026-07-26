---
title: 'Friday Q&A 2011-09-02: Let''s Build NSAutoreleasePool'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2011-09-02-lets-build-nsautoreleasepool.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:df788907df6e1ce1'
translated: false
---

> 原文：[Friday Q&A 2011-09-02: Let's Build NSAutoreleasePool](https://www.mikeash.com/pyblog/friday-qa-2011-09-02-lets-build-nsautoreleasepool.html)　·　mikeash.com Friday Q&A

Posted at 2011-09-02 16:30 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2011-09-16: Let's Build Reference Counting](https://www.mikeash.com/pyblog/friday-qa-2011-09-16-lets-build-reference-counting.html)  
Previous article: [Friday Q&A 2011-08-19: Namespaced Constants and Functions](https://www.mikeash.com/pyblog/friday-qa-2011-08-19-namespaced-constants-and-functions.html)  
Tags: [autorelease](https://www.mikeash.com/pyblog/?tag=autorelease) [cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild)

Friday Q&A 2011-09-02: Let's Build NSAutoreleasePool

by [Mike Ash](https://www.mikeash.com/)

**High Level Overview**  
The ball gets rolling when the `autorelease` message is sent to an object. `autorelease` is implemented on NSObject, and just calls through to `[NSAutoreleasePool addObject: self]`. This is a class method, which then needs to track down the right instance to talk to.

`NSAutoreleasePool` instances are stored in a per-thread stack. When a new pool is created, it gets pushed onto the top of the stack. When a pool is destroyed, it's popped off the stack. When the `NSAutoreleasePool` class method needs to look up the current pool, it grabs the stack for the current thread and grabs the pool at the top.

Once the right pool is found, the `addObject:` instance method is used to add the object to the pool. When an object is added to the pool, it's just added to a list of objects kept by the pool.

When a pool is destroyed, it goes through this list of objects and sends `release` to each one. This is just about all there is to it. There is one additional small complication: if a pool is destroyed which is not at the top of the stack of pools, it also destroys the other pools which sit above it. In short, `NSAutoreleasePool` instances nest, and if you fail to destroy an inner one, the outer one will take care of it when it gets destroyed.

**Garbage Collection**  
`NSAutoreleasePool` exists under garbage collection and is even slightly functional. If you use the `drain` message rather than the `release` message, destroying a pool under garbage collection signals to the collector that this might be a good time to run a collection cycle. Aside from this, however, `NSAutoreleasePool` does nothing under garbage collection and isn't very interesting to consider there. For this article I will ignore garbage collection and concentrate on traditional memory management.

**10.7 and ARC**  
10.7 got a major internal overhaul of autorelease pools, and Apple is in the middle of introducing a whole new automatic reference counting system. Although the details have changed a great deal, the concepts of how autorelease pools work have not, so everything here is still valid.

**Interface**  
My version of an autorelease pool class will be called `MAAutoreleasePool`. If you'd like to look at the code in its entirety, it's [available on GitHub](https://github.com/mikeash/MAAutoreleasePool).

This class has class and instance methods for `addObject:`, as well as a `CFMutableArray` to hold the list of autoreleased objects. `CFMutableArray` is used instead of `NSMutableArray` because the automatic `retain` and `release` behavior of `NSMutableArray` will interfere with what we're trying to do here. There's also the possibility that `NSMutableArray` would use `autorelease` internally, which would really mess things up. `CFMutableArray` can be configured not to do any memory management of its contents, which is what we're after here.

The interface then looks like this:

```
    @interface MAAutoreleasePool : NSObject
    {
        CFMutableArrayRef _objects;
    }

    + (void)addObject: (id)object;

    - (void)addObject: (id)object;

    @end
```

Additionally, to match the official implementation, there needs to be a helper method on `NSObject`. I called this `ma_autorelease` to distinguish it from the real thing and avoid name clashes:

```
    @interface NSObject (MAAutoreleasePool)

    - (id)ma_autorelease;

    @end
```

As I mentioned above, the implementation of this is just a cover on the class method:

```
    @implementation NSObject (MAAutoreleasePool)

    - (id)ma_autorelease
    {
        [MAAutoreleasePool addObject: self];
        return self;
    }

    @end
```

**Pool Stack**  
Autorelease pools are kept in a stack. Each thread has its own stack of pools, which is used to determine which pool to put an object in when it gets autoreleased.

To encapsulate the management of the stack, I wrote a private method, `+_threadPoolStack` which returns the current thread's stack of `MAAutoreleasePool` instances, creating it if necessary. Like each pool's list of contained objects, the pool stack is a `CFMutableArray` in order to prevent `NSMutableArray`'s automatic memory management from screwing things up.

The simplest way to handle thread-local storage in Cocoa is with the `threadDictionary` method on `NSThread`. This method returns an `NSMutableDictionary` which is unique to the current thread, and automatically destroyed when the thread terminates.

The first thing this method does, then, is fetch that dictionary and declare a unique key to associate with the pool stack:

```
    + (CFMutableArrayRef)_threadPoolStack
    {
        NSMutableDictionary *threadDictionary = [[NSThread currentThread] threadDictionary];

        NSString *key = @"MAAutoreleasePool thread-local pool stack";
```

Next, it fetches the stack (as a `CFMutableArray`) from that dictionary:

```
        CFMutableArrayRef array = (CFMutableArrayRef)[threadDictionary objectForKey: key];
```

The first time this method runs on any given thread, the stack won't exist yet. In that case, it needs to be created and stored in the dictionary:

```
        if(!array)
        {
            array = CFArrayCreateMutable(NULL, 0, NULL);
            [threadDictionary setObject: (id)array forKey: key];
            CFRelease(array);
        }
```

Finally, with the array either retrieved or newly created, it's returned:

```
        return array;
    }
```

Now that this is in place, the other methods can be implemented. The `+addObject:` method essentially just calls the above and then forwards the `addObject:` to the pool at the top of the stack. I added a bit of paranoia to make sure that the stack isn't empty, and to print an error if it is:

```
    + (void)addObject: (id)object
    {
        CFArrayRef stack = [self _threadPoolStack];
        CFIndex count = CFArrayGetCount(stack);
        if(count == 0)
        {
            fprintf(stderr, "Object of class %s autoreleased with no pool, leaking\n", class_getName(object_getClass(object)));
        }
        else
        {
            MAAutoreleasePool *pool = (id)CFArrayGetValueAtIndex(stack, count - 1);
            [pool addObject: object];
        }
    }
```

**Instance Methods**  
The `-init` method for this class is really simple. Initialize the `_objects` array, add `self` to the top of the pool stack, and return:

```
    - (id)init
    {
        if((self = [super init]))
        {
            _objects = CFArrayCreateMutable(NULL, 0, NULL);
            CFArrayAppendValue([[self class] _threadPoolStack], self);
        }
        return self;
    }
```

The `-addObject:` method is even simpler: just add the given object to the end of `_objects`:

```
    - (void)addObject: (id)object
    {
        CFArrayAppendValue(_objects, object);
    }
```

The `-dealloc` method gets more interesting, due to the need to nest pools. It starts out easily enough: iterate through the `_objects` array and send a `release` to everything in it:

```
    - (void)dealloc
    {
        if(_objects)
        {
            for(id object in (id)_objects)
                [object release];
            CFRelease(_objects);
        }
```

Next, it removes `self` from the pool stack. Additionally, it also needs to remove any pools which sit above it in the pool stack. Because this process needs to iterate backwards and needs to be able to modify the stack while iterating, it uses a manual index-based loop:

```
        CFMutableArrayRef stack = [[self class] _threadPoolStack];
        CFIndex index = CFArrayGetCount(stack);
        while(index-- > 0)
        {
            MAAutoreleasePool *pool = (id)CFArrayGetValueAtIndex(stack, index);
```

If `pool` is `self`, then the loop is done. All that needs to be done is to remove the entry from the stack and then break out of the loop. All pools in the stack below the current one are left alone:

```
            if(pool == self)
            {
                CFArrayRemoveValueAtIndex(stack, index);
                break;
            }
```

If it's some other pool, then it needs to be destroyed. This is done by simply sending a `release` to it. Everything else that needs to happen will be done automatically:

```
            else
            {
                [pool release];
            }
        }
```

This may be a little hard to understand at first, and it took me a little while to realize how this code needed to be written. When this line is hit, `pool` is necessarily at the top of the stack. When it's released, it will be deallocated (it's not legal to retain autorelease pools). When it gets deallocated, it will call into its own `-dealloc` which enters into this same loop again. This loop immediately hits the `pool == self` condition, removing the pool from the stack and exiting. Thus, all pools on the stack above the one currently being destroyed also get destroyed and removed from the stack.

The loop is now done, and all that's left to do is call through to `super`:

```
        [super dealloc];
    }
```

The class is now complete!

**Lessons**  
There are some good lessons to be learned from this exercise. Most importantly is that `NSAutoreleasePool` is a pretty straightforward class without much in the way of hidden gotchas. There's nothing complex going on behind the scenes. People new to Cocoa memory management often imagine that `autorelease` is much more complex than it really is, and ask questions like "How can I tell if an object has been autoreleased?" or "What happens if I autorelease an object twice?" Specifically, we can now see:

- There's no way to tell if an object has been autoreleased. The pool is a fairly dumb container with only the barest idea of what it contains. It really just keeps a list for the purposes of sending `release` to those objects later. This is perfectly fine, because your code should never care whether an object has already been autoreleased.
- Objects that are autoreleased twice just get added to the pool twice, and then when the pool is destroyed they get released twice.
- Autoreleased objects get released when the current autorelease pool is destroyed. Pools are destroyed when the code that created them explicitly destroys them. If you aren't managing your own pools, then autoreleased objects will survive at least until you return to code you don't own (like Cocoa).
- If you autorelease an object on one thread and then pass it to another thread, nothing special happens. The object is still released when the first thread's pool gets destroyed, regardless of what's happening on the new thread. If you need an object to survive the passage, it needs to be retained before sending and then released after receiving. (Fortunately, the cross-thread messaging mechanisms you're likely to use with objects, like GCD/blocks and Cocoa's `perform...` methods do this for you.)

**Conclusion**  
That wraps up today's exploration of Cocoa internals. Now you know approximately how `NSAutoreleasePool` gets its job done and how it works. The implementation specifics vary (especially on Lion), but the basic ideas are the same. By knowing how memory management internals work, you can write better and less error-prone code.

Unless you're completely new to this blog, you probably already know that Friday Q&A is driven by reader submissions. On that note, if you have a topic that you'd like to see covered, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2011-09-02-lets-build-nsautoreleasepool.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
