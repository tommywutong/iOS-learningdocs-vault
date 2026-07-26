---
title: changesWhenCaseMapped
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/changeswhencasemapped
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/changeswhencasemapped'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/changeswhencasemapped.json'
content_hash: 'sha256:a7a45a11dba2ec05'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# changesWhenCaseMapped

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar may change when it undergoes case mapping.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var changesWhenCaseMapped: Bool { get }
```

## Discussion

This property is `true` whenever one or more of `changesWhenLowercased`, `changesWhenUppercased`, or `changesWhenTitlecased` are `true`.

This property corresponds to the “Changes_When_Casemapped” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
