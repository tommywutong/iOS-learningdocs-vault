---
title: identifier
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/identifier
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/identifier.json'
content_hash: 'sha256:4573b579d5227917'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# identifier

<sub>Instance Property</sub>

The string that represents the type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var identifier: String { get }
```

## Discussion

The identifier uniquely identifies its type, represented by a reverse-DNS string, such as `public.jpeg` or `com.adobe.pdf`.

API that doesn’t use [UTType](../uttype-swift.struct.md) uses a `String` or [CFString](../../corefoundation/cfstring.md) to refer to a type by its identifier.

## See Also

### Identifying a type

- [ReferenceType](referencetype.md) — An alias for the associated reference type.
