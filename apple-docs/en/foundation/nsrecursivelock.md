---
title: NSRecursiveLock
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsrecursivelock
source_url: 'https://developer.apple.com/documentation/foundation/nsrecursivelock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsrecursivelock.json'
content_hash: 'sha256:f45954aa0593033c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSRecursiveLock

<sub>Class</sub>

A lock that may be acquired multiple times by the same thread without causing a deadlock.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSRecursiveLock
```

## Overview

[NSRecursiveLock](nsrecursivelock.md) defines a lock that may be acquired multiple times by the same thread without causing a deadlock, a situation where a thread is permanently blocked waiting for itself to relinquish a lock. While the locking thread has one or more locks, all other threads are prevented from accessing the code protected by the lock.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSLocking](nslocking.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Acquiring a Lock

- [- lockBeforeDate:](<nsrecursivelock/lock(before_).md>) — Attempts to acquire a lock before a given date.
- [- tryLock](<nsrecursivelock/try().md>) — Attempts to acquire a lock, and immediately returns a Boolean value that indicates whether the attempt was successful.

### Naming the Lock

- [name](nsrecursivelock/name.md) — The name associated with the receiver.

## See Also

### Threads and Locking

- [Thread](thread.md) — A thread of execution.
- [NSLocking](nslocking.md) — The elementary methods adopted by classes that define lock objects.
- [NSLock](nslock.md) — An object that coordinates the operation of multiple threads of execution within the same application.
- [NSDistributedLock](nsdistributedlock.md) — A lock that multiple applications on multiple hosts can use to restrict access to some shared resource, such as a file.
- [NSConditionLock](nsconditionlock.md) — A lock that can be associated with specific, user-defined conditions.
- [NSCondition](nscondition.md) — A condition variable whose semantics follow those used for POSIX-style conditions.
