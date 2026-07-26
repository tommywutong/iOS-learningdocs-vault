---
title: isDynamic
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/isdynamic
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/isdynamic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/isdynamic.json'
content_hash: 'sha256:40436b4ed39d0b7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# isDynamic

<sub>Instance Property</sub>

A Boolean value that indicates whether the system generates the type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isDynamic: Bool { get }
```

## Discussion

The system recognizes dynamic types, but they may not be directly declared or claimed by an app. The system returns dynamic types when it encounters a file whose metadata doesn’t have a corresponding type known to the system.

The system either declares a type or dynamically generates a type, but not both.

## See Also

### Obtaining additional type information

- [isDeclared](isdeclared.md) — A Boolean value that indicates whether the system declares the type.
- [isPublic](ispublic.md) — A Boolean value that indicates whether the type is in the public domain.
- [referenceURL](referenceurl.md) — The reference URL for the type.
- [version](version.md) — The type’s version, if available.
