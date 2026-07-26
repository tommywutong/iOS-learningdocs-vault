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
doc_path: '/documentation/swift/int32/random(in:)-47fh7'
source_url: 'https://developer.apple.com/documentation/swift/int32/random(in:)-47fh7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int32/random%28in%3A%29-47fh7.json'
content_hash: 'sha256:6aafcedacb8b22af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int32](../int32.md)

# random(in:)

<sub>Type Method</sub>

Returns a random value within the specified range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func random(in range: Range<Self>) -> Self
```

## Parameters

- `range` — The range in which to create a random value. `range` must not be empty.

## Return Value

A random value within the bounds of `range`.

## Discussion

Use this method to generate an integer within a specific range. This example creates three new values in the range `1..<100`.

```swift
for _ in 1...3 {
    print(Int.random(in: 1..<100))
}
// Prints "53"
// Prints "64"
// Prints "5"
```

This method is equivalent to calling the version that takes a generator, passing in the system’s default random generator.
