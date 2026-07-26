---
title: random()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/bool/random()
source_url: 'https://developer.apple.com/documentation/swift/bool/random()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bool/random%28%29.json'
content_hash: 'sha256:5ad60200a874c2ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Bool](../bool.md)

# random()

<sub>Type Method</sub>

Returns a random Boolean value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func random() -> Bool
```

## Return Value

Either `true` or `false`, randomly chosen with equal probability.

## Discussion

This method returns `true` and `false` with equal probability.

```swift
let flippedHeads = Bool.random()
if flippedHeads {
    print("Heads, you win!")
} else {
    print("Maybe another try?")
}
```

This method is equivalent to calling `Bool.random(using:)`, passing in the system’s default random generator.

## See Also

### Creating a Random Value

- [random(using:)](<random(using_).md>) — Returns a random Boolean value, using the given generator as a source for randomness.
