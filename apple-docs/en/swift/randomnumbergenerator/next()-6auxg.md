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
doc_path: /documentation/swift/randomnumbergenerator/next()-6auxg
source_url: 'https://developer.apple.com/documentation/swift/randomnumbergenerator/next()-6auxg'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/randomnumbergenerator/next%28%29-6auxg.json'
content_hash: 'sha256:cbad7586d7f4ccd8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RandomNumberGenerator](../randomnumbergenerator.md)

# next()

<sub>Instance Method</sub>

Returns a value from a uniform, independent distribution of binary data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next<T>() -> T where T : FixedWidthInteger, T : UnsignedInteger
```

## Return Value

A random value of `T`. Bits are randomly distributed so that every value of `T` is equally likely to be returned.

## Discussion

Use this method when you need random binary data to generate another value. If you need an integer value within a specific range, use the static `random(in:using:)` method on that integer type instead of this method.
