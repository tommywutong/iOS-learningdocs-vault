---
title: UnsafeBufferPointer
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsafebufferpointer
source_url: 'https://developer.apple.com/documentation/swift/unsafebufferpointer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafebufferpointer.json'
content_hash: 'sha256:ee89c25f243748e1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# UnsafeBufferPointer

<sub>Structure</sub>

A nonowning collection interface to a buffer of elements stored contiguously in memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct UnsafeBufferPointer<Element> where Element : ~Copyable
```

## Overview

You can use an `UnsafeBufferPointer` instance in low level operations to eliminate uniqueness checks and, in release mode, bounds checks. Bounds checks are always performed in debug mode.

## UnsafeBufferPointer Semantics

An `UnsafeBufferPointer` instance is a view into memory and does not own the memory that it references. Copying a value of type `UnsafeBufferPointer` does not copy the instances stored in the underlying memory. However, initializing another collection with an `UnsafeBufferPointer` instance copies the instances out of the referenced memory and into the new collection.

## Relationships

- **Conforms To**: [AccelerateBuffer](../accelerate/acceleratebuffer.md), [AtomicRepresentable](../synchronization/atomicrepresentable.md), [BNNSGraph.Builder.OperationParameter](../accelerate/bnnsgraph/builder/operationparameter.md), [BidirectionalCollection](bidirectionalcollection.md), [BitwiseCopyable](bitwisecopyable.md), [Collection](collection.md), [ContiguousBytes](../foundation/contiguousbytes.md), [ConvertibleToBytes](convertibletobytes.md), [Copyable](copyable.md), [CustomDebugStringConvertible](customdebugstringconvertible.md), [DataProtocol](../foundation/dataprotocol.md), [Escapable](escapable.md), [RandomAccessCollection](randomaccesscollection.md), [Sequence](sequence.md)

## Topics

### Initializers

- [init(_:)](<unsafebufferpointer/init(__)-2fjdq.md>)
- [init(_:)](<unsafebufferpointer/init(__)-36fvm.md>) — Creates an immutable typed buffer pointer referencing the same memory as the given mutable buffer pointer.
- [init(_:)](<unsafebufferpointer/init(__)-5ei4s.md>) — Initialize an `UnsafeBufferPointer<Element>` from an `AudioBuffer`. Binds the buffer’s memory type to `Element`.
- [init(rebasing:)](<unsafebufferpointer/init(rebasing_)-53eec.md>) — Creates a buffer over the same memory as the given buffer slice.
- [init(rebasing:)](<unsafebufferpointer/init(rebasing_)-56rdb.md>) — Creates a buffer over the same memory as the given buffer slice.
- [init(start:count:)](<unsafebufferpointer/init(start_count_).md>) — Creates a new buffer pointer over the specified number of contiguous instances beginning at the given pointer.

### Instance Properties

- [baseAddress](unsafebufferpointer/baseaddress.md) — A pointer to the first element of the buffer.
- [count](unsafebufferpointer/count.md) — The number of elements in the buffer.
- [span](unsafebufferpointer/span.md) — A span over the elements of this buffer.

### Instance Methods

- [deallocate()](<unsafebufferpointer/deallocate().md>) — Deallocates the memory block previously allocated at this buffer pointer’s base address.
- [extracting(_:)](<unsafebufferpointer/extracting(__)-47z4z.md>) — Constructs a standalone buffer pointer over the items within the supplied range of positions in the memory region addressed by this buffer pointer.
- [extracting(_:)](<unsafebufferpointer/extracting(__)-4bn8q.md>) — Extracts and returns a copy of the entire buffer.
- [extracting(_:)](<unsafebufferpointer/extracting(__)-nivx.md>) — Constructs a standalone buffer pointer over the items within the supplied range of positions in the memory region addressed by this buffer pointer.
- [isTriviallyIdentical(to:)](<unsafebufferpointer/istriviallyidentical(to_).md>) — Returns a Boolean value indicating whether two instances refer to the same memory region.
- [withMemoryRebound(to:_:)](<unsafebufferpointer/withmemoryrebound(to___).md>) — Executes the given closure while temporarily binding the memory referenced by this buffer to the given type.

### Subscripts

- [subscript(_:)](<unsafebufferpointer/subscript(__)-3sy16.md>) — Accesses the element at the specified position.

### Default Implementations

- [AtomicRepresentable Implementations](unsafebufferpointer/atomicrepresentable-implementations.md)
- [BidirectionalCollection Implementations](unsafebufferpointer/bidirectionalcollection-implementations.md)
- [Collection Implementations](unsafebufferpointer/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](unsafebufferpointer/customdebugstringconvertible-implementations.md)
- [OperationParameter Implementations](unsafebufferpointer/operationparameter-implementations.md)
- [Sequence Implementations](unsafebufferpointer/sequence-implementations.md)

## See Also

### Typed Pointers

- [UnsafePointer](unsafepointer.md) — A pointer for accessing data of a specific type.
- [UnsafeMutablePointer](unsafemutablepointer.md) — A pointer for accessing and manipulating data of a specific type.
- [UnsafeMutableBufferPointer](unsafemutablebufferpointer.md) — A nonowning collection interface to a buffer of mutable elements stored contiguously in memory.
