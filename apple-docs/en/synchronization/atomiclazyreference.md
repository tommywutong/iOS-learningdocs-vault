---
title: AtomicLazyReference
framework: Synchronization
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/synchronization/atomiclazyreference
source_url: 'https://developer.apple.com/documentation/synchronization/atomiclazyreference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomiclazyreference.json'
content_hash: 'sha256:9186e1f73edd49c3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Synchronization](../synchronization.md)

# AtomicLazyReference

<sub>Structure</sub>

A lazily initializable atomic strong reference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct AtomicLazyReference<Instance> where Instance : AnyObject
```

## Overview

These values can be set (initialized) exactly once, but read many times.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init()](<atomiclazyreference/init().md>)

### Instance Methods

- [load()](<atomiclazyreference/load().md>) — Atomically loads and returns the current value of this reference.
- [storeIfNil(_:)](<atomiclazyreference/storeifnil(__).md>) — Atomically initializes this reference if its current value is nil, then returns the initialized value. If this reference is already initialized, then `storeIfNil(_:)` discards its supplied argument and returns the current value without updating it.

## See Also

### Atomic Values

- [Atomic](atomic.md) — An atomic value.
- [WordPair](wordpair.md) — A pair of two word sized `UInt`s.
- [AtomicRepresentable](atomicrepresentable.md) — A type that supports atomic operations through a separate atomic storage representation.
- [AtomicOptionalRepresentable](atomicoptionalrepresentable.md) — An atomic value that also supports atomic operations when wrapped in an `Optional`. Atomic optional representable types come with a standalone atomic representation for their optional-wrapped variants.
