---
title: next()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/randomnumbergenerator/next()
source_url: 'https://developer.apple.com/documentation/swift/randomnumbergenerator/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/randomnumbergenerator/next%28%29.json'
content_hash: 'sha256:26a432175408f248'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RandomNumberGenerator](../randomnumbergenerator.md)

# next()

<sub>Instance Method</sub>

Returns a value from a uniform, independent distribution of binary data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() -> UInt64
```

## Return Value

An unsigned 64-bit random value.

## Discussion

Use this method when you need random binary data to generate another value. If you need an integer value within a specific range, use the static `random(in:using:)` method on that integer type instead of this method.

## Default Implementations

### RandomNumberGenerator Implementations

- [next()](<next()-6auxg.md>) — Returns a value from a uniform, independent distribution of binary data.

## See Also

### Generating Random Binary Data

- [next(upperBound:)](<next(upperbound_).md>) — Returns a random value that is less than the given upper bound.
