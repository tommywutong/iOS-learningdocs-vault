---
title: OSAllocatedUnfairLock
framework: os
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/osallocatedunfairlock
source_url: 'https://developer.apple.com/documentation/os/osallocatedunfairlock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osallocatedunfairlock.json'
content_hash: 'sha256:63712d5c29990d19'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# OSAllocatedUnfairLock

<sub>Structure</sub>

A structure that creates an unfair lock.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct OSAllocatedUnfairLock<State>
```

## Overview

Unfair locks are low-level locks that block efficiently on contention. They’re useful for protecting code that loads stored resources. However, it’s unsafe to use [os_unfair_lock](os_unfair_lock.md) from Swift because it’s a value type and, therefore, doesn’t have a stable memory address. That means when you call [os_unfair_lock_lock](os_unfair_lock_lock.md) or [os_unfair_lock_unlock](os_unfair_lock_unlock.md) and pass a lock object using the `&` operator, the system may lock or unlock the wrong object.

Instead, use [OSAllocatedUnfairLock](osallocatedunfairlock.md), which avoids that pitfall because it doesn’t function as a value type, despite being a structure. All copied instances of an [OSAllocatedUnfairLock](osallocatedunfairlock.md) control the same underlying lock allocation.

> [!important] Important
> If you’ve existing Swift code that uses [os_unfair_lock](os_unfair_lock.md), change it to use [OSAllocatedUnfairLock](osallocatedunfairlock.md) to ensure correct locking behavior.

To create a lock that protects operation state, create an enumeration that contains the possible states, then create a lock object, passing the initial state. Here’s an example of what that looks like for an asset load operation:

```swift
enum MyState {
    case idle
    case loading
    case complete(MyAsset)
    case error(Error)
}
let protectedState = OSAllocatedUnfairLock(initialState: MyState.idle)
```

Storing the state inside the lock helps track what the lock is protecting, and provides a way to safely access the state. To begin using the lock, call `withLock(_:)` or `withLockIfAvailable(_:)`, passing a closure that contains the code for the lock to protect, like in the following example:

```swift
func myLoadMethod() {
    protectedState.withLock { state in
        state = .loading
    }
    var (resource, error) = loadMyResources()
    if resource != nil {
        protectedState.withLock { state in
            state = .complete(resource)
        }
    } else {
        protectedState.withLock { state in
            state = .error(error!)
        }
    }
}
```

To protect an operation with an externally defined state or no state, create a lock object without specifying an initial state. Nonscoped locking is more flexible, but offers no assistance in tracking the state of the operation the lock protects. To use a nonscoped lock, use `withLock(_:)` or `withLockIfAvailable(_:)`.

```swift
let myLock = OSAllocatedUnfairLock()
myLock.withLock {
    // Code that needs protection.
}
```

You can also use [OSAllocatedUnfairLock](osallocatedunfairlock.md) with the more traditional lock/unlock approach by calling [lock()](<osallocatedunfairlock/lock().md>) before executing code that needs protection, and [unlock()](<osallocatedunfairlock/unlock().md>) upon completion, like this:

```swift
myLock.lock()
// Code that needs protection.
myLock.unlock()
```

When using this approach, you must call [unlock()](<osallocatedunfairlock/unlock().md>) from the same thread you use to call [lock()](<osallocatedunfairlock/lock().md>). Because of this, it’s unsafe to use this approach across an `await` suspension point. When using a lock with asynchronous code, lock using a closure or, even better, consider using an [Actor](../swift/actor.md).

> [!warning] Warning
> [OSAllocatedUnfairLock](osallocatedunfairlock.md) isn’t a recursive lock. Attempting to lock an object more than once from the same thread without unlocking in between triggers a runtime exception.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a lock object

- [init()](<osallocatedunfairlock/init().md>) — Creates a lock object that doesn’t protect state data.
- [init(initialState:)](<osallocatedunfairlock/init(initialstate_).md>) — Creates a lock object that maintains and protects state data.

### Using locks

- [lock()](<osallocatedunfairlock/lock().md>) — Acquires a lock.
- [lockIfAvailable()](<osallocatedunfairlock/lockifavailable().md>) — Attempts to acquire a lock.
- [unlock()](<osallocatedunfairlock/unlock().md>) — Ends the lock.

### Determining lock ownership

- [Ownership](osallocatedunfairlock/ownership.md) — An enumeration that represents the ownership status of an unfair lock.
- [precondition(_:)](<osallocatedunfairlock/precondition(__).md>) — Asserts if the lock object fails to meet specified ownership requirements.

### Initializers

- [init(uncheckedState:)](<osallocatedunfairlock/init(uncheckedstate_).md>)

### Instance Methods

- [lock(flags:)](<osallocatedunfairlock/lock(flags_).md>)
- [withLock(_:)](<osallocatedunfairlock/withlock(__)-1uy7m.md>)
- [withLock(_:)](<osallocatedunfairlock/withlock(__)-hple.md>)
- [withLock(flags:_:)](<osallocatedunfairlock/withlock(flags___)-1ub4c.md>)
- [withLock(flags:_:)](<osallocatedunfairlock/withlock(flags___)-u2xj.md>)
- [withLockIfAvailable(_:)](<osallocatedunfairlock/withlockifavailable(__)-1rp3w.md>)
- [withLockIfAvailable(_:)](<osallocatedunfairlock/withlockifavailable(__)-3kw0o.md>)
- [withLockIfAvailableUnchecked(_:)](<osallocatedunfairlock/withlockifavailableunchecked(__)-15q0y.md>)
- [withLockIfAvailableUnchecked(_:)](<osallocatedunfairlock/withlockifavailableunchecked(__)-6gji7.md>)
- [withLockUnchecked(_:)](<osallocatedunfairlock/withlockunchecked(__)-7qywq.md>)
- [withLockUnchecked(_:)](<osallocatedunfairlock/withlockunchecked(__)-9v03m.md>)
- [withLockUnchecked(flags:_:)](<osallocatedunfairlock/withlockunchecked(flags___)-8cv64.md>)
- [withLockUnchecked(flags:_:)](<osallocatedunfairlock/withlockunchecked(flags___)-9iq8s.md>)

## See Also

### Swift Wrappers

- [OSAllocatedUnfairLockFlags](osallocatedunfairlockflags.md)
