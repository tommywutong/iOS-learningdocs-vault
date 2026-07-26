---
title: InlineArray
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/inlinearray
source_url: 'https://developer.apple.com/documentation/swift/inlinearray'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/inlinearray.json'
content_hash: 'sha256:23710a3a6f26ab68'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# InlineArray

<sub>Structure</sub>

A fixed-size array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct InlineArray<let count : Int, Element> where Element : ~Copyable
```

## Overview

An `InlineArray` is a specialized container that doesn’t use a separate memory allocation just to store its elements. When a value is copied, all of its elements are copied eagerly, like those of a tuple. Use an `InlineArray` when you have a fixed number of elements and need to avoid a separate heap allocation.

## Initializing a Value

When initializing a new `InlineArray` value, you must initialize all of its elements. You can use an array literal just as with `Array`, rely on type inference for the `count` and `Element` type, and spell the type with the shorthand `[count of Element]`.

```swift
let a: InlineArray<3, Int> = [1, 2, 3]
let b: InlineArray<_, Int> = [1, 2, 3]
let c: InlineArray<3, _>   = [1, 2, 3]
let d: InlineArray         = [1, 2, 3]

let e: [3 of Int]          = [1, 2, 3]
let f: [_ of Int]          = [1, 2, 3]
let g: [3 of _]            = [1, 2, 3]
let h: [_ of _]            = [1, 2, 3]
```

You can also use one of the type’s initializers to create a new value.

## Accessing Elements

Just as with `Array`, you can read and modify an element in an `InlineArray` using a subscript. Unless you use the memory-unsafe `unchecked` subscript, any index you provide is subject to bounds checking; an invalid index triggers a runtime error in your program.

```swift
var values: [3 of Double] = [1, 1.5, 2]
print(values[0])  // Prints "1.0"
values[1] -= 0.25
print(values[1])  // Prints "1.25"
values[3] = 42.0  // Fatal error: Index out of bounds
```

You can use the `indices` property to iterate over all elements in order.

```swift
for index in values.indices {
    print(values[index])
}
```

## Working with Noncopyable Elements

An `InlineArray` can store elements of potentially noncopyable type. When `Element` isn’t copyable, the `InlineArray` itself also isn’t copyable. You must then explicitly move or consume the value if you want to transfer ownership.

## Memory Layout

An `InlineArray` stores its elements contiguously. If an `InlineArray` is a stored property of a class, then it’s allocated on the heap along with the other stored properties of the class. Otherwise, in general, an `InlineArray` is allocated on the stack.

A _non-empty_ `InlineArray`’s size and stride are both found by multiplying the `count` of elements by the `Element`’s stride. Its alignment is equal to the `Element`’s alignment.

```swift
struct Record {
    let x: UInt32
    let y: Bool
}
MemoryLayout<Record>.size                 // 5
MemoryLayout<Record>.stride               // 8
MemoryLayout<Record>.alignment            // 4
MemoryLayout<[2 of Record]>.size          // 16
MemoryLayout<[2 of Record]>.stride        // 16
MemoryLayout<[2 of Record]>.alignment     // 4
MemoryLayout<(Record, Record)>.size       // 13
MemoryLayout<(Record, Record)>.stride     // 16
MemoryLayout<(Record, Record)>.alignment  // 4
```

An _empty_ `InlineArray`’s size is zero. Its stride and alignment are both one byte.

## Relationships

- **Conforms To**: [BitwiseCopyable](bitwisecopyable.md), [BorrowingSequence](borrowingsequence.md), [ContiguousBytes](../foundation/contiguousbytes.md), [ConvertibleFromBytes](convertiblefrombytes.md), [ConvertibleToBytes](convertibletobytes.md), [Copyable](copyable.md), [Escapable](escapable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Initializers

- [init(_:)](<inlinearray/init(__).md>) — Initializes every element in this array, by calling the given closure with each index.
- [init(first:next:)](<inlinearray/init(first_next_).md>) — Initializes every element in this array, by calling the given closure with each preceding element.
- [init(initializingWith:)](<inlinearray/init(initializingwith_).md>)
- [init(repeating:)](<inlinearray/init(repeating_).md>) — Initializes every element in this array to a copy of the given value.

### Instance Properties

- [count](inlinearray/count.md) — The number of elements in the array.
- [endIndex](inlinearray/endindex.md) — The array’s “past the end” position—that is, the position one greater than the last valid subscript argument.
- [indices](inlinearray/indices.md) — The indices that are valid for subscripting the array, in ascending order.
- [isEmpty](inlinearray/isempty.md) — A Boolean value indicating whether the array is empty.
- [mutableSpan](inlinearray/mutablespan.md) — A mutable span over the elements of this array.
- [span](inlinearray/span.md) — A span over the elements of this array.
- [startIndex](inlinearray/startindex.md) — The position of the first element in a nonempty array.

### Instance Methods

- [index(after:)](<inlinearray/index(after_).md>) — Returns the position immediately after the given index.
- [index(before:)](<inlinearray/index(before_).md>) — Returns the position immediately before the given index.
- [swapAt(_:_:)](<inlinearray/swapat(____).md>) — Exchanges the values at the specified indices of the array.

### Subscripts

- [subscript(_:)](<inlinearray/subscript(__).md>) — Accesses the element at the specified position.
- [subscript(unchecked:)](<inlinearray/subscript(unchecked_).md>) — Accesses the element at the specified position.

### Type Aliases

- [Index](inlinearray/index.md) — A type that represents a position in the array.

### Default Implementations

- [BorrowingSequence Implementations](inlinearray/borrowingsequence-implementations.md)

## See Also

### Arrays and Dictionaries

- [Array](array.md) — An ordered, random-access collection.
- [Dictionary](dictionary.md) — A collection whose elements are key-value pairs.
