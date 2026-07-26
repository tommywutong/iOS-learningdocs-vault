---
title: an article about locks and thread safety in Swift
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-02-06-locks-thread-safety-and-swift.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a145ce48fc0cec4a'
translated: false
---

> 原文：[an article about locks and thread safety in Swift](https://www.mikeash.com/pyblog/friday-qa-2015-02-06-locks-thread-safety-and-swift.html)　·　mikeash.com Friday Q&A

Posted at 2015-02-06 14:23 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2015-02-20: Let's Build @synchronized](https://www.mikeash.com/pyblog/friday-qa-2015-02-20-lets-build-synchronized.html)  
Previous article: [Friday Q&A 2015-01-23: Let's Build Swift Notifications](https://www.mikeash.com/pyblog/friday-qa-2015-01-23-lets-build-swift-notifications.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [swift](https://www.mikeash.com/pyblog/?tag=swift) [threading](https://www.mikeash.com/pyblog/?tag=threading)

Friday Q&A 2015-02-06: Locks, Thread Safety, and Swift

by [Mike Ash](https://www.mikeash.com/)

This article is also available in [Bosnian (translation by Vlada Catalic)](http://vladacatalic.com/locks-thread-safety-and-swift/) and [Macedonian (translation by Vlada Catalic)](http://balkanscience.com/locks-thread-safety-and-swift/).

**A Quick Recap on Locks**  
A lock, or mutex, is a construct that ensures only one thread is active in a given region of code at any time. They're typically used to ensure that multiple threads accessing a mutable data structure all see a consistent view of it. There are several kinds of locks:

1. Blocking locks sleep a thread while it waits for another thread to release the lock. This is the usual behavior.
2. Spinlocks use a busy loop to constantly check to see if a lock has been released. This is more efficient if waiting is rare, but wastes CPU time if waiting is common.
3. Reader/writer locks allow multiple "reader" threads to enter a region simultaneously, but exclude all other threads (including readers) when a "writer" thread acquires the lock. This can be useful as many data structures are safe to read from multiple threads simultaneously, but unsafe to write while other threads are either reading or writing.
4. Recursive locks allow a single thread to acquire the same lock multiple times. Non-recursive locks can deadlock, crash, or otherwise misbehave when re-entered from the same thread.

**APIs**  
Apple's APIs have a bunch of different mutex facilities. This is a long but not exhaustive list:

1. `pthread_mutex_t`.
2. `pthread_rwlock_t`.
3. `dispatch_queue_t`.
4. `NSOperationQueue` when configured to be serial.
5. `NSLock`.
6. `OSSpinLock`.

In addition to this, Objective-C provides the `@synchronized` language construct, which at the moment is implemented on top of `pthread_mutex_t`. Unlike the others, `@synchronized` doesn't use an explicit lock object, but rather treats an arbitrary Objective-C object as if it were a lock. A `@synchronized(someObject)` section will block access to any other `@synchronized` sections that use the same object pointer. These different facilities all have different behaviors and capabilities:

1. `pthread_mutex_t` is a blocking lock that can optionally be configured as a recursive lock.
2. `pthread_rwlock_t` is a blocking reader/writer lock.
3. `dispatch_queue_t` can be used as a blocking lock. It can be used as a reader/writer lock by configuring it as a concurrent queue and using barrier blocks. It also supports asynchronous execution of the locked region.
4. `NSOperationQueue` can be used as a blocking lock. Like `dispatch_queue_t` it supports asynchronous execution of the locked region.
5. `NSLock` is blocking lock as an Objective-C class. Its companion class `NSRecursiveLock` is a recursive lock, as the name indicates.
6. `OSSpinLock` is a spinlock, as the name indicates.

Finally, `@synchronized` is a blocking recursive lock.

**Value Types**  
Note that `pthread_mutex_t`, `pthread_rwlock_t`, and `OSSpinLock` are value types, not reference types. That means that if you use `=` on them, you make a copy. This is important, because these types can't be copied! If you copy one of the `pthread` types, the copy will be unusable and may crash when you try to use it. The `pthread` functions that work with these types assume that the values are at the same memory addresses as where they were initialized, and putting them somewhere else afterwards is a bad idea. `OSSpinLock` won't crash, but you get a completely separate lock out of it which is never what you want.

If you use these types, you must be careful never to copy them, whether explicitly with a `=` operator, or implicitly by, for example, embedding them in a `struct` or capturing them in a closure.

Additionally, since locks are inherently mutable objects, this means you need to declare them with `var` instead of `let`.

The others are reference types, meaning they can be passed around at will, and can be declared with `let`.

**Initialization**  
**Update 2015-02-10:** the problems described in this section have been made obsolete with breathtaking speed. Apple released Xcode 6.3b1 yesterday which includes Swift 1.2. Among other changes, C structs are now imported with an empty initializer that sets all fields to zero. In short, you can now write `pthread_mutex_t()` without the extensions I discuss below. This section will remain for historical interest, but is no longer relevant to the language.

The `pthread` types are troublesome to use from Swift. They're defined as opaque `struct`s with a bunch of storage, such as:

```
    struct _opaque_pthread_mutex_t {
        long __sig;
        char __opaque[__PTHREAD_MUTEX_SIZE__];
    };
```

The intent is that you declare them, then initialize them using an `init` function that takes a pointer to the storage and fills it out. In C, it looks like:

```
    pthread_mutex_t mutex;
    pthread_mutex_init(&mutex, NULL);
```

This works fine, as long as you remember to call `pthread_mutex_init`. However, Swift really, really dislikes uninitialized variables. The equivalent Swift fails to compile:

```
    var mutex: pthread_mutex_t
    pthread_mutex_init(&mutex, nil)
    // error: address of variable 'mutex' taken before it is initialized
```

Swift requires variables to be initialized before they're used. `pthread_mutex_init` doesn't use the value of the variable passed in, it just overwrites it, but Swift doesn't know that and so it produces an error. To satisfy the compiler, the variable needs to be initialized with something, but that's harder than it looks. Using `()` after the type doesn't work:

```
    var mutex = pthread_mutex_t()
    // error: missing argument for parameter '__sig' in call
```

Swift requires values for those opaque fields. `__sig` is easy, we can just pass zero. `__opaque` is a bit more annoying. Here's how it gets bridged into Swift:

```
    struct _opaque_pthread_mutex_t {
        var __sig: Int
        var __opaque: (Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8,
                       Int8, Int8, Int8, Int8)
    }
```

There's no easy way to get a big tuple full of zeroes, so you have to write it all out:

```
    var mutex = pthread_mutex_t(__sig: 0,
                             __opaque: (0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0, 0, 0))
```

This is awful, but I couldn't find a good way around it. The best I could do was wrap it up in an extension so that the empty `()` works. Here are the two extensions I made:

```
    extension pthread_mutex_t {
        init() {
            __sig = 0
            __opaque = (0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0)
        }
    }

    extension pthread_rwlock_t {
        init() {
            __sig = 0
            __opaque = (0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0)
        }
    }
```

With these extensions, this works:

```
    var mutex = pthread_mutex_t()
    pthread_mutex_init(&mutex, nil)
```

It may be possible to roll the call to `pthread_mutex_init` into the extension initializer as well, but there's no guarantee that `self` in a `struct` init points to the variable being initialized. Since these values can't be moved in memory after being initialized, I wanted to keep the initialization as a separate call.

**Locking Wrappers**  
To make these different APIs easier to use, I wrote a series of small wrapper functions. I settled on `with` as a convenient, short, syntax-looking name inspired by Python's `with` statement. Swift's function overloading allows using the same name for all these different types. The basic form looks like this:

```
    func with(lock: SomeLockType, f: Void -> Void) { ...
```

This then executes `f` with the lock held. Let's implement it for all these types.

For the value types, it needs to take a pointer to the lock so the lock/unlock functions can modify it. The implementation for `pthread_mutex_t` just calls the appropriate lock and unlock functions, with a call to `f` in between:

```
    func with(mutex: UnsafeMutablePointer<pthread_mutex_t>, f: Void -> Void) {
        pthread_mutex_lock(mutex)
        f()
        pthread_mutex_unlock(mutex)
    }
```

The implementation for `pthread_rwlock_t` is almost identical:

```
    func with(rwlock: UnsafeMutablePointer<pthread_rwlock_t>, f: Void -> Void) {
        pthread_rwlock_rdlock(rwlock)
        f()
        pthread_rwlock_unlock(rwlock)
    }
```

I made a companion to this one that takes a write lock, which again looks much the same:

```
    func with_write(rwlock: UnsafeMutablePointer<pthread_rwlock_t>, f: Void -> Void) {
        pthread_rwlock_wrlock(rwlock)
        f()
        pthread_rwlock_unlock(rwlock)
    }
```

The one for `dispatch_queue_t` is even simpler. It's just a wrapper around `dispatch_sync`:

```
    func with(queue: dispatch_queue_t, f: Void -> Void) {
        dispatch_sync(queue, f)
    }
```

In fact, if one were too clever for one's own good and wanted to confuse people, one could take advantage of the functional nature of Swift and simply write:

```
    let with = dispatch_sync
```

This is unwise for a couple of reasons, not the least of which being that it messes with the type-based overloading we're trying to use here.

`NSOperationQueue` is conceptually similar, but there's no direct equivalent to `dispatch_sync`. Instead, we create an operation, add it to the queue, and explicitly wait for it to finish:

```
    func with(opQ: NSOperationQueue, f: Void -> Void) {
        let op = NSBlockOperation(f)
        opQ.addOperation(op)
        op.waitUntilFinished()
    }
```

The implementation for `NSLock` looks like the `pthread` versions, just with slightly different locking calls:

```
    func with(lock: NSLock, f: Void -> Void) {
        lock.lock()
        f()
        lock.unlock()
    }
```

Finally, the `OSSpinLock` implementation is again more of the same:

```
    func with(spinlock: UnsafeMutablePointer<OSSpinLock>, f: Void -> Void) {
        OSSpinLockLock(spinlock)
        f()
        OSSpinLockUnlock(spinlock)
    }
```

**Imitating @synchronized**  
With these wrappers, imitating the basics of `@synchronized` is fairly simple. Add a property to your class that holds a lock, then use `with` where you would have used `@synchronized` before:

```
    let queue = dispatch_queue_create("com.example.myqueue", nil)

    func setEntryForKey(key: Key, entry: Entry) {
        with(queue) {
            entries[key] = entry
        }
    }
```

Getting data out of the block is a bit less pleasant, unfortunately. While `@synchronized` lets you `return` from within, that doesn't work with `with`. Instead, you have to use a `var` and assign to it within the block:

```
    func entryForKey(key: Key) -> Entry? {
        var result: Entry?
        with(queue) {
            result = entries[key]
        }
        return result
    }
```

It should be possible to wrap the boilerplate in a generic function, but I had trouble getting the Swift compiler's type inference to play along and don't have a solution just yet.

**Imitating Atomic Properties**  
Atomic properties are not often useful. The problem is that, unlike many other useful properties of code, atomicity doesn't compose. For example, if function `f` doesn't leak memory, and function `g` doesn't leak memory, then function `h` that just calls `f` and `g` also doesn't leak memory. The same is not true of atomicity. For an example, imagine you have a set of atomic, thread-safe `Account` classes:

```
    let checkingAccount = Account(amount: 100)
    let savingsAccount = Account(amount: 0)
```

Now you move the money to savings:

```
    checkingAccount.withDraw(100)
    savingsAccount.deposit(100)
```

In another thread, you total up the balance and tell the user:

```
    println("Your total balance is: \(checkingAccount.amount + savingsAccount.amount)")
```

If this runs at just the wrong time, it will print zero instead of 100, despite the fact that the `Account` objects themselves are fully atomic and the user had a balance of 100 the whole time. Because of this, it's usually better to build entire subsystems to be atomic, rather than individual properties.

There are rare cases where atomic properties are useful, because it really is a standalone thing that just needs to be thread safe. To achieve that in Swift, you need a computed property that will do the locking, and a second normal property that will actually hold the value:

```
    private let queue = dispatch_queue_create("...", nil)
    private var _myPropertyStorage: SomeType

    var myProperty: SomeType {
        get {
            var result: SomeType?
            with(queue) {
                result = _myPropertyStorage
            }
            return result!
        }
        set {
            with(queue) {
                _myPropertyStorage = newValue
            }
        }
    }
```

**Choosing Your Lock API**  
The `pthread` APIs can be discounted immediately due to the difficulty of using them from Swift, and the fact that they don't do anything that other APIs don't also do. I often like to use them in C and Objective-C because they're fairly straightforward and fast, but it's not worth it here unless something really requires it.

Reader/writer locks are mostly not worth worrying about. For common cases, where reads and writes are quick, the extra overhead used by a reader/writer lock outweighs the ability to have multiple concurrent readers.

Recursive locks are mostly an invitation to deadlock. There are cases where they're useful, but if you find yourself with a design where you need to take a lock that's already locked on the current thread, that's a good sign you should _probably_ rethink it so that's not necessary.

My opinion is that, when in doubt, default to `dispatch_queue_t`. They're more heavyweight, but this rarely matters. The API is reasonably convenient, and they ensure you never forget to pair a lock call with an unlock call. They provide a ton of nice facilities that can come in handy, like the ability to use a single `dispatch_async` call to run locked code in the background, or the ability to set up timers or other event sources targeted directly at the queue so that they automatically execute locked. You can even use it as a target for things like `NSNotificationCenter` observers and `NSURLSession` delegates by using the `underlyingQueue` property of `NSOperationQueue`, new in OS X 10.10 and iOS 8.

`NSOperationQueue` wishes it could be as cool as `dispatch_queue_t` and there are few if any reasons to use it as a lock API. It's more cumbersome to use and doesn't provide any advantages for typical use as a locking API, although the automatic dependency management for operations can sometimes be useful in other contexts.

`NSLock` is a simple locking class that's easy to use and reasonably fast. It's a good choice if you want explicit lock and unlock calls for some reason, rather than the blocks-based API of `dispatch_queue_t`, but there's little reason to use it in most cases.

`OSSpinLock` is an excellent choice for uses where the lock is taken often, contention is low, and the locked code runs quickly. It has much lower overhead and this helps performance for hot code paths. On the other hand, it's a bad choice for uses where code may hold the lock for a substantial amount of time, or contention is common, as it will waste CPU time. In general, default to `dispatch_queue_t`, but keep `OSSpinLock` in mind as a fairly easy optimization if it starts to show up in the profiler.

**Conclusion**  
Swift has no language facilities for thread synchronization, but this deficiency is more than made up for the wealth of locking APIs available in Apple's frameworks. GCD and `dispatch_queue_t` are still a masterpiece and the API works great in Swift. We don't have `@synchronized` or atomic properties, but we have things that are better.

That's it for today. Come back next time for more exciting adventures. Friday Q&A is built on the topic suggestions of readers like you, so if you have something you'd like to see covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

[Comments RSS feed for this page](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2015-02-06-locks-thread-safety-and-swift.html)

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
