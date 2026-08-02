---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSLock.html
archived_at: '2026-07-15T08:13:56.116980Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSLock

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : NSLocking

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

An NSLock object is used to coordinate the operation of multiple threads of execution within the same application. An NSLock object can be used to mediate access to an application's global data or to protect a critical section of code, allowing it to run atomically.

An NSLock object represents a lock that can be acquired by only a single thread at a time. While one thread holds the lock, any other thread is prevented from doing so until the owner relinquishes the lock. An application can have multiple NSLock objects, each protecting different sections of code. It's safest to create all of the locks before the application becomes multi-threaded, to avoid race conditions. If you want to create additional locks after the application becomes multi-threaded, you should create the new lock inside a critical code section that is itself protected by an existing lock.

The basic interface to NSLock is declared by the [NSLocking](NSLocking.md#apple-ineegssbi5euk) interface, which defines the [lock](NSLocking.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjrxwg23jnzts63dpmnvq) and [unlock](NSLocking.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjrxwg23jnzts65lonrxwg2y) methods. To this base, NSLock adds the [tryLock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwg2zporzhstdpmnvq) methods. Whereas the [lock](NSLocking.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjrxwg23jnzts63dpmnvq) method declared in the interface doesn't return until it is successful, the methods declared in this class add more flexible means of acquiring a lock.

An NSLock could be used to coordinate the updating of a visual display shared by a number of threads involved in a single calculation:

> ```
> boolean moreToDo = true;
> NSLock myLock = new NSLock();
> ...
> while (moreToDo) {
>     /* Do another increment of calculation */
>     /* until there's no more to do. */
>     if (myLock.tryLock()) {
>         /* Update display used by all threads. */
>         myLock.unlock();
>     }
> }
> ```

The NSLock, NSMultiReaderLock, and NSRecursiveLock classes all adopt the NSLocking protocol and offer various additional features and performance characteristics. See the NSMultiReaderLock and NSRecursiveLock class descriptions for more information.

## Method Types

---

> **Constructors**
>
> : [NSLock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwg2zpjzjuy33dnm)
>
> **Instance methods**
>
> : [lock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwg2zpnrxwg2y): [lockBeforeDate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwg2zpnrxwg22cmvtg64tfirqxizi): [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwg2zporxvg5dsnfxgo): [tryLock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwg2zporzhstdpmnvq): [unlock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjrxwg2zpovxgy33dnm)

## Constructors

---

### NSLock

`public NSLock()`

Creates an NSLock object.

---

## Instance Methods

---

### lock

`public synchronized void lock()`

Conformance to [NSLocking](NSLocking.md#apple-ineegssbi5euk). See the method description of [lock](NSLocking.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjrxwg23jnzts63dpmnvq) in the interface specification for NSLocking.

---

### lockBeforeDate

`public boolean lockBeforeDate(NSTimestamp timestamp)`

This method is deprecated. Use `tryLock(NSTimestamp timestamp)` instead.

---

### toString

`public String toString()`

Returns a string representation of the receiver indicating whether or not the lock is taken.

---

### tryLock

`public synchronized boolean tryLock()`

Attempts to acquire a lock. Returns immediately, with a value of `true` if successful and `false` otherwise.

`public synchronized boolean tryLock(long msec)`

Attempts to acquire a lock for _msec_ milliseconds. The thread is blocked until the receiver acquires the lock or _msec_ milliseconds have passed. Returns `true` if the lock is acquired within this time limit. Returns `false` if the time limit expires before a lock can be acquired.

`public boolean tryLock(NSTimestamp timestamp)`

Attempts to acquire a lock until the time specified by _timestamp_. The thread is blocked until the receiver acquires the lock or _timestamp_ is reached. Returns `true` if the lock is acquired within this time limit. Returns `false` if the time limit expires before a lock can be acquired.

---

### unlock

`public synchronized void unlock()`

Conformance to [NSLocking](NSLocking.md#apple-ineegssbi5euk). See the method description of [unlock](NSLocking.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjrxwg23jnzts65lonrxwg2y) in the interface specification for NSLocking.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
