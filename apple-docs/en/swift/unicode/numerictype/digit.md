---
title: Unicode.NumericType.digit
framework: Swift
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/numerictype/digit
source_url: 'https://developer.apple.com/documentation/swift/unicode/numerictype/digit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/numerictype/digit.json'
content_hash: 'sha256:b80fa7839fb4c148'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [NumericType](../numerictype.md)

# Unicode.NumericType.digit

<sub>Case</sub>

A digit that does not meet the requirements of the `decimal` numeric type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case digit
```

## Discussion

Scalars with this numeric type are often those that represent a decimal digit but would not typically be used to write a base-10 number, such as “④” (U+2463 CIRCLED DIGIT FOUR).

As of Unicode 6.3, any new scalars that represent numbers but do not meet the requirements of `decimal` will have numeric type `numeric`, and programs can treat `digit` and `numeric` equivalently.
