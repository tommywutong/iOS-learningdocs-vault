---
title: referenceURL
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/referenceurl
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/referenceurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/referenceurl.json'
content_hash: 'sha256:7a0a76e14d51e1e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# referenceURL

<sub>Instance Property</sub>

The reference URL for the type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var referenceURL: URL? { get }
```

## Discussion

A reference URL is a human-readable document that describes a type. Most types don’t specify reference URLs.

> [!warning] Warning
> The system doesn’t validate the URL, nor does it guarantee its scheme or structure.

## See Also

### Obtaining additional type information

- [isDeclared](isdeclared.md) — A Boolean value that indicates whether the system declares the type.
- [isDynamic](isdynamic.md) — A Boolean value that indicates whether the system generates the type.
- [isPublic](ispublic.md) — A Boolean value that indicates whether the type is in the public domain.
- [version](version.md) — The type’s version, if available.
