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
doc_path: '/documentation/swift/float16/random(in:using:)-1prt0'
source_url: 'https://developer.apple.com/documentation/swift/float16/random(in:using:)-1prt0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/random%28in%3Ausing%3A%29-1prt0.json'
content_hash: 'sha256:7b05ec980e9efa14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# random(in:using:)

<sub>Type Method</sub>

Returns a random value within the specified range, using the given generator as a source for randomness.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func random<T>(in range: ClosedRange<Self>, using generator: inout T) -> Self where T : RandomNumberGenerator
```

## Parameters

- `range` — The range in which to create a random value. Must be finite.

- `generator` — The random number generator to use when creating the new random value.

## Return Value

A random value within the bounds of `range`.

## Discussion

Use this method to generate a floating-point value within a specific range when you are using a custom random number generator. This example creates three new values in the range `10.0 ... 20.0`.

```swift
for _ in 1...3 {
    print(Double.random(in: 10.0 ... 20.0, using: &myGenerator))
}
// Prints "18.1900709259179"
// Prints "14.2286325689993"
// Prints "13.1485686260762"
```

The `random(in:using:)` static method chooses a random value from a continuous uniform distribution in `range`, and then converts that value to the nearest representable value in this type. Depending on the size and span of `range`, some concrete values may be represented more frequently than others.

> [!note] Note
> The algorithm used to create random values may change in a future version of Swift. If you’re passing a generator that results in the same sequence of floating-point values each time you run your program, that sequence may change when your program is compiled using a different version of Swift.
