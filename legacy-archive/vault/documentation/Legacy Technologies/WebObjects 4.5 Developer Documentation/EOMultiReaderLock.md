---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOMultiReaderLock.html
archived_at: '2026-07-15T08:11:37.764326Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOMultiReaderLock

> **__Inherits
> from:__**
> : NSObject

> **__Package:__**
> : com.apple.yellow.eocontrol

---

## Class Description

---

The EOMultiReaderLock class provides Enterprise
Objects Framework with reader and writer locks.

|  |
| --- |
| __Note:__ This class doesn't exist in the com.apple.client.eocontrol package. Multithreaded clients aren't yet supported. All the client-side locks in Java Client application's are no-ops. |

The locks are recursive; a single thread can request a lock
many times, but a lock is actually taken only on the first request.
Likewise, when a thread indicates it's finished with a lock, it
takes an equal number of `unlock...` invocations
to return the lock.

There's no limit on the number of reader locks that a process
can take. However, there can only be one writer lock at a time,
and a writer lock is not issued until all reader locks are returned.
Reader locks aren't issued to new threads when there is a thread
waiting for a writer lock, but threads that already have a reader
lock can increment their lock count.

Thread safety is maintained with mutex locks (binary semaphores),
which ensure that no more than one critical section of code can
be processed at a time. The queuing order of requests for writer
locks is not managed by the class; the underlying implementation
of mutex signaling manages the queue order.

EOMultiReaderLock correctly handles promotion of a reader
lock to a writer lock, and the extension of a reader lock to the
current writer. This prevents a thread from deadlocking on itself
when requesting a combination of lock types.

EOMultiReaderLocks are slightly more time-expensive than NSRecursiveLocks
because the recursion count has to be stored per-thread, causing
each request for a reader lock to incur a hash. Writer locks are
even more expensive because EOMultiReaderLock must poll the hashtable
until all reader locks have been returned before the writer lock
can be taken.

## Instance Methods

---

### lockForReading

`public void lockForReading()`

Acquires a reader lock for the current thread.
If the current thread doesn't already have a lock, the method
blocks if there are any waiting or active writer locks. If the current
thread already has a lock (reader or writer), the lock request count
is incremented.

---

### lockForWriting

`public void lockForWriting()`

Gets a writer lock for the current thread. If
the current thread already has one, the lock request count is incremented,
but a new lock is not taken. If the requesting thread has outstanding
reader locks, they are temporarily dropped until the writer lock
is returned. If other threads have outstanding reader locks, this
method blocks until all reader locks have been freed.

---

### tryLockForReading

`public boolean tryLockForReading()`

Returns true if the current thread is able to
immediately obtain a reader lock. There are three ways this can
happen:

1. There are no outstanding writer locks.
2. The writer lock is held by the current thread.
3. The current thread already has a reader lock.

This
method implicitly calls `lockForReading`,
so you must call `unlockForReading` if `tryLockForReading` returns true.

---

### tryLockForWriting

`public boolean tryLockForWriting()`

Returns true if the current thread is able to
immediately obtain a writer lock. Returns false if another thread
already has the lock or is queued to receive it. This method implicitly
calls `lockForWriting`, so you must call `unlockForWriting` if `tryLockForReading` returns true.

---

### unlockForReading

`public void unlockForReading()`

Releases a reader lock for the current thread.
Each `lockForReading` message must be paired
with an `unlockForReading` message before
the lock is actually released. Invoking this method when the lock count
is zero does nothing.

---

### unlockForWriting

`public void unlockForWriting()`

Releases a writer lock for the current thread.
Each `lockForWriting` message must be paired
with an `unlockForWriting` message before
the lock is actually released. When the writer lock is released,
it checks to see if the thread previously had any reader locks.
If so, the reader lock count is restored. Invoking this method when
the lock count is zero does nothing.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
