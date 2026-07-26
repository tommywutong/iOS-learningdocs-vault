---
title: UnsafeMutableBufferPointer
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsafemutablebufferpointer
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablebufferpointer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablebufferpointer.json'
content_hash: 'sha256:7cf1d8b65c852ea4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# UnsafeMutableBufferPointer

<sub>Structure</sub>

A nonowning collection interface to a buffer of mutable elements stored contiguously in memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct UnsafeMutableBufferPointer<Element> where Element : ~Copyable
```

## Overview

You can use an `UnsafeMutableBufferPointer` instance in low level operations to eliminate uniqueness checks and, in release mode, bounds checks. Bounds checks are always performed in debug mode.

## UnsafeMutableBufferPointer Semantics

An `UnsafeMutableBufferPointer` instance is a view into memory and does not own the memory that it references. Copying a value of type `UnsafeMutableBufferPointer` does not copy the instances stored in the underlying memory. However, initializing another collection with an `UnsafeMutableBufferPointer` instance copies the instances out of the referenced memory and into the new collection.

## Relationships

- **Conforms To**: [AccelerateBuffer](../accelerate/acceleratebuffer.md), [AccelerateMutableBuffer](../accelerate/acceleratemutablebuffer.md), [AtomicRepresentable](../synchronization/atomicrepresentable.md), [BNNSGraph.Builder.OperationParameter](../accelerate/bnnsgraph/builder/operationparameter.md), [BNNSGraph.PointerArgument](../accelerate/bnnsgraph/pointerargument.md), [BidirectionalCollection](bidirectionalcollection.md), [BitwiseCopyable](bitwisecopyable.md), [Collection](collection.md), [ContiguousBytes](../foundation/contiguousbytes.md), [ConvertibleToBytes](convertibletobytes.md), [Copyable](copyable.md), [CustomDebugStringConvertible](customdebugstringconvertible.md), [Escapable](escapable.md), [MutableCollection](mutablecollection.md), [RandomAccessCollection](randomaccesscollection.md), [Sequence](sequence.md)

## Topics

### Initializers

- [init(_:)](<unsafemutablebufferpointer/init(__)-6750l.md>) — Initialize an `UnsafeMutableBufferPointer<Element>` from an `AudioBuffer`.
- [init(_:)](<unsafemutablebufferpointer/init(__)-789ap.md>)
- [init(mutating:)](<unsafemutablebufferpointer/init(mutating_).md>) — Creates a mutable typed buffer pointer referencing the same memory as the given immutable buffer pointer.
- [init(rebasing:)](<unsafemutablebufferpointer/init(rebasing_).md>) — Creates a buffer over the same memory as the given buffer slice.
- [init(start:count:)](<unsafemutablebufferpointer/init(start_count_).md>) — Creates a new buffer pointer over the specified number of contiguous instances beginning at the given pointer.

### Instance Properties

- [baseAddress](unsafemutablebufferpointer/baseaddress.md) — A pointer to the first element of the buffer.
- [count](unsafemutablebufferpointer/count.md) — The number of elements in the buffer.
- [mutableSpan](unsafemutablebufferpointer/mutablespan.md) — A mutable span over the elements of this buffer.
- [span](unsafemutablebufferpointer/span.md) — A span over the elements of this buffer.

### Instance Methods

- [assign(repeating:)](<unsafemutablebufferpointer/assign(repeating_).md>) _(deprecated)_
- [deallocate()](<unsafemutablebufferpointer/deallocate().md>) — Deallocates the memory block previously allocated at this buffer pointer’s base address.
- [deinitialize()](<unsafemutablebufferpointer/deinitialize().md>) — Deinitializes every instance in this buffer.
- [deinitializeElement(at:)](<unsafemutablebufferpointer/deinitializeelement(at_).md>) — Deinitializes the memory underlying the element at `index`.
- [extracting(_:)](<unsafemutablebufferpointer/extracting(__)-4izct.md>) — Constructs a standalone buffer pointer over the items within the supplied range of positions in the memory region addressed by this buffer pointer.
- [extracting(_:)](<unsafemutablebufferpointer/extracting(__)-51ps5.md>) — Constructs a standalone buffer pointer over the items within the supplied range of positions in the memory region addressed by this buffer pointer.
- [extracting(_:)](<unsafemutablebufferpointer/extracting(__)-6xfww.md>) — Extracts and returns a copy of the entire buffer.
- [initialize(from:)](<unsafemutablebufferpointer/initialize(from_).md>) — Initializes the buffer’s memory with the given elements.
- [initialize(fromContentsOf:)](<unsafemutablebufferpointer/initialize(fromcontentsof_).md>) — Initializes the buffer’s memory with every element of the source.
- [initialize(repeating:)](<unsafemutablebufferpointer/initialize(repeating_).md>) — Initializes every element in this buffer’s memory to a copy of the given value.
- [initializeElement(at:to:)](<unsafemutablebufferpointer/initializeelement(at_to_).md>) — Initializes the element at `index` to the given value.
- [isTriviallyIdentical(to:)](<unsafemutablebufferpointer/istriviallyidentical(to_).md>) — Returns a Boolean value indicating whether two instances refer to the same memory region.
- [moveElement(from:)](<unsafemutablebufferpointer/moveelement(from_).md>) — Retrieves and returns the element at `index`, leaving that element’s underlying memory uninitialized.
- [moveInitialize(fromContentsOf:)](<unsafemutablebufferpointer/moveinitialize(fromcontentsof_)-1ag7a.md>) — Moves every element of an initialized source buffer into the uninitialized memory referenced by this buffer, leaving the source memory uninitialized and this buffer’s memory initialized.
- [moveInitialize(fromContentsOf:)](<unsafemutablebufferpointer/moveinitialize(fromcontentsof_)-8aiwj.md>) — Moves every element of an initialized source buffer into the uninitialized memory referenced by this buffer, leaving the source memory uninitialized and this buffer’s memory initialized.
- [moveUpdate(fromContentsOf:)](<unsafemutablebufferpointer/moveupdate(fromcontentsof_)-4bpe7.md>) — Updates this buffer’s initialized memory initialized memory by moving every element from the source buffer slice, leaving the source memory uninitialized.
- [moveUpdate(fromContentsOf:)](<unsafemutablebufferpointer/moveupdate(fromcontentsof_)-522y2.md>) — Updates this buffer’s initialized memory by moving every element from the source buffer, leaving the source memory uninitialized.
- [update(from:)](<unsafemutablebufferpointer/update(from_).md>) — Updates the buffer’s initialized memory with the given elements.
- [update(fromContentsOf:)](<unsafemutablebufferpointer/update(fromcontentsof_).md>) — Updates the buffer’s initialized memory with every element of the source.
- [update(repeating:)](<unsafemutablebufferpointer/update(repeating_).md>) — Updates every element of this buffer’s initialized memory.
- [withMemoryRebound(to:_:)](<unsafemutablebufferpointer/withmemoryrebound(to___).md>) — Executes the given closure while temporarily binding the memory referenced by this buffer to the given type.

### Subscripts

- [subscript(_:)](<unsafemutablebufferpointer/subscript(__)-2vl82.md>) — Accesses the element at the specified position.

### Type Methods

- [allocate(capacity:)](<unsafemutablebufferpointer/allocate(capacity_).md>) — Allocates uninitialized memory for the specified number of instances of type `Element`.

### Default Implementations

- [AtomicRepresentable Implementations](unsafemutablebufferpointer/atomicrepresentable-implementations.md)
- [BidirectionalCollection Implementations](unsafemutablebufferpointer/bidirectionalcollection-implementations.md)
- [Collection Implementations](unsafemutablebufferpointer/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](unsafemutablebufferpointer/customdebugstringconvertible-implementations.md)
- [MutableCollection Implementations](unsafemutablebufferpointer/mutablecollection-implementations.md)
- [OperationParameter Implementations](unsafemutablebufferpointer/operationparameter-implementations.md)
- [Sequence Implementations](unsafemutablebufferpointer/sequence-implementations.md)

## See Also

### Typed Pointers

- [UnsafePointer](unsafepointer.md) — A pointer for accessing data of a specific type.
- [UnsafeMutablePointer](unsafemutablepointer.md) — A pointer for accessing and manipulating data of a specific type.
- [UnsafeBufferPointer](unsafebufferpointer.md) — A nonowning collection interface to a buffer of elements stored contiguously in memory.
