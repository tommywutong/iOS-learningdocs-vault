---
title: Unicode.NumericType.numeric
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/numerictype/numeric
source_url: 'https://developer.apple.com/documentation/swift/unicode/numerictype/numeric'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/numerictype/numeric.json'
content_hash: 'sha256:70d029f501d01d0b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [NumericType](../numerictype.md)

# Unicode.NumericType.numeric

<sub>Case</sub>

A digit that does not meet the requirements of the `decimal` numeric type or a non-digit numeric value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case numeric
```

## Discussion

This numeric type includes fractions such as “⅕” (U+2155 VULGAR FRACTION ONE FIFTH), numerical CJK ideographs like “兆” (U+5146 CJK UNIFIED IDEOGRAPH-5146), and other scalars that are not decimal digits used positionally in the writing of base-10 numbers.

As of Unicode 6.3, any new scalars that represent numbers but do not meet the requirements of `decimal` will have numeric type `numeric`, and programs can treat `digit` and `numeric` equivalently.
