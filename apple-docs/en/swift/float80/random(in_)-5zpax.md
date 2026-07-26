---
title: 'random(in:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float80/random(in:)-5zpax'
source_url: 'https://developer.apple.com/documentation/swift/float80/random(in:)-5zpax'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/random%28in%3A%29-5zpax.json'
content_hash: 'sha256:1f8159e3a9c45b5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# random(in:)

<sub>Type Method</sub>

Returns a random value within the specified range.

<sub>macOS</sub>

```swift
static func random(in range: ClosedRange<Self>) -> Self
```

## Parameters

- `range` — The range in which to create a random value. Must be finite.

## Return Value

A random value within the bounds of `range`.

## Discussion

Use this method to generate a floating-point value within a specific range. This example creates three new values in the range `10.0 ... 20.0`.

```swift
for _ in 1...3 {
    print(Double.random(in: 10.0 ... 20.0))
}
// Prints "18.1900709259179"
// Prints "14.2286325689993"
// Prints "13.1485686260762"
```

The `random()` static method chooses a random value from a continuous uniform distribution in `range`, and then converts that value to the nearest representable value in this type. Depending on the size and span of `range`, some concrete values may be represented more frequently than others.

This method is equivalent to calling `random(in:using:)`, passing in the system’s default random generator.
