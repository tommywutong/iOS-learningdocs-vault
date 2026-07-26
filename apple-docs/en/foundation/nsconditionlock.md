---
title: NSConditionLock
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsconditionlock
source_url: 'https://developer.apple.com/documentation/foundation/nsconditionlock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsconditionlock.json'
content_hash: 'sha256:5cbea0f34d140886'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSConditionLock

<sub>Class</sub>

A lock that can be associated with specific, user-defined conditions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSConditionLock
```

## Overview

Using an [NSConditionLock](nsconditionlock.md) object, you can ensure that a thread can acquire a lock only if a certain condition is met. Once it has acquired the lock and executed the critical section of code, the thread can relinquish the lock and set the associated condition to something new. The conditions themselves are arbitrary: you define them as needed for your application.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSLocking](nslocking.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing an NSConditionLock Object

- [- initWithCondition:](<nsconditionlock/init(condition_).md>) — Initializes a newly allocated `NSConditionLock` object and sets its condition.

### Accessing the Condition

- [condition](nsconditionlock/condition.md) — The condition associated with the receiver.

### Acquiring and Releasing a Lock

- [- lockBeforeDate:](<nsconditionlock/lock(before_).md>) — Attempts to acquire a lock before a specified moment in time.
- [- lockWhenCondition:](<nsconditionlock/lock(whencondition_).md>) — Attempts to acquire a lock.
- [- lockWhenCondition:beforeDate:](<nsconditionlock/lock(whencondition_before_).md>) — Attempts to acquire a lock before a specified moment in time.
- [- tryLock](<nsconditionlock/try().md>) — Attempts to acquire a lock without regard to the receiver’s condition.
- [- tryLockWhenCondition:](<nsconditionlock/trylock(whencondition_).md>) — Attempts to acquire a lock if the receiver’s condition is equal to the specified condition.
- [- unlockWithCondition:](<nsconditionlock/unlock(withcondition_).md>) — Relinquishes the lock and sets the receiver’s condition.

### Identifying the Condition Lock

- [name](nsconditionlock/name.md) — The name associated with the receiver.

## See Also

### Threads and Locking

- [Thread](thread.md) — A thread of execution.
- [NSLocking](nslocking.md) — The elementary methods adopted by classes that define lock objects.
- [NSLock](nslock.md) — An object that coordinates the operation of multiple threads of execution within the same application.
- [NSRecursiveLock](nsrecursivelock.md) — A lock that may be acquired multiple times by the same thread without causing a deadlock.
- [NSDistributedLock](nsdistributedlock.md) — A lock that multiple applications on multiple hosts can use to restrict access to some shared resource, such as a file.
- [NSCondition](nscondition.md) — A condition variable whose semantics follow those used for POSIX-style conditions.
