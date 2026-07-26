---
title: 'append(addingCapacity:initializingWith:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/contiguousarray/append(addingcapacity:initializingwith:)'
source_url: 'https://developer.apple.com/documentation/swift/contiguousarray/append(addingcapacity:initializingwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/contiguousarray/append%28addingcapacity%3Ainitializingwith%3A%29.json'
content_hash: 'sha256:1ca350e4a7d3fbbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ContiguousArray](../contiguousarray.md)

# append(addingCapacity:initializingWith:)

<sub>Instance Method</sub>

Grows the array to have enough capacity for the specified number of elements, then calls the closure with an output span covering the array’s uninitialized memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append<E>(addingCapacity uninitializedCount: Int, initializingWith initializer: @_lifetime(span: copy span) (inout OutputSpan<Element>) throws(E) -> Void) throws(E) where E : Error
```

## Parameters

- `uninitializedCount` — The number of new elements the array should have space for.

- `initializer` — A closure that initializes new elements. - Parameters:      - span: An `OutputSpan` covering uninitialized memory with space for the specified number of additional elements.

## Discussion

Inside the closure, initialize elements by appending to `span`. It ensures safety by keeping track of the initialization state of the memory At the end of the closure, `span`’s `count` elements will have been appended to the array.

If the closure throws an error, the items appended until that point will remain in the array.
