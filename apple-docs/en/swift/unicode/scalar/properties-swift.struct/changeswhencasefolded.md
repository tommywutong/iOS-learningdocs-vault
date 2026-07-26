---
title: changesWhenCaseFolded
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar/properties-swift.struct/changeswhencasefolded
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/changeswhencasefolded'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/properties-swift.struct/changeswhencasefolded.json'
content_hash: 'sha256:e73450ce7f355314'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [Scalar](../../scalar.md) · [Properties](../properties-swift.struct.md)

# changesWhenCaseFolded

<sub>Instance Property</sub>

A Boolean value indicating whether the scalar’s normalized form differs from the case-fold mapping of each constituent scalar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var changesWhenCaseFolded: Bool { get }
```

## Discussion

This property corresponds to the “Changes_When_Casefolded” property in the [Unicode Standard](http://www.unicode.org/versions/latest/).
