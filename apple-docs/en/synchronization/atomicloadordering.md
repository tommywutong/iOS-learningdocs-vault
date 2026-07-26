---
title: AtomicLoadOrdering
framework: Synchronization
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/synchronization/atomicloadordering
source_url: 'https://developer.apple.com/documentation/synchronization/atomicloadordering'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/synchronization/atomicloadordering.json'
content_hash: 'sha256:3494e3dd25e63866'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Synchronization](../synchronization.md)

# AtomicLoadOrdering

<sub>Structure</sub>

Specifies the memory ordering semantics of an atomic load operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct AtomicLoadOrdering
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [acquiring](atomicloadordering/acquiring.md) — An acquiring load synchronizes with a releasing operation whose value its reads. It ensures that the releasing and acquiring threads agree that all subsequent variable accesses on the acquiring thread happen after the atomic operation itself.
- [relaxed](atomicloadordering/relaxed.md) — Guarantees the atomicity of the specific operation on which it is applied, but imposes no ordering constraints on any other variable accesses.
- [sequentiallyConsistent](atomicloadordering/sequentiallyconsistent.md) — A sequentially consistent load performs an acquiring load and also guarantees that it and all other sequentially consistent atomic operations (loads, stores, updates) appear to be executed in a single, total sequential ordering.

## See Also

### Memory Ordering Semantics

- [AtomicStoreOrdering](atomicstoreordering.md) — Specifies the memory ordering semantics of an atomic store operation.
- [AtomicUpdateOrdering](atomicupdateordering.md) — Specifies the memory ordering semantics of an atomic read-modify-write operation.
- [atomicMemoryFence(ordering:)](<atomicmemoryfence(ordering_).md>) — Establishes a memory ordering without associating it with a particular atomic operation.
