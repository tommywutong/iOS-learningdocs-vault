---
title: UniqueArray
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swift/uniquearray
source_url: 'https://developer.apple.com/documentation/swift/uniquearray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray.json'
content_hash: 'sha256:2fb26bd2ce9da9f6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# UniqueArray

<sub>Structure</sub>

A dynamically self-resizing, heap allocated, noncopyable array of potentially noncopyable elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct UniqueArray<Element> where Element : ~Copyable
```

## Overview

`UniqueArray` instances automatically resize their underlying storage as needed to accommodate newly inserted items, using a geometric growth curve. This lets code using `UniqueArray` avoid having to allocate enough capacity in advance; on the other hand, it makes it difficult to tell when and where such reallocations may happen.

For example, appending an element to a `UniqueArray` has highly variable complexity; often, it runs at a constant cost, but if the operation has to resize storage, then the cost of an individual append suddenly becomes proportional to the size of the whole array.

The geometric growth curve allows the cost of such latency spikes to get amortized across repeated invocations, bringing the average cost back to O(1); but the spikes make this construct less suitable for use cases that expect predictable, consistent performance on every operation.

Implicit growth also makes it more difficult to predict/analyze the amount of memory an algorithm would need. Developers targeting environments with stringent limits on heap allocations may prefer to avoid using dynamically resizing container types as a matter of policy. The type `RigidArray` provides a fixed-capacity array variant that caters specifically for these use cases, trading ease-of-use for more consistent/predictable execution. For copyable elements, the copy-on-write `Array` type is an even more convenient and expressive choice.

## Relationships

- **Conforms To**: [Equatable](equatable.md), [Hashable](hashable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Initializers

- [init()](<uniquearray/init().md>) — Initializes a new unique array with no elements. _(beta)_
- [init(capacity:)](<uniquearray/init(capacity_).md>) — Initializes a new unique array with the specified capacity and no elements. _(beta)_
- [init(capacity:copying:)](<uniquearray/init(capacity_copying_)-5tkhn.md>) — Creates a new array with the specified initial capacity, holding a copy of the contents of a given sequence. _(beta)_
- [init(capacity:copying:)](<uniquearray/init(capacity_copying_)-991h4.md>) — Creates a new array with the specified capacity, holding a copy of the contents of the given span. _(beta)_
- [init(capacity:initializingWith:)](<uniquearray/init(capacity_initializingwith_).md>) — Creates a new array with the specified capacity, directly initializing its storage using an output span. _(beta)_
- [init(minimumCapacity:)](<uniquearray/init(minimumcapacity_).md>) — Initializes a new unique array with the specified capacity and no elements. _(beta)_
- [init(repeating:count:)](<uniquearray/init(repeating_count_).md>) — Creates a new array containing the specified number of a single, repeated value. _(beta)_

### Instance Properties

- [capacity](uniquearray/capacity.md) — The maximum number of elements this array can hold without having to reallocate its storage. _(beta)_
- [count](uniquearray/count.md) — The number of elements in this array. _(beta)_
- [debugDescription](uniquearray/debugdescription.md) _(beta)_
- [description](uniquearray/description.md) _(beta)_
- [endIndex](uniquearray/endindex.md) — The array’s “past the end” position—that is, the position one greater than the last valid subscript argument. This is always equal to array’s count. _(beta)_
- [freeCapacity](uniquearray/freecapacity.md) — The number of additional elements that can be added to this array without reallocating its storage. _(beta)_
- [indices](uniquearray/indices.md) — The range of indices that are valid for subscripting the array. _(beta)_
- [isEmpty](uniquearray/isempty.md) — A Boolean value indicating whether this array contains no elements. _(beta)_
- [mutableSpan](uniquearray/mutablespan.md) — A mutable span over the elements of this array, providing direct mutating access. _(beta)_
- [span](uniquearray/span.md) — A span over the elements of this array, providing direct read-only access. _(beta)_
- [startIndex](uniquearray/startindex.md) — The position of the first element in a nonempty array. This is always zero. _(beta)_

### Instance Methods

- [append(_:)](<uniquearray/append(__).md>) — Adds an element to the end of the array. _(beta)_
- [append(addingCount:initializingWith:)](<uniquearray/append(addingcount_initializingwith_).md>) — Append a given number of items to the end of this array by populating an output span. _(beta)_
- [append(copying:)](<uniquearray/append(copying_)-1qhpn.md>) — Copies the elements of a buffer to the end of this array. _(beta)_
- [append(copying:)](<uniquearray/append(copying_)-3aouw.md>) — Copies the elements of a span to the end of this array. _(beta)_
- [append(copying:)](<uniquearray/append(copying_)-7ntgb.md>) — Copies the elements of a sequence to the end of this array. _(beta)_
- [append(copying:)](<uniquearray/append(copying_)-90c4t.md>) — Copies the elements of a buffer to the end of this array. _(beta)_
- [append(moving:)](<uniquearray/append(moving_)-71oaj.md>) — Moves the elements of a buffer to the end of this array, leaving the buffer uninitialized. _(beta)_
- [append(moving:)](<uniquearray/append(moving_)-9p4vs.md>) — Moves the elements of a output span to the end of this array, leaving the span empty. _(beta)_
- [clone()](<uniquearray/clone().md>) — Copy the contents of this array into a newly allocated unique array instance with just enough capacity to hold all its elements. _(beta)_
- [clone(capacity:)](<uniquearray/clone(capacity_).md>) — Copy the contents of this array into a newly allocated unique array instance with the specified capacity. _(beta)_
- [distance(from:to:)](<uniquearray/distance(from_to_).md>) — Returns the distance between two indices. _(beta)_
- [edit(_:)](<uniquearray/edit(__).md>) — Arbitrarily edit the storage underlying this array by invoking a user-supplied closure with a mutable `OutputSpan` view over it. This method calls its function argument at most once, allowing it to arbitrarily modify the contents of the output span it is given. The argument is free to add, remove or reorder any items; however, it is not allowed to replace the span or change its capacity. _(beta)_
- [formIndex(_:offsetBy:limitedBy:)](<uniquearray/formindex(__offsetby_limitedby_).md>) — Offsets the given index by the specified distance, but no further than the given limiting index. _(beta)_
- [formIndex(after:)](<uniquearray/formindex(after_).md>) — Replaces the given index with its successor. _(beta)_
- [formIndex(before:)](<uniquearray/formindex(before_).md>) — Replaces the given index with its predecessor. _(beta)_
- [index(_:offsetBy:)](<uniquearray/index(__offsetby_).md>) — Returns an index that is the specified distance from the given index. _(beta)_
- [index(after:)](<uniquearray/index(after_).md>) — Returns the position immediately after the given index. _(beta)_
- [index(before:)](<uniquearray/index(before_).md>) — Returns the position immediately before the given index. _(beta)_
- [insert(_:at:)](<uniquearray/insert(__at_).md>) — Inserts a new element into the array at the specified position. _(beta)_
- [insert(addingCount:at:initializingWith:)](<uniquearray/insert(addingcount_at_initializingwith_).md>) — Inserts a given number of new items into this array at the specified position, using a callback to directly initialize array storage by populating an output span. _(beta)_
- [insert(copying:at:)](<uniquearray/insert(copying_at_)-2g824.md>) — Copies the elements of a span into this array at the specified position. _(beta)_
- [insert(copying:at:)](<uniquearray/insert(copying_at_)-4823q.md>) — Copies the elements of a collection into this array at the specified position. _(beta)_
- [insert(copying:at:)](<uniquearray/insert(copying_at_)-6kuy5.md>) — Copies the elements of a fully initialized buffer pointer into this array at the specified position. _(beta)_
- [insert(copying:at:)](<uniquearray/insert(copying_at_)-9wt40.md>) — Copies the elements of a fully initialized buffer pointer into this array at the specified position. _(beta)_
- [insert(moving:at:)](<uniquearray/insert(moving_at_)-4f2qc.md>) — Moves the elements of a fully initialized buffer into this array, starting at the specified position, and leaving the buffer uninitialized. _(beta)_
- [insert(moving:at:)](<uniquearray/insert(moving_at_)-6d5t1.md>) — Moves the elements of an output span into this array, starting at the specified position, and leaving the span empty. _(beta)_
- [isTriviallyIdentical(to:)](<uniquearray/istriviallyidentical(to_).md>) _(beta)_
- [popLast()](<uniquearray/poplast().md>) — Removes and returns the last element of the array, if there is one. _(beta)_
- [remove(at:)](<uniquearray/remove(at_).md>) — Removes and returns the element at the specified position. _(beta)_
- [removeAll()](<uniquearray/removeall().md>) — Removes all elements from the array, preserving its allocated capacity. _(beta)_
- [removeLast()](<uniquearray/removelast().md>) — Removes and returns the last element of the array. _(beta)_
- [removeLast(_:)](<uniquearray/removelast(__).md>) — Removes and discards the specified number of elements from the end of the array. _(beta)_
- [removeSubrange(_:)](<uniquearray/removesubrange(__)-6hkdt.md>) — Removes the specified subrange of elements from the array. _(beta)_
- [removeSubrange(_:)](<uniquearray/removesubrange(__)-6t21j.md>) — Removes the specified subrange of elements from the array. _(beta)_
- [replaceSubrange(_:addingCount:initializingWith:)](<uniquearray/replacesubrange(__addingcount_initializingwith_).md>) — Replaces the specified range of elements by a given count of new items, using a callback to directly initialize array storage by populating an output span. _(beta)_
- [replaceSubrange(_:copying:)](<uniquearray/replacesubrange(__copying_)-5cbxf.md>) — Replaces the specified subrange of elements by copying the elements of the given buffer pointer, which must be fully initialized. _(beta)_
- [replaceSubrange(_:copying:)](<uniquearray/replacesubrange(__copying_)-70i0j.md>) — Replaces the specified subrange of elements by copying the elements of the given span. _(beta)_
- [replaceSubrange(_:copying:)](<uniquearray/replacesubrange(__copying_)-7599g.md>) — Replaces the specified subrange of elements by copying the elements of the given collection. _(beta)_
- [replaceSubrange(_:copying:)](<uniquearray/replacesubrange(__copying_)-8tpt1.md>) — Replaces the specified subrange of elements by copying the elements of the given buffer pointer, which must be fully initialized. _(beta)_
- [replaceSubrange(_:moving:)](<uniquearray/replacesubrange(__moving_)-4de3f.md>) — Replaces the specified range of elements by moving the elements of a fully initialized buffer into their place. On return, the buffer is left in an uninitialized state. _(beta)_
- [replaceSubrange(_:moving:)](<uniquearray/replacesubrange(__moving_)-6vpdp.md>) — Replaces the specified range of elements by moving the contents of an output span into their place. On return, the span is left empty. _(beta)_
- [reserveCapacity(_:)](<uniquearray/reservecapacity(__).md>) — Ensure that the array has capacity to store the specified number of elements, by growing its storage buffer if necessary. _(beta)_
- [setCapacity(_:)](<uniquearray/setcapacity(__).md>) — Grow or shrink the capacity of a unique array instance without discarding its contents. _(beta)_
- [swapAt(_:_:)](<uniquearray/swapat(____).md>) — Exchanges the values at the specified indices of the array. _(beta)_

### Subscripts

- [subscript(_:)](<uniquearray/subscript(__).md>) — Accesses the element at the specified position. _(beta)_

### Type Aliases

- [Index](uniquearray/index.md) — A type that represents a position in the array: an integer offset from the start. _(beta)_

### Default Implementations

- [Equatable Implementations](uniquearray/equatable-implementations.md)
- [Hashable Implementations](uniquearray/hashable-implementations.md)

## See Also

### Heap Storage

- [UniqueBox](uniquebox.md) — A smart pointer type that uniquely owns an instance of `Value` on the heap. _(beta)_
