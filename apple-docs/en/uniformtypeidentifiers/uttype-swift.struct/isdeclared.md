---
title: isDeclared
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/isdeclared
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/isdeclared'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/isdeclared.json'
content_hash: 'sha256:e5d01235e5fb6942'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

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

- [isDynamic](isdynamic.md) — A Boolean value that indicates whether the system generates the type.
- [isPublic](ispublic.md) — A Boolean value that indicates whether the type is in the public domain.
- [referenceURL](referenceurl.md) — The reference URL for the type.
- [version](version.md) — The type’s version, if available.
