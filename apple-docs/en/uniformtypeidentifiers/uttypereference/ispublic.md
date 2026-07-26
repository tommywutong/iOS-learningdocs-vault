---
title: isPublic
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypereference/ispublic
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/ispublic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypereference/ispublic.json'
content_hash: 'sha256:b95314967a35ec55'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTTypeReference](../uttypereference.md)

# isPublic

<sub>Instance Property</sub>

A Boolean value that indicates whether the type is in the public domain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isPublic: Bool { get }
```

## Discussion

Types in the public domain have identifiers starting with `public`, and are generally defined by a standards body or by convention. Public types aren’t dynamic.

## See Also

### Obtaining additional type information

- [declared](isdeclared.md) — A Boolean value that indicates whether the system declares the type.
- [dynamic](isdynamic.md) — A Boolean value that indicates whether the system generates the type.
- [referenceURL](../uttype-swift.struct/referenceurl.md) — The reference URL for the type.
- [version](../uttype-swift.struct/version.md) — The type’s version, if available.
