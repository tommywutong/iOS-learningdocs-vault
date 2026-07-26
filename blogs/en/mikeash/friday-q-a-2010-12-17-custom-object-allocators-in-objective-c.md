---
title: 'Friday Q&A 2010-12-17: Custom Object Allocators in Objective-C'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-12-17-custom-object-allocators-in-objective-c.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b8f6776f5a7a28f4'
translated: false
---

> 原文：[Friday Q&A 2010-12-17: Custom Object Allocators in Objective-C](https://www.mikeash.com/pyblog/friday-qa-2010-12-17-custom-object-allocators-in-objective-c.html)　·　mikeash.com Friday Q&A

Posted at 2010-12-17 18:27 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2010-12-31: C Macro Tips and Tricks](https://www.mikeash.com/pyblog/friday-qa-2010-12-31-c-macro-tips-and-tricks.html)  
Previous article: [Friday Q&A 2010-12-03: Accessors, Memory Management, and Thread Safety](https://www.mikeash.com/pyblog/friday-qa-2010-12-03-accessors-memory-management-and-thread-safety.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [memory](https://www.mikeash.com/pyblog/?tag=memory) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2010-12-17: Custom Object Allocators in Objective-C

by [Mike Ash](https://www.mikeash.com/)

**What It Means**  
 As anyone who uses Objective-C knows, you allocate an instance of a class by writing `[MyClass alloc]`. Creating a custom allocator simply means that replace the standard allocator so that `[MyClass alloc]` calls into your own code instead.

An Objective-C object [is just a chunk of memory with the right size, and with the first pointer-sized chunk set to point at the object's class](https://www.mikeash.com/pyblog/friday-qa-2009-03-13-intro-to-the-objective-c-runtime.html). A custom allocator thus needs to return a pointer to a properly-sized chunk of memory, with the class filled out appropriately.

**Why It's Useful**  
 By far the largest reason to write a custom allocator is for performance. The standard allocator makes tradeoffs which may not be appropriate for your particular case. It also has to work with every class in every situation, whereas your custom allocator only needs to work with your class and the situations it's used in.

Another reason is overhead. The standard allocator requires a certain amount of extra storage for each allocation for various reasons. This can be particularly expensive for very small objects allocated in very large numbers. A custom allocator can cut down on this overhead substantially by tailoring it to the needs of the class it's written for.

**A Note on Garbage Collection**  
 This post assumes manual `retain`/`release` memory management. Custom allocators are mostly impossible to use under garbage collection, because there is no way to add a custom `free` callback. It is possible to use some of these techniques (like an object cache) but for the most part, custom allocators are reserved for the realm of manual memory management.

**A Basic Custom Allocator**  
 The `+alloc` method actually just calls through to `+allocWithZone:`. Although memory zones are pretty much just a historical curiosity at this point, they remain in the API. Thus the method to override is `+allocWithZone:`:

```
    + (id)allocWithZone: (NSZone *)zone
    {
```

For a simple allocator example, I'll just call `calloc`. This will have roughly zero advantages over the standard allocator, but shows how it can be done. (I'm using `calloc` instead of `malloc` because Objective-C code assumes that instance variables are zeroed out.)

In order to call `calloc`, you need to know how much memory to allocate. Fortunately, the Objective-C runtime makes it easy. The `class_getInstanceSize` function will tell you exactly this:

```
        id obj = calloc(class_getInstanceSize(self), 1);
```

Next, you need to set the isa of this newly-allocated object. The isa is found right at the beginning of the object, and a bit of judicious casting lets you set it easily:

```
        *(Class *)obj = self;
```

You can now return the newly created object:

```
        return obj;
    }
```

We're not done yet. We also have to override `-dealloc` to call `free`:

```
    - (void)dealloc
    {
        free(self);
```

Normally this would be all. However, the compiler has a warning for `-dealloc` methods that don't call through to `super`. In order to shut up this warning, I insert a dummy call after a `return` statement which prevents it from executing:

```
        return;
        [super dealloc]; // shut up compiler
    }
```

Your custom allocator is all ready to go.

**Gotchas**  
 As with most things at this level, there are a few things to watch out for.

First, don't do this unless you subclass `NSObject` directly. The `-dealloc` method covers both destroying the object itself, and freeing resources it holds. `-[NSObject dealloc]` just destroys the object (mostly) so it's safe not to call it. It's not safe to do this for any other class, though. For example, if you tried this with an `NSView` subclass, you'd end up leaking a whole bunch of internal state.

Second, the "(mostly)" from above means there are some things that `NSObject` does that you need to think about. One is removing associated objects. If your objects may have associated objects, or you think there's even a chance that it might, then you need to make sure they're removed. This can be done by calling `objc_removeAssociatedObjects(self)`. The other is calling destructors for C++ objects in instance variables. Your best bet here is to just avoid having C++ objects as instance variables. If you must have them, look into the possibility of calling or imitating the private runtime function `objc_destructInstance`, which takes care of both C++ destructors and associated objects.

Third, memory debugging tools like ObjectAlloc and zombies won't work on objects with a custom allocator. For this reason, I recommend that you have a memory debugging preprocessor define which makes your objects use the standard allocator instead of your custom allocator, so that you can flip the switch and use these tools if need be.

**Caching Objects**  
 For a realistic example, I'll write an allocator that places destroyed objects in a cache so that they can be quickly reused. This sort of thing is useful for classes which are allocated and destroyed so frequently that the standard allocator is too slow.

In order to reach maximum speed, I'll make a few assumptions about how this class works and is used:

- It is never subclassed, or if it is, subclasses never add instance variables. (This allows it to put all instances in the same cache.)
- Its initializer methods can deal with a "dirty" object; i.e. the instance variables don't need to be zeroed out. (This saves time zeroing out each instance when pulling it out of the cache.)
- It is only ever allocated and destroyed from the same thread. (This makes it unnecessary to create a thread-safe cache.)

I'll ignore just how the cache works for now, and just assume it presents a simple interface of two functions: `AddObjectToCache` and `GetObjectFromCache`. The `+allocWithZone:` override then looks like this:

```
    + (id)allocWithZone: (NSZone *)zone
    {
        id obj = GetObjectFromCache();
        if(obj)
            *(Class *)obj = self;
        else
            obj = [super allocWithZone: zone];
        return obj;
    }
```

The `-dealloc` override simply returns the object to the cache:

```
    - (void)dealloc
    {
        // release any ivars here
        AddObjectToCache(self);
        
        // shut up the compiler
        return;
        [super dealloc];
    }
```

The cache itself is just a linked list, using the `isa` slot of each object to point to the next entry in the list. The list head is a global variable:

```
    static id gCacheListHead;
```

Next, I want a couple of helper functions for accessing the `next` pointer of each list item:

```
    static id GetNext(id cachedObj)
    {
        return *(id *)cachedObj;
    }
    
    static void SetNext(id cachedObj, id next)
    {
        *(id *)cachedObj = next;
    }
```

With these helpers, the two main cache functions are easy to write:

```
    static id GetObjectFromCache(void)
    {
        id obj = gCacheListHead;
        if(obj)
            gCacheListHead = GetNext(obj);
        return obj;
    }
    
    static void AddObjectToCache(id obj)
    {
        SetNext(obj, gCacheListHead);
        gCacheListHead = obj;
    }
```

With this system in place, objects are initially allocated normally, but then go into the cache when destroyed. Once the cache has objects, new objects come out of it, which is much faster than allocating new memory.

**Custom Block Allocator**  
 Caching objects can be a big speed boost, but the initial allocations are not accelerated, and you still have the space overhead of all of those small allocations. By allocating a large block of memory and chopping it up into chunks, it's possible to speed up the initial allocations and vastly decrease the per-object overhead. To do this, I'll use the same object cache scheme as above, but with a modification to the `+allocWithZone:` implementation:

```
    + (id)allocWithZone: (NSZone *)zone
    {
        id obj = GetObjectFromCache();
        if(!obj)
        {
            AllocateNewBlockAndCache(self);
            obj = GetObjectFromCache();
        }
        *(Class *)obj = self;
        return obj;
    }
```

All of the interesting stuff will then happen in `AllocateNewBlockAndCache`. The first thing this function will do is allocate a large block of memory. I chose `4096` for the block size as it matches the page size used by OS X and is a convenient number to work with:

```
    static void AllocateNewBlockAndCache(Class class)
    {
        static size_t kBlockSize = 4096;
        char *newBlock = malloc(kBlockSize);
```

Once it has this block, it needs to chop it into pieces and add each piece to the cache. To do this, it will walk through the block using `class_getInstanceSize` to mark off each instance-sized section, and then use `AddObjectToCache` to get each section into the cache:

```
        int instanceSize = class_getInstanceSize(class);
        int instanceCount = kBlockSize / instanceSize;
        while(instanceCount-- > 0)
        {
            AddObjectToCache((id)newBlock);
            newBlock += instanceSize;
        }
    }
```

That's all there is to it. The object caching mechanism takes care of recycling old objects so that they can be used again.

**Conclusion**  
 Writing a custom object allocator in Objective-C is relatively simple. The hard part is the allocator itself, which is largely up to you. Once you have the allocator, you can plug it into your Objective-C class by:

1. Overriding `+allocWithZone:` to call your custom allocator, set the `isa` of the block to `self`, and optionally zero out the rest of the memory.
2. Overriding `-dealloc` to call your custom allocator, and do _not_ call through to `super`.
3. Calling `objc_removeAssociatedObjects` in `-dealloc` if there's a chance of your object containing associated objects.
4. Only subclassing `NSObject` directly, and not subclassing any subclass of `NSObject`.

In addition to a full-blown custom allocator, techniques like object caching can give you a speed boost with less complexity.

That's it for this edition of Friday Q&A. Come back in two weeks for the next exciting edition. As always, your ideas for topics to cover are welcome and requested, so if you have something that you would like to see covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-12-17-custom-object-allocators-in-objective-c.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
