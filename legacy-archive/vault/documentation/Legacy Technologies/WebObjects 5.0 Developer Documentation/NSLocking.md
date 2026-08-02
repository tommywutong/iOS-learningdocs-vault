---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Interfaces/NSLocking.html
archived_at: '2026-07-15T08:13:56.866953Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSLocking

> **__Package:__**
> : com.webobjects.foundation

---

## Interface Description

---

The NSLocking protocol declares the elementary methods adopted by classes that define lock objects. A lock object is used to coordinate the actions of multiple threads of execution within a single application. By using a lock object, an application can protect critical sections of code from being executed simultaneously by separate threads, thus protecting shared data and other shared resources from corruption.

For example, consider a multithreaded application in which each thread updates a shared counter. If two threads simultaneously fetch the current value into local storage, increment it, and then write the value back, the counter will be incremented only once, losing one thread's contribution. However, if the code that manipulates the shared data (the critical section of code) must be locked before being executed, only one thread at a time can perform the updating operation, and collisions are prevented.

A lock object is either locked or unlocked. You acquire a lock by sending the object a lock message, thus putting the object in the locked state. You relinquish a lock by sending an unlock message, and thus putting the object in the unlocked state. (The Foundation classes that adopt this protocol define additional ways to acquire and relinquish locks.)

The lock method as declared in this protocol is blocking. That is, the thread that sends a lock message is blocked from further execution until the lock is acquired (presumably because some other thread relinquishes its lock). Classes that adopt this protocol typically add methods that offer nonblocking alternatives.

These Foundation classes conform to the NSLocking protocol:

|  |  |
| --- | --- |
| __Class__ | __Adds these features to the basic protocol__ |
| NSLock | A nonblocking lock method; the ability to limit the duration of a locking attempt. |
| NSMultiReaderLock | The ability for multiple threads to acquire the lock for reading while allowing only a single thread to acquire the lock for writing. |
| NSRecursiveLock | The ability for a single thread to acquire a lock more than once without deadlocking. |

These classes use a locking mechanism that causes a thread to sleep while waiting to acquire a lock rather than to poll the system constantly. Thus, lock objects can be used to lock time-consuming operations without causing system performance to degrade. See the class specifications for these classes for further information on their behavior and usage.

Java also has a locking mechanism, which is based on the `synchronized` keyword. In certain cases, you may want to use the Foundation locking classes instead:

- The Foundation classes have extra features that are not supported by the `synchronized` locking mechanism like nonblocking lock methods.
- Foundation locking objects can coordinate the locking of many objects at the same time, unlike the `synchronized` locking mechanism, which can lock only a single method, class, or instance at a time.
- These locking classes were available in previous versions of WebObjects. You may encounter these classes if you are porting older applications to this version of WebObjects.

## Constants

NSLocking defines the following constants to simplify locking method invocations that take time intervals as parameters.

|  |  |  |
| --- | --- | --- |
| __Constant__ | __Type__ | __Description__ |
| OneSecond | `long` | Number of milliseconds in one second |
| OneMinute | `long` | Number of milliseconds in one minute |
| OneHour | `long` | Number of milliseconds in one hour |
| OneDay | `long` | Number of milliseconds in one day |
| OneWeek | `long` | Number of milliseconds in one week |
| OneYear | `long` | Number of milliseconds in one year (defined as 365.2425 days) |
| OneCentury | `long` | Number of milliseconds in one century |

## Method Types

---

> **All methods**
>
> : [lock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjrxwg23jnzts63dpmnvq): [unlock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjrxwg23jnzts65lonrxwg2y)

## Instance Methods

---

### lock

`public void lock()`

Attempts to acquire a lock. This method blocks a thread's execution until the lock can be acquired.

An application protects a critical section of code by requiring a thread to acquire a lock before executing the code. Once the critical section is past, the thread relinquishes the lock by invoking unlock.

---

### unlock

`public void unlock()`

Relinquishes a previously acquired lock.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
