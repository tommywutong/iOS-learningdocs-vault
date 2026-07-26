---
title: 'Friday Q&A 2015-02-20: Let''s Build @synchronized'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-02-20-lets-build-synchronized.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a9326de12f1337bd'
translated: false
---

> 原文：[Friday Q&A 2015-02-20: Let's Build @synchronized](https://www.mikeash.com/pyblog/friday-qa-2015-02-20-lets-build-synchronized.html)　·　mikeash.com Friday Q&A

Posted at 2015-02-20 14:26 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2015-03-20: Preprocessor Abuse and Optional Parentheses](https://www.mikeash.com/pyblog/friday-qa-2015-03-20-preprocessor-abuse-and-optional-parentheses.html)  
Previous article: [Friday Q&A 2015-02-06: Locks, Thread Safety, and Swift](https://www.mikeash.com/pyblog/friday-qa-2015-02-06-locks-thread-safety-and-swift.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [swift](https://www.mikeash.com/pyblog/?tag=swift) [threading](https://www.mikeash.com/pyblog/?tag=threading)

Friday Q&A 2015-02-20: Let's Build @synchronized

by [Mike Ash](https://www.mikeash.com/)

**Recap**  
`@synchronized` is a control construct in Objective-C. It takes an object pointer as a parameter and is followed by a block of code. The object pointer acts as a lock, and only one thread is permitted within a `@synchronized` block with that object pointer at any given time.

It's a simpler way of using locks for multithreaded programming. For example, you might use an `NSLock` to protect access to an `NSMutableArray`:

```
    NSMutableArray *array;
    NSLock *arrayLock;

    [arrayLock lock];
    [array addObject: obj];
    [arrayLock unlock];
```

Or you can use `@synchronized` to use the array itself as the lock:

```
    @synchronized(array) {
        [array addObject: obj];
    }
```

I personally prefer an explicit lock, both to make it clearer what's going on, and because `@synchronized` doesn't perform quite as well for reasons we'll see below. However, it can be convenient, and it's interesting to build regardless.

**Implementation Theory**  
The Swift version of `@synchronized` is a function that takes an object and a closure, and invokes the closure with the lock held:

```
    func synchronized(obj: AnyObject, f: Void -> Void) {
        ...
    }
```

The question is, how do you turn an arbitrary object into a lock?

In an ideal world (from the perspective of implementing this function), every object would have a little extra space set aside for a lock. `synchronized` could then use the appropriate lock and unlock functions on that little extra space. However, no such extra space exists, which is probably fortunate because it would bloat the memory size of every object on the system for a feature that most of them will never encounter.

The alternative is to use a table that maps an object to a lock. `synchronized` can then look up the lock in the table, and lock and unlock it there. The trouble with this approach is that the table itself needs to be thread safe, which either requires its own lock or some sort of fancy lockless data structure. A separate lock for the table is by far easier.

To prevent locks from building up forever, the table needs to track lock usage and destroy or reuse locks when they're no longer needed.

**Implementation**  
For the table that maps objects to locks, `NSMapTable` fits the bill perfectly. It can be configured to use raw object addresses as its keys, and it can hold weak references to both keys and values which allows the system to automatically reclaim unused locks. This sets it up appropriately:

```
    let locksTable = NSMapTable.weakToWeakObjectsMapTable()
```

The objects will be instances of `NSRecursiveLock`. Because it's a class, it works well with `NSMapTable`, as opposed to something like `pthread_mutex_t`. `@synchronized` provides recursive semantics and this does the same.

The table itself also needs a lock. A spinlock works well here, as accesses to the table will be brief:

```
    var locksTableLock = OS_SPINLOCK_INIT
```

With the table in place, we can implement the function:

```
    func synchronized(obj: AnyObject, f: Void -> Void) {
```

The first thing it does is look up the lock corresponding to `obj` in `locksTable`. This must be done with `locksTableLock` held:

```
        OSSpinLockLock(&locksTableLock)
        var lock = locksTable.objectForKey(obj) as! NSRecursiveLock?
```

If there's no entry in the table, create a new lock and set it:

```
        if lock == nil {
            lock = NSRecursiveLock()
            locksTable.setObject(lock!, forKey: obj)
        }
```

With the lock in hand, the master table lock can be released. This _must_ be done before invoking `f` in order to avoid a potential deadlock:

```
        OSSpinLockUnlock(&locksTableLock)
```

Now we can invoke `f`, locking and unlocking `lock` around the invocation:

```
        lock!.lock()
        f()
        lock!.unlock()
    }
```

**Comparison With Apple's Implementation**  
Apple's implementation of `@synchronized` is available as part of the Objective-C runtime source distribution. This specific bit is available here:

[http://www.opensource.apple.com/source/objc4/objc4-646/runtime/objc-sync.mm](http://www.opensource.apple.com/source/objc4/objc4-646/runtime/objc-sync.mm)

It's build for speed rather than simplicity as the above toy implementation is. It's interesting to see what it does the same and what it does differently.

The basic concept is the same. There's a global table that maps object pointers to locks, and the lock is then locked and unlocked around the `@synchronized` block.

For the underlying lock object, Apple's version uses `pthread_mutex_t` configured as a recursive lock. Since `NSRecursiveLock` is likely implemented using `pthread_mutex_t` anyway, this cuts out the middleman, and avoids a dependency on Foundation in the runtime.

The table itself is implemented as a linked list rather than a hash table. Since the common case is that only a few locks exist at any given time, this will still perform well, and probably performs better than a hash table, since the performance advantage of hash tables comes with larger data sets. Performance is further improved with a per-thread cache that saves locks that were recently looked up on the current thread.

Instead of a single global table, there are 16 tables kept in an array. Objects are mapped to different tables depending on their address. This reduces unnecessary contention between `@synchronized` blocks operating on different objects, since they will likely use different global tables.

Instead of using weak pointers, which incur substantial additional overhead, Apple's implementation instead keeps an internal reference count alongside each lock. When the reference count reaches zero, the lock is available for reuse with a new object. Unused locks are not destroyed, but reuse means that the total number of locks is limited to the maximum number of active locks at any given time, rather than growing without bound as new objects are used.

Apple's implementation is intelligent and fast for what it does, but it still incurs some unavoidable extra overhead compared to using a separate, explicit lock. In particular:

1. Unrelated objects can still be subject to contention if they happen to be assigned to the same global table.
2. A spinlock must be acquired and released when looking up the lock in the common case where it doesn't exist in the per-thread cache.
3. Additional work must be done to look up the appropriate lock for the object in the global table.
4. Each lock/unlock cycle incurs overhead for recursive semantics even when it's not required.

However, these problems are more or less inherent to what `@synchronized` does, and the implementation certainly can't be faulted for it. It's a great piece of code that's well worth reading through.

**Conclusion**  
`@synchronized` is an interesting language construct with some implementation challenges. Fundamentally, it provides thread safety, but the implementation itself requires synchronization to be safe. Using a global lock behind the scenes to protect access to the lock table solves this dilemma. Clever tricks in Apple's implementation allow it to be reasonably fast.

That's it for today. Come back next time for more amusing whatnot. Friday Q&A is driven by reader suggestions, so if you have an idea you'd like to see covered, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2015-02-20-lets-build-synchronized.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
