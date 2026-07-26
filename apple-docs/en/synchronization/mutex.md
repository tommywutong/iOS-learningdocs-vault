---
title: Mutex
framework: Synchronization
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/synchronization/mutex
source_url: 'https://developer.apple.com/documentation/synchronization/mutex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/mutex.json'
content_hash: 'sha256:94181519478a07ab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Synchronization](../synchronization.md)

# Mutex

<sub>Structure</sub>

A synchronization primitive that protects shared mutable state via mutual exclusion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Mutex<Value> where Value : ~Copyable
```

## Overview

The `Mutex` type offers non-recursive exclusive access to the state it is protecting by blocking threads attempting to acquire the lock. Only one execution context at a time has access to the value stored within the `Mutex` allowing for exclusive access.

An example use of `Mutex` in a class used simultaneously by many threads protecting a `Dictionary` value:

```swift
class Manager {
  let cache = Mutex<[Key: Resource]>([:])

  func saveResource(_ resource: Resource, as key: Key) {
    cache.withLock {
      $0[key] = resource
    }
  }
}
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(_:)](<mutex/init(__).md>) — Initializes a value of this mutex with the given initial state.

### Instance Methods

- [withLock(_:)](<mutex/withlock(__).md>) — Calls the given closure after acquiring the lock and then releases ownership.
- [withLockIfAvailable(_:)](<mutex/withlockifavailable(__).md>) — Attempts to acquire the lock and then calls the given closure if successful.
