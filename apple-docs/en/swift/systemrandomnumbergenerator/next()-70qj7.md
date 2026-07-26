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
doc_path: /documentation/swift/systemrandomnumbergenerator/next()-70qj7
source_url: 'https://developer.apple.com/documentation/swift/systemrandomnumbergenerator/next()-70qj7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/systemrandomnumbergenerator/next%28%29-70qj7.json'
content_hash: 'sha256:fb08dc7f7ef4aefc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SystemRandomNumberGenerator](../systemrandomnumbergenerator.md)

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
