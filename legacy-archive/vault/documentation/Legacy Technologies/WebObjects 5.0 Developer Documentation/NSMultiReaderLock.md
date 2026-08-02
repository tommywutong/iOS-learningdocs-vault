---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/FoundationRef/Java/Classes/NSMultiReaderLock.html
archived_at: '2026-07-15T08:13:56.196250Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md) 

# NSMultiReaderLock

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : NSLocking

> **__Package:__**
> : com.webobjects.foundation

---

## Class Description

---

The NSMultiReaderLock class provides __reader__ and __writer locks__. The locks are recursive; a single thread can request a lock many times, but a lock is actually taken only on the first request. Likewise, when a thread indicates it's finished with a lock, it takes an equal number of __unlock...__ invocations to return the lock.

There's no limit on the number of reader locks that a process can take. However, there can only be one writer lock at a time, and a writer lock is not issued until all reader locks are returned. Reader locks aren't issued to new threads when there is a thread waiting for a writer lock, but threads that already have a reader lock can increment their lock count.

NSMultiReaderLock correctly handles promotion of a reader lock to a writer lock, and the extension of a reader lock to the current writer. This prevents a thread from deadlocking on itself when requesting a combination of lock types.

NSMultiReaderLocks are slightly more time-expensive than [NSRecursiveLock](NSRecursiveLock.md#apple-inbekrkkjffem)s because the recursion count has to be stored per-thread, causing each request for a reader lock to incur at least one hash lookup. Writer locks are even more expensive because NSMultiReaderLock must poll the hashtable until all reader locks have been returned before the writer lock can be taken.

## Method Types

---

> **Constructors**
>
> : [NSMultiReaderLock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2wy5djkjswczdfojgg6y3lf5hfgtlvnr2gsutfmfsgk4smn5rww)
>
> **Managing reader locks**
>
> : [lockForReading](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2wy5djkjswczdfojgg6y3lf5wg6y3lizxxeutfmfsgs3th): [retrieveReaderLocks](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2wy5djkjswczdfojgg6y3lf5zgk5dsnfsxmzksmvqwizlsjrxwg23t): [suspendReaderLocks](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2wy5djkjswczdfojgg6y3lf5zxk43qmvxgiutfmfsgk4smn5rww4y): [tryLockForReading](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2wy5djkjswczdfojgg6y3lf52he6kmn5rwwrtpojjgkylenfxgo): [unlockForReading](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2wy5djkjswczdfojgg6y3lf52w43dpmnvum33skjswczdjnztq)
>
> **Managing writer locks**
>
> : [lock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2wy5djkjswczdfojgg6y3lf5wg6y3l): [lockForWriting](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2wy5djkjswczdfojgg6y3lf5wg6y3lizxxev3snf2gs3th): [tryLockForWriting](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2wy5djkjswczdfojgg6y3lf52he6kmn5rwwrtpojlxe2lunfxgo): [unlock](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2wy5djkjswczdfojgg6y3lf52w43dpmnvq): [unlockForWriting](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2wy5djkjswczdfojgg6y3lf52w43dpmnvum33sk5zgs5djnztq)
>
> **Methods inherited from Object**
>
> : [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2wy5djkjswczdfojgg6y3lf52g6u3uojuw4zy)

## Constructors

---

### NSMultiReaderLock

`public NSMultiReaderLock()`

Creates an NSMultiReaderLock object.

---

## Instance Methods

---

### lock

`public void lock()`

Conformance to [NSLocking](NSLocking.md#apple-ineegssbi5euk). See the method description of [lock](NSLocking.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjrxwg23jnzts63dpmnvq) in the interface description for NSLocking. This method is equivalent to [lockForWriting](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2wy5djkjswczdfojgg6y3lf5wg6y3lizxxev3snf2gs3th).

---

### lockForReading

`public void lockForReading()`

Acquires a reader lock for the current thread. If the current thread doesn't already have a lock, the method blocks if there are any waiting or active writer locks. If the current thread already has a lock (reader or writer), the lock request count is incremented.

---

### lockForWriting

`public void lockForWriting()`

Gets a writer lock for the current thread. If the current thread already has one, the lock request count is incremented, but a new lock is not taken. If the requesting thread has outstanding reader locks, they are temporarily dropped until the writer lock is returned. If other threads have outstanding reader locks, this method blocks until all reader locks have been freed.

---

### retrieveReaderLocks

`public void retrieveReaderLocks()`

Reinstates the current thread's reader locks that have been suspended using [suspendReaderLocks](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2wy5djkjswczdfojgg6y3lf5zxk43qmvxgiutfmfsgk4smn5rww4y).

---

### suspendReaderLocks

`public void suspendReaderLocks()`

Temporarily relinquishes all of the current thread's reader locks, releasing the lock if all reader locks are unlocked. To reinstate the current thread's suspended reader locks, use the [retrieveReaderLocks](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2wy5djkjswczdfojgg6y3lf5zgk5dsnfsxmzksmvqwizlsjrxwg23t) method.

---

### toString

`public String toString()`

Returns a string representation of the receiver containing the current thread name and a table with the names and reader lock counts of all the receiver's threads.

---

### tryLockForReading

`public boolean tryLockForReading()`

Returns `true` if the current thread is able to immediately obtain a reader lock. There are three ways this can happen:

1. There are no outstanding writer locks.
2. The writer lock is held by the current thread.
3. The current thread already has a reader lock.

This method implicitly calls __lockForReading__, so you must call __unlockForReading__ if __tryLockForReading__ returns `true`.

---

### tryLockForWriting

`public boolean tryLockForWriting()`

Returns `true` if the current thread is able to immediately obtain a writer lock. Returns `false` if another thread already has the lock or is queued to receive it. This method implicitly calls __lockForWriting__, so you must call __unlockForWriting__ if __tryLockForWriting__ returns `true`.

---

### unlock

`public void unlock()`

Conformance to [NSLocking](NSLocking.md#apple-ineegssbi5euk). See the method description of [unlock](NSLocking.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6tstjrxwg23jnzts65lonrxwg2y) in the interface description for NSLocking. This method is equivalent to [unlockForWriting](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6tstjv2wy5djkjswczdfojgg6y3lf52w43dpmnvum33sk5zgs5djnztq).

---

### unlockForReading

`public void unlockForReading()`

Releases a reader lock for the current thread. Each __lockForReading__ message must be paired with an __unlockForReading__ message before the lock is actually released. Invoking this method when the lock count is zero does nothing.

---

### unlockForWriting

`public void unlockForWriting()`

Releases a writer lock for the current thread. Each __lockForWriting__ message must be paired with an __unlockForWriting__ message before the lock is actually released. When the writer lock is released, it checks to see if the thread previously had any reader locks. If so, the reader lock count is restored. Invoking this method when the lock count is zero does nothing.

---

© 2001 Apple Computer, Inc. (Last Published April 17, 2001)

[![Table of Contents](attachments/FoundationRef/Java/Art/up.gif)](../FoundationTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
