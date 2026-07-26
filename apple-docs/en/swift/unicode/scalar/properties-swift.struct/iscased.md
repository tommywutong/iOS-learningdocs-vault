---
title: isCased
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/iscased
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/iscased'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/iscased.json'
content_hash: 'sha256:60f2020a7de24f4b'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# isCased

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar is considered to be either lowercase, uppercase, or titlecase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isCased: Bool { get }
```

## Discussion

Though similar in name, this property is _not_ equivalent to `changesWhenCaseMapped`. The set of scalars for which `isCased` is `true` is a superset of those for which `changesWhenCaseMapped` is `true`. For example, the Latin small capitals that are used by the International Phonetic Alphabet have a case, but do not change when they are mapped to any of the other cases.

This property corresponds to the “Cased” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
