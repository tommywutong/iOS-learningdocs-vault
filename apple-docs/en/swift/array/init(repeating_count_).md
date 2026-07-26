---
title: 'init(repeating:count:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/init(repeating:count:)'
source_url: 'https://developer.apple.com/documentation/swift/array/init(repeating:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/init%28repeating%3Acount%3A%29.json'
content_hash: 'sha256:a9546bd6013e735d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# init(repeating:count:)

<sub>Initializer</sub>

Creates a new array containing the specified number of a single, repeated value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(repeating repeatedValue: Element, count: Int)
```

## Parameters

- `repeatedValue` — The element to repeat.

- `count` — The number of times to repeat the value passed in the `repeating` parameter. `count` must be zero or greater.

## Discussion

Here’s an example of creating an array initialized with five strings containing the letter _Z_.

```swift
let fiveZs = Array(repeating: "Z", count: 5)
print(fiveZs)
// Prints "["Z", "Z", "Z", "Z", "Z"]"
```

## See Also

### Creating an Array

- [init()](<init().md>) — Creates a new, empty array.
- [init(_:)](<init(__)-1ip9h.md>) — Creates a new instance of a collection containing the elements of a sequence.
- [init(_:)](<init(__)-236cl.md>) — Creates an array containing the elements of a sequence.
- [init(unsafeUninitializedCapacity:initializingWith:)](<init(unsafeuninitializedcapacity_initializingwith_).md>) — Creates an array with the specified capacity, and then calls the given closure with a buffer covering the array’s uninitialized memory.
