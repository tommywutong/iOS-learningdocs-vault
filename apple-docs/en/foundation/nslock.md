---
title: NSLock
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nslock
source_url: 'https://developer.apple.com/documentation/foundation/nslock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslock.json'
content_hash: 'sha256:490d81e1fc00e049'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSLock

<sub>Class</sub>

An object that coordinates the operation of multiple threads of execution within the same application.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSLock
```

## Overview

An [NSLock](nslock.md) object can be used to mediate access to an application’s global data or to protect a critical section of code, allowing it to run atomically.

> [!warning] Warning
> The [NSLock](nslock.md) class uses POSIX threads to implement its locking behavior. When sending an unlock message to an [NSLock](nslock.md) object, you must be sure that message is sent from the same thread that sent the initial lock message. Unlocking a lock from a different thread can result in undefined behavior.

You should not use this class to implement a recursive lock. Calling the `lock` method twice on the same thread will lock up your thread permanently. Use the [NSRecursiveLock](nsrecursivelock.md) class to implement recursive locks instead.

Unlocking a lock that is not locked is considered a programmer error and should be fixed in your code. The [NSLock](nslock.md) class reports such errors by printing an error message to the console when they occur.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSLocking](nslocking.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Acquiring a Lock

- [- lockBeforeDate:](<nslock/lock(before_).md>) — Attempts to acquire a lock before a given time and returns a Boolean value indicating whether the attempt was successful.
- [- tryLock](<nslock/try().md>) — Attempts to acquire a lock and immediately returns a Boolean value that indicates whether the attempt was successful.

### Naming the Lock

- [name](nslock/name.md) — The name associated with the receiver.

## See Also

### Threads and Locking

- [Thread](thread.md) — A thread of execution.
- [NSLocking](nslocking.md) — The elementary methods adopted by classes that define lock objects.
- [NSRecursiveLock](nsrecursivelock.md) — A lock that may be acquired multiple times by the same thread without causing a deadlock.
- [NSDistributedLock](nsdistributedlock.md) — A lock that multiple applications on multiple hosts can use to restrict access to some shared resource, such as a file.
- [NSConditionLock](nsconditionlock.md) — A lock that can be associated with specific, user-defined conditions.
- [NSCondition](nscondition.md) — A condition variable whose semantics follow those used for POSIX-style conditions.
