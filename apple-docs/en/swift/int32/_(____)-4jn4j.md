---
title: '>(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int32/_(_:_:)-4jn4j'
source_url: 'https://developer.apple.com/documentation/swift/int32/_(_:_:)-4jn4j'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int32/_%28_%3A_%3A%29-4jn4j.json'
content_hash: 'sha256:2ff1fdbcbe16a15b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int32](../int32.md)

# \>(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func > <Other>(lhs: Self, rhs: Other) -> Bool where Other : BinaryInteger
```

## Parameters

- `lhs` — An integer to compare.

- `rhs` — Another integer to compare.

## Discussion

You can compare instances of any `BinaryInteger` types using the greater-than operator (`>`), even if the two instances are of different types.
