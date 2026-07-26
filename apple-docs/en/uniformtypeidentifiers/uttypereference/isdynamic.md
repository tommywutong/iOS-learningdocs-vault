---
title: isDynamic
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypereference/isdynamic
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/isdynamic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypereference/isdynamic.json'
content_hash: 'sha256:443d1dd756f84fb3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTTypeReference](../uttypereference.md)

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

- [declared](isdeclared.md) — A Boolean value that indicates whether the system declares the type.
- [publicType](ispublic.md) — A Boolean value that indicates whether the type is in the public domain.
- [referenceURL](../uttype-swift.struct/referenceurl.md) — The reference URL for the type.
- [version](../uttype-swift.struct/version.md) — The type’s version, if available.
