---
title: Slice
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/slice
source_url: 'https://developer.apple.com/documentation/swift/slice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice.json'
content_hash: 'sha256:1508348ece71e0b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Slice

<sub>Structure</sub>

A view into a subsequence of elements of another collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Slice<Base> where Base : Collection
```

## Overview

A slice stores a base collection and the start and end indices of the view. It does not copy the elements from the collection into separate storage. Thus, creating a slice has O(1) complexity.

## Slices Share Indices

Indices of a slice can be used interchangeably with indices of the base collection. An element of a slice is located under the same index in the slice and in the base collection, as long as neither the collection nor the slice has been mutated since the slice was created.

For example, suppose you have an array holding the number of absences from each class during a session.

```swift
var absences = [0, 2, 0, 4, 0, 3, 1, 0]
```

You’re tasked with finding the day with the most absences in the second half of the session. To find the index of the day in question, follow these steps:

1. Create a slice of the `absences` array that holds the second half of the days.
2. Use the `max(by:)` method to determine the index of the day with the most absences.
3. Print the result using the index found in step 2 on the original `absences` array.

Here’s an implementation of those steps:

```swift
let secondHalf = absences.suffix(absences.count / 2)
if let i = secondHalf.indices.max(by: { secondHalf[$0] < secondHalf[$1] }) {
    print("Highest second-half absences: \(absences[i])")
}
// Prints "Highest second-half absences: 3"
```

## Slices Inherit Semantics

A slice inherits the value or reference semantics of its base collection. That is, if a `Slice` instance is wrapped around a mutable collection that has value semantics, such as an array, mutating the original collection would trigger a copy of that collection, and not affect the base collection stored inside of the slice.

For example, if you update the last element of the `absences` array from `0` to `2`, the `secondHalf` slice is unchanged.

```swift
absences[7] = 2
print(absences)
// Prints "[0, 2, 0, 4, 0, 3, 1, 2]"
print(secondHalf)
// Prints "[0, 3, 1, 0]"
```

Use slices only for transient computation. A slice may hold a reference to the entire storage of a larger collection, not just to the portion it presents, even after the base collection’s lifetime ends. Long-term storage of a slice may therefore prolong the lifetime of elements that are no longer otherwise accessible, which can erroneously appear to be memory leakage.

> [!note] Note
> Using a `Slice` instance with a mutable collection requires that the base collection’s `subscript(_: Index)` setter does not invalidate indices. If mutations need to invalidate indices in your custom collection type, don’t use `Slice` as its subsequence type. Instead, define your own subsequence type that takes your index invalidation requirements into account.

## Relationships

- **Conforms To**: [AccelerateBuffer](../accelerate/acceleratebuffer.md), [AccelerateMutableBuffer](../accelerate/acceleratemutablebuffer.md), [BidirectionalCollection](bidirectionalcollection.md), [Collection](collection.md), [ContiguousBytes](../foundation/contiguousbytes.md), [Copyable](copyable.md), [DataProtocol](../foundation/dataprotocol.md), [Escapable](escapable.md), [LazySequenceProtocol](lazysequenceprotocol.md), [MutableCollection](mutablecollection.md), [RandomAccessCollection](randomaccesscollection.md), [RangeReplaceableCollection](rangereplaceablecollection.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [Sequence](sequence.md)

## Topics

### Initializers

- [init(base:bounds:)](<slice/init(base_bounds_).md>) — Creates a view into the given collection that allows access to elements within the specified range.

### Instance Properties

- [base](slice/base.md) — The underlying collection of the slice.

### Instance Methods

- [assumingMemoryBound(to:)](<slice/assumingmemorybound(to_)-5fkwu.md>) — Returns a typed buffer to the memory referenced by this buffer slice, assuming that the memory is already bound to the specified type.
- [assumingMemoryBound(to:)](<slice/assumingmemorybound(to_)-7a4sa.md>) — Returns a typed buffer to the memory referenced by this buffer slice, assuming that the memory is already bound to the specified type.
- [bindMemory(to:)](<slice/bindmemory(to_)-4ombl.md>) — Binds this buffer slice’s memory to the specified type and returns a typed buffer of the bound memory.
- [bindMemory(to:)](<slice/bindmemory(to_)-92fs7.md>) — Binds this buffer slice’s memory to the specified type and returns a typed buffer of the bound memory.
- [copyBytes(from:)](<slice/copybytes(from_).md>) — Copies from a collection of `UInt8` into this buffer slice’s memory.
- [deinitialize()](<slice/deinitialize().md>) — Deinitializes every instance in this buffer slice.
- [deinitializeElement(at:)](<slice/deinitializeelement(at_).md>) — Deinitializes the memory underlying the element at `index`.
- [initialize(from:)](<slice/initialize(from_).md>) — Initializes the buffer slice’s memory with the given elements.
- [initialize(fromContentsOf:)](<slice/initialize(fromcontentsof_).md>) — Initializes the buffer slice’s memory with with every element of the source.
- [initialize(repeating:)](<slice/initialize(repeating_).md>) — Initializes every element in this buffer slice’s memory to a copy of the given value.
- [initializeElement(at:to:)](<slice/initializeelement(at_to_).md>) — Initializes the element at `index` to the given value.
- [initializeMemory(as:from:)](<slice/initializememory(as_from_).md>) — Initializes the buffer’s memory with the given elements, binding the initialized memory to the elements’ type.
- [initializeMemory(as:fromContentsOf:)](<slice/initializememory(as_fromcontentsof_).md>) — Initializes the buffer slice’s memory with every element of the source, binding the initialized memory to the elements’ type.
- [initializeMemory(as:repeating:)](<slice/initializememory(as_repeating_).md>) — Initializes the memory referenced by this buffer slice with the given value, binds the memory to the value’s type, and returns a typed buffer of the initialized memory.
- [insert(_:at:)](<slice/insert(__at_)-4n5zz.md>)
- [insert(contentsOf:at:)](<slice/insert(contentsof_at_)-3z6ts.md>)
- [load(fromByteOffset:as:)](<slice/load(frombyteoffset_as_)-3vjps.md>) — Returns a new instance of the given type, read from the specified offset into the buffer pointer slice’s raw memory.
- [load(fromByteOffset:as:)](<slice/load(frombyteoffset_as_)-45bko.md>) — Returns a new instance of the given type, read from the specified offset into the buffer pointer slice’s raw memory.
- [loadUnaligned(fromByteOffset:as:)](<slice/loadunaligned(frombyteoffset_as_)-6jvd4.md>)
- [loadUnaligned(fromByteOffset:as:)](<slice/loadunaligned(frombyteoffset_as_)-6u1jm.md>) — Returns a new instance of the given type, read from the specified offset into the buffer pointer slice’s raw memory.
- [loadUnaligned(fromByteOffset:as:)](<slice/loadunaligned(frombyteoffset_as_)-7jjnt.md>) — Returns a new instance of the given type, read from the specified offset into the buffer pointer slice’s raw memory.
- [loadUnaligned(fromByteOffset:as:)](<slice/loadunaligned(frombyteoffset_as_)-9gtr0.md>)
- [moveElement(from:)](<slice/moveelement(from_).md>) — Retrieves and returns the element at `index`, leaving that element’s underlying memory uninitialized.
- [moveInitialize(fromContentsOf:)](<slice/moveinitialize(fromcontentsof_)-82ebd.md>) — Moves every element of an initialized source buffer into the uninitialized memory referenced by this buffer slice, leaving the source memory uninitialized and this buffer slice’s memory initialized.
- [moveInitialize(fromContentsOf:)](<slice/moveinitialize(fromcontentsof_)-iasq.md>) — Moves every element of an initialized source buffer slice into the uninitialized memory referenced by this buffer slice, leaving the source memory uninitialized and this buffer slice’s memory initialized.
- [moveInitializeMemory(as:fromContentsOf:)](<slice/moveinitializememory(as_fromcontentsof_)-1jll.md>) — Moves every element of an initialized source buffer into the uninitialized memory referenced by this buffer slice, leaving the source memory uninitialized and this slice’s memory initialized.
- [moveInitializeMemory(as:fromContentsOf:)](<slice/moveinitializememory(as_fromcontentsof_)-1uz4a.md>) — Moves every element from an initialized source buffer slice into the uninitialized memory referenced by this buffer slice, leaving the source memory uninitialized and this slice’s memory initialized.
- [moveUpdate(fromContentsOf:)](<slice/moveupdate(fromcontentsof_)-5i98g.md>) — Updates this buffer slice’s initialized memory by moving every element from the source buffer, leaving the source memory uninitialized.
- [moveUpdate(fromContentsOf:)](<slice/moveupdate(fromcontentsof_)-ou4d.md>) — Updates this buffer slice’s initialized memory initialized memory by moving every element from the source buffer slice, leaving the source memory uninitialized.
- [remove(at:)](<slice/remove(at_)-pbti.md>)
- [removeSubrange(_:)](<slice/removesubrange(__)-8hbh1.md>)
- [replaceSubrange(_:with:)](<slice/replacesubrange(__with_)-904p8.md>)
- [storeBytes(of:toByteOffset:as:)](<slice/storebytes(of_tobyteoffset_as_).md>) — Stores a value’s bytes into the buffer pointer slice’s raw memory at the specified byte offset.
- [update(from:)](<slice/update(from_).md>) — Updates the buffer slice’s initialized memory with the given elements.
- [update(fromContentsOf:)](<slice/update(fromcontentsof_).md>) — Updates the buffer slice’s initialized memory with every element of the source.
- [update(repeating:)](<slice/update(repeating_).md>) — Updates every element of this buffer slice’s initialized memory.
- [withContiguousMutableStorageIfAvailable(_:)](<slice/withcontiguousmutablestorageifavailable(__)-2ader.md>)
- [withMemoryRebound(to:_:)](<slice/withmemoryrebound(to___)-1nqta.md>) — Executes the given closure while temporarily binding the buffer slice to instances of type `T`.
- [withMemoryRebound(to:_:)](<slice/withmemoryrebound(to___)-3oirt.md>) — Executes the given closure while temporarily binding the buffer slice to instances of type `T`.
- [withMemoryRebound(to:_:)](<slice/withmemoryrebound(to___)-6kxii.md>) — Executes the given closure while temporarily binding the memory referenced by this buffer slice to the given type.
- [withMemoryRebound(to:_:)](<slice/withmemoryrebound(to___)-ibp7.md>) — Executes the given closure while temporarily binding the memory referenced by this buffer slice to the given type.

### Default Implementations

- [BidirectionalCollection Implementations](slice/bidirectionalcollection-implementations.md)
- [Collection Implementations](slice/collection-implementations.md)
- [LazySequenceProtocol Implementations](slice/lazysequenceprotocol-implementations.md)
- [MutableCollection Implementations](slice/mutablecollection-implementations.md)
- [RangeReplaceableCollection Implementations](slice/rangereplaceablecollection-implementations.md)
- [Sequence Implementations](slice/sequence-implementations.md)
