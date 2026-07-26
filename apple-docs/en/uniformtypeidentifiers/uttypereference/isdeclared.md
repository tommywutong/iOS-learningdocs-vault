---
title: isDeclared
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypereference/isdeclared
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/isdeclared'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypereference/isdeclared.json'
content_hash: 'sha256:8722f233f0cbf3ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTTypeReference](../uttypereference.md)

# isDeclared

<sub>Instance Property</sub>

A Boolean value that indicates whether the system declares the type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isDeclared: Bool { get }
```

## Discussion

The system either declares a type or dynamically generates a type, but not both.

## See Also

### Obtaining additional type information

- [dynamic](isdynamic.md) — A Boolean value that indicates whether the system generates the type.
- [publicType](ispublic.md) — A Boolean value that indicates whether the type is in the public domain.
- [referenceURL](../uttype-swift.struct/referenceurl.md) — The reference URL for the type.
- [version](../uttype-swift.struct/version.md) — The type’s version, if available.
