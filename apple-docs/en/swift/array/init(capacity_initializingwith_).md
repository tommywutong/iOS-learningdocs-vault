---
title: 'init(capacity:initializingWith:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 12.2+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 5.2+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/init(capacity:initializingwith:)'
source_url: 'https://developer.apple.com/documentation/swift/array/init(capacity:initializingwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/init%28capacity%3Ainitializingwith%3A%29.json'
content_hash: 'sha256:c8a260c3ead6a446'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# init(capacity:initializingWith:)

<sub>Initializer</sub>

Creates an array with the specified capacity, and then calls the given closure with an output span covering the array’s uninitialized memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<E>(capacity: Int, initializingWith initializer: @_lifetime(span: copy span) (inout OutputSpan<Element>) throws(E) -> Void) throws(E) where E : Error
```

## Parameters

- `capacity` — The number of elements to allocate space for in the new array.

- `initializer` — A closure that initializes the elements of the new array. - Parameters:      - span: An `OutputSpan` covering uninitialized memory with space for the specified number of elements.

## Discussion

Inside the closure, initialize elements by appending to the `OutputSpan`. The `OutputSpan` keeps track of memory’s initialization state, ensuring safety. Its `count` at the end of the closure will become the `count` of the newly-initialized array.

> [!note] Note
> While the resulting array may have a capacity larger than the requested amount, the `OutputSpan` passed to the closure will cover exactly the number of elements requested.
