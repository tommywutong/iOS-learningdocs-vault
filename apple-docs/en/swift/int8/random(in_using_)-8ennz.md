---
title: 'random(in:using:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int8/random(in:using:)-8ennz'
source_url: 'https://developer.apple.com/documentation/swift/int8/random(in:using:)-8ennz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int8/random%28in%3Ausing%3A%29-8ennz.json'
content_hash: 'sha256:a56e63b1d26f5b70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int8](../int8.md)

# random(in:using:)

<sub>Type Method</sub>

Returns a random value within the specified range, using the given generator as a source for randomness.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func random<T>(in range: ClosedRange<Self>, using generator: inout T) -> Self where T : RandomNumberGenerator
```

## Parameters

- `range` — The range in which to create a random value.

- `generator` — The random number generator to use when creating the new random value.

## Return Value

A random value within the bounds of `range`.

## Discussion

Use this method to generate an integer within a specific range when you are using a custom random number generator. This example creates three new values in the range `1...100`.

```swift
for _ in 1...3 {
    print(Int.random(in: 1...100, using: &myGenerator))
}
// Prints "7"
// Prints "44"
// Prints "21"
```
