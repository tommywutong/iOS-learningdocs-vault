---
title: UnsafeMutableRawBufferPointer
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsafemutablerawbufferpointer
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawbufferpointer.json'
content_hash: 'sha256:15455e1eb362f6f9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# UnsafeMutableRawBufferPointer

<sub>Structure</sub>

A mutable nonowning collection interface to the bytes in a region of memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct UnsafeMutableRawBufferPointer
```

## Overview

You can use an `UnsafeMutableRawBufferPointer` instance in low-level operations to eliminate uniqueness checks and release mode bounds checks. Bounds checks are always performed in debug mode.

An `UnsafeMutableRawBufferPointer` instance is a view of the raw bytes in a region of memory. Each byte in memory is viewed as a `UInt8` value independent of the type of values held in that memory. Reading from and writing to memory through a raw buffer are untyped operations. Accessing this collection’s bytes does not bind the underlying memory to `UInt8`.

In addition to its collection interface, an `UnsafeMutableRawBufferPointer` instance also supports the following methods provided by `UnsafeMutableRawPointer`, including bounds checks in debug mode:

- `load(fromByteOffset:as:)`
- `loadUnaligned(fromByteOffset:as:)`
- `storeBytes(of:toByteOffset:as:)`
- `copyMemory(from:)`

To access the underlying memory through typed operations, the memory must be bound to a trivial type.

> [!note] Note
> A _trivial type_ can be copied bit for bit with no indirection or reference-counting operations. Generally, native Swift types that do not contain strong or weak references or other forms of indirection are trivial, as are imported C structs and enums. Copying memory that contains values of nontrivial types can only be done safely with a typed pointer. Copying bytes directly from nontrivial, in-memory values does not produce valid copies and can only be done by calling a C API, such as `memmove()`.

## UnsafeMutableRawBufferPointer Semantics

An `UnsafeMutableRawBufferPointer` instance is a view into memory and does not own the memory that it references. Copying a variable or constant of type `UnsafeMutableRawBufferPointer` does not copy the underlying memory. However, initializing another collection with an `UnsafeMutableRawBufferPointer` instance copies bytes out of the referenced memory and into the new collection.

The following example uses `someBytes`, an `UnsafeMutableRawBufferPointer` instance, to demonstrate the difference between assigning a buffer pointer and using a buffer pointer as the source for another collection’s elements. Here, the assignment to `destBytes` creates a new, nonowning buffer pointer covering the first `n` bytes of the memory that `someBytes` references—nothing is copied:

```swift
var destBytes = someBytes[0..<n]
```

Next, the bytes referenced by `destBytes` are copied into `byteArray`, a new `[UInt8]` array, and then the remainder of `someBytes` is appended to `byteArray`:

```swift
var byteArray: [UInt8] = Array(destBytes)
byteArray += someBytes[n..<someBytes.count]
```

Assigning into a ranged subscript of an `UnsafeMutableRawBufferPointer` instance copies bytes into the memory. The next `n` bytes of the memory that `someBytes` references are copied in this code:

```swift
destBytes[0..<n] = someBytes[n..<(n + n)]
```

## Relationships

- **Conforms To**: [AtomicRepresentable](../synchronization/atomicrepresentable.md), [BidirectionalCollection](bidirectionalcollection.md), [BitwiseCopyable](bitwisecopyable.md), [Collection](collection.md), [ContiguousBytes](../foundation/contiguousbytes.md), [ConvertibleToBytes](convertibletobytes.md), [Copyable](copyable.md), [CustomDebugStringConvertible](customdebugstringconvertible.md), [Escapable](escapable.md), [MutableCollection](mutablecollection.md), [RandomAccessCollection](randomaccesscollection.md), [Sequence](sequence.md)

## Topics

### Initializers

- [init(_:)](<unsafemutablerawbufferpointer/init(__)-5kt34.md>) — Creates a new buffer over the same memory as the given buffer.
- [init(_:)](<unsafemutablerawbufferpointer/init(__)-9dmrh.md>) — Creates a raw buffer over the contiguous bytes in the given typed buffer.
- [init(mutating:)](<unsafemutablerawbufferpointer/init(mutating_).md>) — Creates a new mutable buffer over the same memory as the given buffer.
- [init(rebasing:)](<unsafemutablerawbufferpointer/init(rebasing_).md>) — Creates a raw buffer over the same memory as the given raw buffer slice, with the indices rebased to zero.
- [init(start:count:)](<unsafemutablerawbufferpointer/init(start_count_).md>) — Creates a buffer over the specified number of contiguous bytes starting at the given pointer.

### Instance Properties

- [baseAddress](unsafemutablerawbufferpointer/baseaddress.md) — A pointer to the first byte of the buffer.
- [bytes](unsafemutablerawbufferpointer/bytes.md) — A span over the bytes of this buffer.
- [mutableBytes](unsafemutablerawbufferpointer/mutablebytes.md) — A mutable span over the bytes of this buffer.

### Instance Methods

- [assumingMemoryBound(to:)](<unsafemutablerawbufferpointer/assumingmemorybound(to_).md>) — Returns a typed buffer to the memory referenced by this buffer, assuming that the memory is already bound to the specified type.
- [bindMemory(to:)](<unsafemutablerawbufferpointer/bindmemory(to_).md>) — Binds this buffer’s memory to the specified type and returns a typed buffer of the bound memory.
- [copyBytes(from:)](<unsafemutablerawbufferpointer/copybytes(from_)-6hg9u.md>) — Copies from a collection of `UInt8` into this buffer’s memory.
- [copyBytes(from:)](<unsafemutablerawbufferpointer/copybytes(from_)-8y3nw.md>)
- [copyMemory(from:)](<unsafemutablerawbufferpointer/copymemory(from_).md>) — Copies the bytes from the given buffer to this buffer’s memory.
- [deallocate()](<unsafemutablerawbufferpointer/deallocate().md>) — Deallocates the memory block previously allocated at this buffer pointer’s base address.
- [initializeMemory(as:from:)](<unsafemutablerawbufferpointer/initializememory(as_from_).md>) — Initializes the buffer’s memory with the given elements, binding the initialized memory to the elements’ type.
- [initializeMemory(as:fromContentsOf:)](<unsafemutablerawbufferpointer/initializememory(as_fromcontentsof_).md>) — Initializes the buffer’s memory with every element of the source, binding the initialized memory to the elements’ type.
- [initializeMemory(as:repeating:)](<unsafemutablerawbufferpointer/initializememory(as_repeating_).md>) — Initializes the memory referenced by this buffer with the given value, binds the memory to the value’s type, and returns a typed buffer of the initialized memory.
- [isTriviallyIdentical(to:)](<unsafemutablerawbufferpointer/istriviallyidentical(to_).md>) — Returns a Boolean value indicating whether two instances refer to the same memory region.
- [load(fromByteOffset:as:)](<unsafemutablerawbufferpointer/load(frombyteoffset_as_).md>) — Returns a new instance of the given type, read from the buffer pointer’s raw memory at the specified byte offset.
- [loadUnaligned(fromByteOffset:as:)](<unsafemutablerawbufferpointer/loadunaligned(frombyteoffset_as_)-9iyyx.md>) — Returns a new instance of the given type, constructed from the raw memory at the specified offset.
- [loadUnaligned(fromByteOffset:as:)](<unsafemutablerawbufferpointer/loadunaligned(frombyteoffset_as_)-q4sv.md>)
- [moveInitializeMemory(as:fromContentsOf:)](<unsafemutablerawbufferpointer/moveinitializememory(as_fromcontentsof_)-3gs5r.md>) — Moves every element of an initialized source buffer into the uninitialized memory referenced by this buffer, leaving the source memory uninitialized and this buffer’s memory initialized.
- [moveInitializeMemory(as:fromContentsOf:)](<unsafemutablerawbufferpointer/moveinitializememory(as_fromcontentsof_)-8gjm9.md>) — Moves every element of an initialized source buffer slice into the uninitialized memory referenced by this buffer, leaving the source memory uninitialized and this buffer’s memory initialized.
- [storeBytes(of:toByteOffset:as:)](<unsafemutablerawbufferpointer/storebytes(of_tobyteoffset_as_).md>) — Stores a value’s bytes into the buffer pointer’s raw memory at the specified byte offset.
- [withMemoryRebound(to:_:)](<unsafemutablerawbufferpointer/withmemoryrebound(to___).md>) — Executes the given closure while temporarily binding the buffer to instances of type `T`.

### Type Methods

- [allocate(byteCount:alignment:)](<unsafemutablerawbufferpointer/allocate(bytecount_alignment_).md>) — Allocates uninitialized memory with the specified size and alignment.
- [allocate(count:)](<unsafemutablerawbufferpointer/allocate(count_).md>)

### Default Implementations

- [AtomicRepresentable Implementations](unsafemutablerawbufferpointer/atomicrepresentable-implementations.md)
- [BidirectionalCollection Implementations](unsafemutablerawbufferpointer/bidirectionalcollection-implementations.md)
- [Collection Implementations](unsafemutablerawbufferpointer/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](unsafemutablerawbufferpointer/customdebugstringconvertible-implementations.md)
- [MutableCollection Implementations](unsafemutablerawbufferpointer/mutablecollection-implementations.md)
- [RandomAccessCollection Implementations](unsafemutablerawbufferpointer/randomaccesscollection-implementations.md)
- [Sequence Implementations](unsafemutablerawbufferpointer/sequence-implementations.md)

## See Also

### Raw Pointers

- [UnsafeRawPointer](unsaferawpointer.md) — A raw pointer for accessing untyped data.
- [UnsafeMutableRawPointer](unsafemutablerawpointer.md) — A raw pointer for accessing and manipulating untyped data.
- [UnsafeRawBufferPointer](unsaferawbufferpointer.md) — A  nonowning collection interface to the bytes in a region of memory.
