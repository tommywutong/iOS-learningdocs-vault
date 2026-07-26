---
title: 'init(repeating:count:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/arrayslice/init(repeating:count:)-95f9t'
source_url: 'https://developer.apple.com/documentation/swift/arrayslice/init(repeating:count:)-95f9t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/arrayslice/init%28repeating%3Acount%3A%29-95f9t.json'
content_hash: 'sha256:fd09f2af6e6f7d9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ArraySlice](../arrayslice.md)

# init(repeating:count:)

<sub>Initializer</sub>

Creates a new collection containing the specified number of a single, repeated value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(repeating repeatedValue: Self.Element, count: Int)
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
