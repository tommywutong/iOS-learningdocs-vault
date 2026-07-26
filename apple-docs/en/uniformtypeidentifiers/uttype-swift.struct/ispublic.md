---
title: isPublic
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/ispublic
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/ispublic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/ispublic.json'
content_hash: 'sha256:fd0d7f1b48a31a13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

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

- [isDeclared](isdeclared.md) — A Boolean value that indicates whether the system declares the type.
- [isDynamic](isdynamic.md) — A Boolean value that indicates whether the system generates the type.
- [referenceURL](referenceurl.md) — The reference URL for the type.
- [version](version.md) — The type’s version, if available.
