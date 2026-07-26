---
title: ContiguousArray
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/contiguousarray
source_url: 'https://developer.apple.com/documentation/swift/contiguousarray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/contiguousarray.json'
content_hash: 'sha256:e963411f3ba95b32'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# ContiguousArray

<sub>Structure</sub>

A contiguously stored array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct ContiguousArray<Element>
```

## Overview

The `ContiguousArray` type is a specialized array that always stores its elements in a contiguous region of memory. This contrasts with `Array`, which can store its elements in either a contiguous region of memory or an `NSArray` instance if its `Element` type is a class or `@objc` protocol.

If your array’s `Element` type is a class or `@objc` protocol and you do not need to bridge the array to `NSArray` or pass the array to Objective-C APIs, using `ContiguousArray` may be more efficient and have more predictable performance than `Array`. If the array’s `Element` type is a struct or enumeration, `Array` and `ContiguousArray` should have similar efficiency.

For more information about using arrays, see `Array` and `ArraySlice`, with which `ContiguousArray` shares most properties and methods.

## Relationships

- **Conforms To**: [AccelerateBuffer](../accelerate/acceleratebuffer.md), [AccelerateMutableBuffer](../accelerate/acceleratemutablebuffer.md), [Attachable](../testing/attachable.md), [BNNSGraph.Builder.OperationParameter](../accelerate/bnnsgraph/builder/operationparameter.md), [BidirectionalCollection](bidirectionalcollection.md), [Collection](collection.md), [ContiguousBytes](../foundation/contiguousbytes.md), [Copyable](copyable.md), [CustomDebugStringConvertible](customdebugstringconvertible.md), [CustomReflectable](customreflectable.md), [CustomStringConvertible](customstringconvertible.md), [DataProtocol](../foundation/dataprotocol.md), [Decodable](decodable.md), [Encodable](encodable.md), [Equatable](equatable.md), [Escapable](escapable.md), [ExpressibleByArrayLiteral](expressiblebyarrayliteral.md), [Hashable](hashable.md), [MutableCollection](mutablecollection.md), [MutableDataProtocol](../foundation/mutabledataprotocol.md), [RandomAccessCollection](randomaccesscollection.md), [RangeReplaceableCollection](rangereplaceablecollection.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [Sequence](sequence.md)

## Topics

### Initializers

- [init(_:)](<contiguousarray/init(__).md>) — Creates an array containing the elements of a sequence.
- [init(capacity:initializingWith:)](<contiguousarray/init(capacity_initializingwith_).md>) — Creates an array with the specified capacity, and then calls the given closure with an output span covering the array’s uninitialized memory.
- [init(unsafeUninitializedCapacity:initializingWith:)](<contiguousarray/init(unsafeuninitializedcapacity_initializingwith_).md>) — Creates an array with the specified capacity, and then calls the given closure with a buffer covering the array’s uninitialized memory.

### Instance Properties

- [capacity](contiguousarray/capacity.md) — The total number of elements that the array can contain without allocating new storage.
- [mutableSpan](contiguousarray/mutablespan.md) — A mutable span over the elements of this array.
- [span](contiguousarray/span.md) — A span over the elements of this array.

### Instance Methods

- [append(addingCapacity:initializingWith:)](<contiguousarray/append(addingcapacity_initializingwith_).md>) — Grows the array to have enough capacity for the specified number of elements, then calls the closure with an output span covering the array’s uninitialized memory.
- [insert(_:at:)](<contiguousarray/insert(__at_).md>) — Inserts a new element at the specified position.
- [isTriviallyIdentical(to:)](<contiguousarray/istriviallyidentical(to_).md>) — Returns a boolean value indicating whether this array is identical to `other`.
- [remove(at:)](<contiguousarray/remove(at_).md>) — Removes and returns the element at the specified position.
- [reserveCapacity(_:)](<contiguousarray/reservecapacity(__).md>) — Reserves enough space to store the specified number of elements.
- [withUnsafeBufferPointer(_:)](<contiguousarray/withunsafebufferpointer(__).md>) — Calls a closure with a pointer to the array’s contiguous storage.
- [withUnsafeBytes(_:)](<contiguousarray/withunsafebytes(__).md>) — Calls the given closure with a pointer to the underlying bytes of the array’s contiguous storage.
- [withUnsafeMutableBufferPointer(_:)](<contiguousarray/withunsafemutablebufferpointer(__).md>) — Calls the given closure with a pointer to the array’s mutable contiguous storage.
- [withUnsafeMutableBytes(_:)](<contiguousarray/withunsafemutablebytes(__).md>) — Calls the given closure with a pointer to the underlying bytes of the array’s mutable contiguous storage.

### Default Implementations

- [Attachable Implementations](contiguousarray/attachable-implementations.md)
- [BidirectionalCollection Implementations](contiguousarray/bidirectionalcollection-implementations.md)
- [Collection Implementations](contiguousarray/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](contiguousarray/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](contiguousarray/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](contiguousarray/customstringconvertible-implementations.md)
- [Decodable Implementations](contiguousarray/decodable-implementations.md)
- [Encodable Implementations](contiguousarray/encodable-implementations.md)
- [Equatable Implementations](contiguousarray/equatable-implementations.md)
- [ExpressibleByArrayLiteral Implementations](contiguousarray/expressiblebyarrayliteral-implementations.md)
- [Hashable Implementations](contiguousarray/hashable-implementations.md)
- [MutableCollection Implementations](contiguousarray/mutablecollection-implementations.md)
- [OperationParameter Implementations](contiguousarray/operationparameter-implementations.md)
- [RandomAccessCollection Implementations](contiguousarray/randomaccesscollection-implementations.md)
- [RangeReplaceableCollection Implementations](contiguousarray/rangereplaceablecollection-implementations.md)
- [Sequence Implementations](contiguousarray/sequence-implementations.md)

## See Also

### Related Array Types

- [ArraySlice](arrayslice.md) — A slice of an `Array`, `ContiguousArray`, or `ArraySlice` instance.
