---
title: 'next(upperBound:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/systemrandomnumbergenerator/next(upperbound:)'
source_url: 'https://developer.apple.com/documentation/swift/systemrandomnumbergenerator/next(upperbound:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/systemrandomnumbergenerator/next%28upperbound%3A%29.json'
content_hash: 'sha256:3f376ed403304cbc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SystemRandomNumberGenerator](../systemrandomnumbergenerator.md)

# next(upperBound:)

<sub>Instance Method</sub>

Returns a random value that is less than the given upper bound.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next<T>(upperBound: T) -> T where T : FixedWidthInteger, T : UnsignedInteger
```

## Parameters

- `upperBound` — The upper bound for the randomly generated value. Must be non-zero.

## Return Value

A random value of `T` in the range `0..<upperBound`. Every value in the range `0..<upperBound` is equally likely to be returned.

## Discussion

Use this method when you need random binary data to generate another value. If you need an integer value within a specific range, use the static `random(in:using:)` method on that integer type instead of this method.

## See Also

### Generating Random Binary Data

- [next()](<next().md>) — Returns a value from a uniform, independent distribution of binary data.
- [next()](<next()-2x0ly.md>) — Returns a value from a uniform, independent distribution of binary data.
