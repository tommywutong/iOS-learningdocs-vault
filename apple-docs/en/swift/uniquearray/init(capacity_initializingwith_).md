---
title: 'init(capacity:initializingWith:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/init(capacity:initializingwith:)'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/init(capacity:initializingwith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/init%28capacity%3Ainitializingwith%3A%29.json'
content_hash: 'sha256:84a7dca741941618'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# init(capacity:initializingWith:)

<sub>Initializer</sub>

Creates a new array with the specified capacity, directly initializing its storage using an output span.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<E>(capacity: Int, initializingWith body: @_lifetime(0: copy 0) (inout OutputSpan<Element>) throws(E) -> Void) throws(E) where E : Error
```

## Parameters

- `capacity` — The storage capacity of the new array.

- `body` — A callback that gets called at most once to directly populate newly reserved storage within the array. The function is allowed to add fewer than `capacity` items. The array is initialized with however many items the callback adds to the output span before it returns (or before it throws an error).
