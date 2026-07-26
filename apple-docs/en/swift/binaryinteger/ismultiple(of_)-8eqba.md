---
title: 'isMultiple(of:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/binaryinteger/ismultiple(of:)-8eqba'
source_url: 'https://developer.apple.com/documentation/swift/binaryinteger/ismultiple(of:)-8eqba'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryinteger/ismultiple%28of%3A%29-8eqba.json'
content_hash: 'sha256:986b0bd79c2a0265'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BinaryInteger](../binaryinteger.md)

# isMultiple(of:)

<sub>Instance Method</sub>

Returns `true` if this value is a multiple of the given value, and `false` otherwise.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isMultiple(of other: Self) -> Bool
```

## Parameters

- `other` — The value to test.

## Discussion

For two integers _a_ and _b_, _a_ is a multiple of _b_ if there exists a third integer _q_ such that _a = q*b_. For example, _6_ is a multiple of _3_ because _6 = 2*3_. Zero is a multiple of everything because _0 = 0*x_ for any integer _x_.

Two edge cases are worth particular attention:

- `x.isMultiple(of: 0)` is `true` if `x` is zero and `false` otherwise.
- `T.min.isMultiple(of: -1)` is `true` for signed integer `T`, even though the quotient `T.min / -1` isn’t representable in type `T`.
