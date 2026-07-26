---
title: NSDistributedLock
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdistributedlock
source_url: 'https://developer.apple.com/documentation/foundation/nsdistributedlock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdistributedlock.json'
content_hash: 'sha256:d2efd42271be872f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSDistributedLock

<sub>Class</sub>

A lock that multiple applications on multiple hosts can use to restrict access to some shared resource, such as a file.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSDistributedLock
```

## Overview

The lock is implemented by an entry (such as a file or directory) in the file system. For multiple applications to use an [NSDistributedLock](nsdistributedlock.md) object to coordinate their activities, the lock must be writable on a file system accessible to all hosts on which the applications might be running.

Use the [- tryLock](<nsdistributedlock/try().md>) method to attempt to acquire a lock. You should generally use the [- unlock](<nsdistributedlock/unlock().md>) method to release the lock rather than [- breakLock](<nsdistributedlock/break().md>).

[NSDistributedLock](nsdistributedlock.md) doesn’t conform to the [NSLocking](nslocking.md) protocol, nor does it have a `lock` method. The protocol’s [- lock](<nslocking/lock().md>) method is intended to block the execution of the thread until successful. For an [NSDistributedLock](nsdistributedlock.md) object, this could mean polling the file system at some predetermined rate. A better solution is to provide the [- tryLock](<nsdistributedlock/try().md>) method and let you determine the polling frequency that makes sense for your application.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an NSDistributedLock

- [- initWithPath:](<nsdistributedlock/init(path_).md>) — Initializes an `NSDistributedLock` object to use as the lock the file-system entry specified by a given path.

### Acquiring a Lock

- [- tryLock](<nsdistributedlock/try().md>) — Attempts to acquire the receiver and immediately returns a Boolean value that indicates whether the attempt was successful.

### Relinquishing a Lock

- [- breakLock](<nsdistributedlock/break().md>) — Forces the lock to be relinquished.
- [- unlock](<nsdistributedlock/unlock().md>) — Relinquishes the receiver.

### Getting Lock Information

- [lockDate](nsdistributedlock/lockdate.md) — Returns the time the receiver was acquired by any of the `NSDistributedLock` objects using the same path.

## See Also

### Threads and Locking

- [Thread](thread.md) — A thread of execution.
- [NSLocking](nslocking.md) — The elementary methods adopted by classes that define lock objects.
- [NSLock](nslock.md) — An object that coordinates the operation of multiple threads of execution within the same application.
- [NSRecursiveLock](nsrecursivelock.md) — A lock that may be acquired multiple times by the same thread without causing a deadlock.
- [NSConditionLock](nsconditionlock.md) — A lock that can be associated with specific, user-defined conditions.
- [NSCondition](nscondition.md) — A condition variable whose semantics follow those used for POSIX-style conditions.
