---
title: 'random(in:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint16/random(in:)-512t7'
source_url: 'https://developer.apple.com/documentation/swift/uint16/random(in:)-512t7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint16/random%28in%3A%29-512t7.json'
content_hash: 'sha256:2686a4ceb7644c06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt16](../uint16.md)

# random(in:)

<sub>Type Method</sub>

Returns a random value within the specified range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func random(in range: ClosedRange<Self>) -> Self
```

## Parameters

- `range` — The range in which to create a random value.

## Return Value

A random value within the bounds of `range`.

## Discussion

Use this method to generate an integer within a specific range. This example creates three new values in the range `1...100`.

```swift
for _ in 1...3 {
    print(Int.random(in: 1...100))
}
// Prints "53"
// Prints "64"
// Prints "5"
```

This method is equivalent to calling `random(in:using:)`, passing in the system’s default random generator.
