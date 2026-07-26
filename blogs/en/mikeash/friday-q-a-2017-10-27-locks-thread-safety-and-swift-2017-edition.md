---
title: 'Friday Q&A 2017-10-27: Locks, Thread Safety, and Swift: 2017 Edition'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2017-10-27-locks-thread-safety-and-swift-2017-edition.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2a655cff4076eb77'
translated: false
---

> 原文：[Friday Q&A 2017-10-27: Locks, Thread Safety, and Swift: 2017 Edition](https://www.mikeash.com/pyblog/friday-qa-2017-10-27-locks-thread-safety-and-swift-2017-edition.html)　·　mikeash.com Friday Q&A

Posted at 2017-10-27 11:28 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2017-11-10: Observing the A11's Heterogenous Cores](https://www.mikeash.com/pyblog/friday-qa-2017-11-10-observing-the-a11s-heterogenous-cores.html)  
Previous article: [The Complete Friday Q&A Volumes II and III Are Out!](https://www.mikeash.com/pyblog/the-complete-friday-qa-volumes-ii-and-iii-are-out.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [swift](https://www.mikeash.com/pyblog/?tag=swift) [threading](https://www.mikeash.com/pyblog/?tag=threading)

Friday Q&A 2017-10-27: Locks, Thread Safety, and Swift: 2017 Edition

by [Mike Ash](https://www.mikeash.com/)

This article is also available in [Chinese (translation by 李孛)](http://kylinroc.github.io/friday-qa-2017-10-27-locks-thread-safety-and-swift-2017-edition.html).

This article will repeat some material from the old one, with changes to bring it up to date, and some discussion of how things have changed. Reading the previous article is not necessary before you read this one.

**A Quick Recap on Locks**  
A lock, or mutex, is a construct that ensures only one thread is active in a given region of code at any time. They're typically used to ensure that multiple threads accessing a mutable data structure all see a consistent view of it. There are several kinds of locks:

1. Blocking locks sleep a thread while it waits for another thread to release the lock. This is the usual behavior.
2. Spinlocks use a busy loop to constantly check to see if a lock has been released. This is more efficient if waiting is rare, but wastes CPU time if waiting is common.
3. Reader/writer locks allow multiple "reader" threads to enter a region simultaneously, but exclude all other threads (including readers) when a "writer" thread acquires the lock. This can be useful as many data structures are safe to read from multiple threads simultaneously, but unsafe to write while other threads are either reading or writing.
4. Recursive locks allow a single thread to acquire the same lock multiple times. Non-recursive locks can deadlock, crash, or otherwise misbehave when re-entered from the same thread.

**APIs**  
Apple's APIs have a bunch of different mutex facilities. This is a long but not exhaustive list:

1. .
2. .
3. .
4. when configured to be serial.
5. .
6. .

In addition to this, Objective-C provides the `@synchronized` language construct, which at the moment is implemented on top of `pthread_mutex_t`. Unlike the others, `@synchronized` doesn't use an explicit lock object, but rather treats an arbitrary Objective-C object as if it were a lock. A `@synchronized(someObject)` section will block access to any other `@synchronized` sections that use the same object pointer. These different facilities all have different behaviors and capabilities:

1. is a blocking lock that can optionally be configured as a recursive lock.
2. is a blocking reader/writer lock.
3. can be used as a blocking lock. It can be used as a reader/writer lock by configuring it as a concurrent queue and using barrier blocks. It also supports asynchronous execution of the locked region.
4. can be used as a blocking lock. Like

  it supports asynchronous execution of the locked region.
5. is blocking lock as an Objective-C class. Its companion class

  is a recursive lock, as the name indicates.
6. is a less sophisticated, lower-level blocking lock.

Finally, `@synchronized` is a blocking recursive lock.

**Spinlocks, Lack of**  
I mentioned spinlocks as one type of lock, but none of the APIs listed here are spinlocks. This is a big change from the previous article, and is the main reason I'm writing this update.

Spinlocks are really simple, and are efficient in the right circumstances. Unfortunately, they're a little too simple for the complexities of the modern world.

The problem is thread priorities. When there are more runnable threads than CPU cores, higher priority threads get preference. This is a useful notion, because CPU cores are always a limited resource, and you don't want some time-insensitive background network operation stealing time from your UI while the user is trying to use it.

When a high-priority thread gets stuck and has to wait for a low-priority thread to finish some work, but the high-priority thread prevents the low-priority thread from actually performing that work, it can result in long hangs or even a permanent deadlock.

The deadlock scenario looks like this, where H is a high-priority thread and L is a low-priority thread:

1. L acquires the spinlock.
2. L starts doing some work.
3. H becomes ready to run, and preempts L.
4. H attempts to acquire the spinlock, but fails, because L still holds it.
5. H begins angrily spinning on the spinlock, repeatedly trying to acquire it, and monopolizing the CPU.
6. H can't proceed until L finishes its work. L can't finish its work unless H stops angrily spinning on the spinlock.
7. Sadness.

There are ways to solve this problem. For example, H might donate its priority to L in step 4, allowing L to complete its work in a timely fashion. It's possible to make a spinlock that solves this problem, but Apple's old spinlock API, `OSSpinLock`, doesn't.

This was fine for a long time, because thread priorities didn't get much use on Apple's platforms, and the priority system used dynamic priorities that kept the deadlock scenario from persisting too long. More recently, [quality of service classes](https://developer.apple.com/library/content/documentation/Performance/Conceptual/EnergyGuide-iOS/PrioritizeWorkWithQoS.html) made different priorities more common, and made the deadlock scenario more likely to persist.

`OSSpinLock`, which did a fine job for so long, stopped being a good idea with the release of iOS 8 and macOS 10.10. It's now been formally deprecated. The replacement is `os_unfair_lock`, which fills the same overall purpose as a low-level, unsophisticated, cheap lock, but is sufficiently sophisticated to avoid problems with priorities.

**Value Types**  
Note that `pthread_mutex_t`, `pthread_rwlock_t`, and `os_unfair_lock` are value types, not reference types. That means that if you use `=` on them, you make a copy. This is important, because these types can't be copied! If you copy one of the `pthread` types, the copy will be unusable and may crash when you try to use it. The `pthread` functions that work with these types assume that the values are at the same memory addresses as where they were initialized, and putting them somewhere else afterwards is a bad idea. `os_unfair_lock` won't crash, but you get a completely separate lock out of it which is never what you want.

If you use these types, you must be careful never to copy them, whether explicitly with a `=` operator, or implicitly by, for example, embedding them in a `struct` or capturing them in a closure.

Additionally, since locks are inherently mutable objects, this means you need to declare them with `var` instead of `let`.

The others are reference types, meaning they can be passed around at will, and can be declared with `let`.

**Initialization**  
You must be careful with the `pthread` locks, because you can create a value using the empty `()` initializer, but that value won't be a valid lock. These locks must be separately initialized using `pthread_mutex_init` or `pthread_rwlock_init`:

```
    var mutex = pthread_mutex_t()
    pthread_mutex_init(&mutex, nil)
```

It's tempting to write an extension on these types which wraps up the initialization. However, there's no guarantee that initializers work on the variable directly, rather than on a copy. Since these types can't be safely copied, such an extension can't be safely written unless you have it return a pointer or a wrapper class.

If you use these APIs, don't forget to call the corresponding `destroy` function when it's time to dispose of the lock.

**Use**  
`DispatchQueue` has a callback-based API which makes it natural to use it safely. Depending on whether you need the protected code to run synchronously or asynchronously, call `sync` or `async` and pass it the code to run:

```
    queue.sync(execute: { ... })
    queue.async(execute: { ... })
```

For the `sync` case, the API is nice enough to capture the return value from the protected code and provide it as the return value of the `sync` method:

```
    let value = queue.sync(execute: { return self.protectedProperty })
```

You can even `throw` errors inside the protected block and they'll propagate out.

`OperationQueue` is similar, although it doesn't have a built-in way to propogate return values or errors. You'll have to build that yourself, or use `DispatchQueue` instead.

The other APIs require separate locking and unlocking calls, which can be exciting when you forget one of them. The calls look like this:

```
    pthread_mutex_lock(&mutex)
    ...
    pthread_mutex_unlock(&mutex)

    nslock.lock()
    ...
    nslock.unlock()

    os_unfair_lock_lock(&lock)
    ...
    os_unfair_lock_unlock(&lock)
```

Since the APIs are virtually identical, I'll use `nslock` for further examples. The others are the same, but with different names.

When the protected code is simple, this works well. But what if it's more complicated? For example:

```
    nslock.lock()
    if earlyExitCondition {
        return nil
    }
    let value = compute()
    nslock.unlock()
    return value
```

Oops, sometimes you don't unlock the lock! This is a good way to make hard-to-find bugs. Maybe you're always disciplined with your `return` statements and never do this. What if you throw an error?

```
    nslock.lock()
    guard something else { throw error }
    let value = compute()
    nslock.unlock()
    return value
```

Same problem! Maybe you're really disciplined and would never do this either. Then you're safe, but even then the code is a bit ugly:

```
    nslock.lock()
    let value = compute()
    nslock.unlock()
    return value
```

The obvious fix for this is to use Swift's `defer` mechanism. The moment you lock, defer the unlock. Then no matter how you exit the code, the lock will be released:

```
    nslock.lock()
    defer { nslock.unlock() }
    return compute()
```

This works for early returns, throwing errors, or just normal code.

It's still annoying to have to write two lines, so we can wrap everything up in a callback-based function like `DispatchQueue` has:

```
    func withLocked<T>(_ lock: NSLock, _ f: () throws -> T) rethrows -> T {
        lock.lock()
        defer { lock.unlock() }
        return try f()
    }

    let value = withLocked(lock, { return self.protectedProperty })
```

When implementing this for value types, you'll need to be sure to take a _pointer_ to the lock rather than the lock itself. Remember, you don't want to copy these things! The `pthread` version would look like this:

```
    func withLocked<T>(_ mutexPtr: UnsafeMutablePointer<pthread_mutex_t>, _ f: () throws -> T) rethrows -> T {
        pthread_mutex_lock(mutexPtr)
        defer { pthread_mutex_unlock(mutexPtr) }
        return try f()
    }

    let value = withLocked(&mutex, { return self.protectedProperty })
```

**Choosing Your Lock API**  
`DispatchQueue` is an obvious favorite. It has a nice Swifty API and is pleasant to use. The Dispatch library gets a huge amount of attention from Apple, and that means that it can be counted on to perform well, work reliably, and get lots of cool new features.

`DispatchQueue` allows for a lot of nifty advanced uses, such as scheduling timers or event sources to fire directly on the queue you're using as a lock, ensuring that the handlers are synchronized with other things using the queue. The ability to set target queues allows expressing complex lock hierarchies. Custom concurrent queues can be easily used as reader-writer locks. You only have to change a single letter to execute protected code asynchronously on a background thread rather than synchronously. And the API is easy to use and hard to misuse. It's a win all around. There's a reason GCD quickly became one of my favorite APIs, and remains one to this day.

Like most things, it's not perfect. A dispatch queue is represented by an object in memory, so there's a bit of overhead. They're missing some niche features, like condition variables or recursiveness. Every once in a great while, it's useful to be able to make individual lock and unlock calls rather than be forced to use a callback-based API. `DispatchQueue` is usually the right choice, and is a great default if you don't know what to pick, but there are occasionally reasons to use others.

`os_unfair_lock` can be a good choice when per-lock overhead is important (because for some reason you have a huge number of them) and you don't need fancy features. It's implemented as a single 32-bit integer which you can place wherever you need it, so overhead is small.

As the name hints, one of the features that `os_unfair_lock` is missing is fairness. Lock fairness means that there's at least some attempt to ensure that different threads waiting on a lock all get a chance to acquire it. Without fairness, it's possible for a thread that rapidly releases and re-acquires the lock to monopolize it while other threads are waiting.

Whether or not this is a problem depends on what you're doing. There are some use cases where fairness is necessary, and some where it doesn't matter at all. The lack of fairness allows `os_unfair_lock` to have better performance, so it can provide an edge in cases where fairness isn't needed.

`pthread_mutex` is somewhere in the middle. It's considerably larger than `os_unfair_lock`, at 64 bytes, but you can still control where it's stored. It implements fairness, although this is a detail of Apple's implementation, not part of the API spec. It also provides various other advanced features, such as the ability to make the mutex recursive, and fancy thread priority stuff.

`pthread_rwlock` provides a reader/writer lock. It takes up a whopping 200 bytes and doesn't provide much in the way of interesting features, so there doesn't seem to be much reason to use it over a concurrent `DispatchQueue`.

`NSLock` is a wrapper around `pthread_mutex`. It's hard to come up with a use case for this, but it could be useful if you need explicit lock/unlock calls but don't want the hassle of manually initializing and destroying a `pthread_mutex`.

`OperationQueue` offers callback-based API like `DispatchQueue`, with some advanced features for things like dependency management between operations, but without many of the other features offered by `DispatchQueue`. There is little reason to use `OperationQueue` as a locking API, although it can be useful for other things.

In short: `DispatchQueue` is probably the right choice. In certain circumstances, `os_unfair_lock` may be better. The others are usually not the ones to use.

**Conclusion**  
Swift has no language facilities for thread synchronization, but the APIs make up for it. GCD remains one of Apple's crown jewels, and the Swift API for it is great. For the rare occasions where it's not suitable, there are many other options to choose from. We don't have `@synchronized` or atomic properties, but we have things that are better.

That wraps it up for this time. Check back again for more fun stuff. If you get bored in the meantime, [buy one of my books!](https://www.mikeash.com/book.html) Friday Q&A is driven by reader ideas, so if you have a topic you'd like to see covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
