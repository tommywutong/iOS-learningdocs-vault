---
title: 'random(using:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/bool/random(using:)'
source_url: 'https://developer.apple.com/documentation/swift/bool/random(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bool/random%28using%3A%29.json'
content_hash: 'sha256:98abd4d836c149ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Bool](../bool.md)

# random(using:)

<sub>Type Method</sub>

Returns a random Boolean value, using the given generator as a source for randomness.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func random<T>(using generator: inout T) -> Bool where T : RandomNumberGenerator
```

## Parameters

- `generator` — The random number generator to use when creating the new random value.

## Return Value

Either `true` or `false`, randomly chosen with equal probability.

## Discussion

This method returns `true` and `false` with equal probability. Use this method to generate a random Boolean value when you are using a custom random number generator.

```swift
let flippedHeads = Bool.random(using: &myGenerator)
if flippedHeads {
    print("Heads, you win!")
} else {
    print("Maybe another try?")
}
```

> [!note] Note
> The algorithm used to create random values may change in a future version of Swift. If you’re passing a generator that results in the same sequence of Boolean values each time you run your program, that sequence may change when your program is compiled using a different version of Swift.

## See Also

### Creating a Random Value

- [random()](<random().md>) — Returns a random Boolean value.
