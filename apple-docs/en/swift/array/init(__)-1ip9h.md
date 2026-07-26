---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/init(_:)-1ip9h'
source_url: 'https://developer.apple.com/documentation/swift/array/init(_:)-1ip9h'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/init%28_%3A%29-1ip9h.json'
content_hash: 'sha256:012d4cb83dc02734'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# init(_:)

<sub>Initializer</sub>

Creates a new instance of a collection containing the elements of a sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S>(_ elements: S) where S : Sequence, Self.Element == S.Element
```

## Parameters

- `elements` — The sequence of elements for the new collection.

## See Also

### Creating an Array

- [init()](<init().md>) — Creates a new, empty array.
- [init(_:)](<init(__)-236cl.md>) — Creates an array containing the elements of a sequence.
- [init(repeating:count:)](<init(repeating_count_).md>) — Creates a new array containing the specified number of a single, repeated value.
- [init(unsafeUninitializedCapacity:initializingWith:)](<init(unsafeuninitializedcapacity_initializingwith_).md>) — Creates an array with the specified capacity, and then calls the given closure with a buffer covering the array’s uninitialized memory.
