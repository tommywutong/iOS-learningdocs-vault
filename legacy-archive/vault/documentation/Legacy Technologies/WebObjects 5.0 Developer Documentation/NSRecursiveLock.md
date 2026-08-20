---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSRecursiveLock.html
archived_at: '2026-07-15T08:13:56.484433Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSRecursiveLock

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : NSLocking

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

NSRecursiveLock defines a lock that may be acquired multiple times by the same thread without causing a deadlock, a situation where a thread is permanently blocked waiting for itself to relinquish a lock. While the locking thread has one or more locks, all other threads are prevented from accessing the code protected by the lock. Here's an example where a recursive lock functions properly but other lock types would deadlock:

> ```
> NSRecursiveLock theLock = new NSRecursiveLock();
> ...
> theLock.lock();
> /* lengthy operations involving global data */
> theLock.lock();   /* possibly invoked in a subroutine */
> ...
> theLock.unlock(); /* relinquishes most recent lock */
> ...
> theLock.unlock(); /* relinquishes the first lock */
> ```

Unless _theLock_ was an NSRecursiveLock, a deadlock condition would occur at the second __lock__ message in the example above.

The NSRecursiveLock object keeps track of the recursion count: the number of lock requests that the owning thread has made and not unlocked. This is also the number of times unlock must be invoked to return the lock. To access the recursion count, use the [recursionCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjswg5lsonuxmzkmn5rwwl3smvrxk4ttnfxw4q3povxhi) method.

The NSLock, NSMultiReaderLock, and NSRecursiveLock classes all adopt the NSLocking protocol and offer various additional features and performance characteristics. See the NSLock and NSMultiReaderLock class descriptions for more information.

## Method Types

---

> **Constructors**
>
> : [NSRecursiveLock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjswg5lsonuxmzkmn5rwwl2oknjgky3vojzws5tfjrxwg2y)
>
> **Instance methods**
>
> : [lock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjswg5lsonuxmzkmn5rwwl3mn5rww): [tryLock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjswg5lsonuxmzkmn5rwwl3uoj4uy33dnm): [lockBeforeDate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjswg5lsonuxmzkmn5rwwl3mn5rwwqtfmzxxezkemf2gk): [recursionCount](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjswg5lsonuxmzkmn5rwwl3smvrxk4ttnfxw4q3povxhi): [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjswg5lsonuxmzkmn5rwwl3un5jxi4tjnztq): [unlock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjswg5lsonuxmzkmn5rwwl3vnzwg6y3l)

## Constructors

---

### NSRecursiveLock

`public NSRecursiveLock()`

Creates an NSRecursiveLock.

---

## Instance Methods

---

### lock

`public void lock()`

Conformance to [NSLocking](NSLocking.md#apple-ineegssbi5euk). See the method description of [lock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstkjswg5lsonuxmzkmn5rwwl3mn5rww) in the interface description for NSLocking. If the current thread already owns the lock, this method increments the recursion count.

---

### lockBeforeDate

`public boolean lockBeforeDate(NSTimestamp timestamp)`

This method is deprecated. Use `tryLock(NSTimestamp timestamp)` instead.

---

### recursionCount

`public synchronized long recursionCount()`

Returns the receiver's recursion count (the number of unlocks needed to return the lock) if the current thread owns the lock. If the current thread is not the owner of the lock, returns zero.

---

### toString

`public String toString()`

Returns a string representation of the receiver that includes the thread that owns it and its recursion count.

---

### tryLock

`public boolean tryLock()`

Attempts to acquire a lock. If the lock is not already taken by another thread, acquires the lock, sets the recursion count to 1 and returns `true`. If the current thread owns the lock, increments the recursion count and returns with a value of `true`. If the another thread owns the lock, returns `false` immediately.

`public boolean tryLock(long msec)`

Attempts to acquire a lock for _msec_ milliseconds. If the current thread owns the lock, increments the recursion count and returns `true`. Otherwise, the thread is blocked until the receiver acquires the lock or _msec_ milliseconds have passed. Returns `true` if the lock is acquired within this time limit. Returns `false` if the time limit expires before a lock can be acquired.

`public boolean tryLock(NSTimestamp timestamp)`

Attempts to acquire a lock until the time specified by _timestamp_. If the current thread owns the lock, increments the recursion count and returns `true`. Otherwise, the thread is blocked until the receiver acquires the lock or _timestamp_ is reached. Returns `true` if the lock is acquired within this time limit. Returns `false` if the time limit expires before a lock can be acquired.

---

### unlock

`public synchronized void unlock()`

`public synchronized void unlock(long levels)`

Decrements the recursion count by _levels_ (decrements the recursion count by one in the no-argument version). If the resulting recursion level is zero, returns the lock. This method throws an Error if the thread that invokes it is not the lock's owner. Invoking this method when the lock count is zero does nothing.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
