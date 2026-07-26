---
title: Locale.Subdivision
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/subdivision-swift.struct
source_url: 'https://developer.apple.com/documentation/foundation/locale/subdivision-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/subdivision-swift.struct.json'
content_hash: 'sha256:9801567063092c89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# Locale.Subdivision

<sub>Structure</sub>

A type that represents a subdivision of a region, such as a state in the US or a province in Canada.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Subdivision
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [ExpressibleByExtendedGraphemeClusterLiteral](../../swift/expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByStringLiteral](../../swift/expressiblebystringliteral.md), [ExpressibleByUnicodeScalarLiteral](../../swift/expressiblebyunicodescalarliteral.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a subdivision

- [init(_:)](<subdivision-swift.struct/init(__).md>) — Creates a sudivision from a Unicode identifier.
- [subdivision(for:)](<subdivision-swift.struct/subdivision(for_).md>) — Returns the subdivision representing the given region as a whole.
- [init(stringLiteral:)](<subdivision-swift.struct/init(stringliteral_).md>) — Creates a sudivision from a Unicode identifier as a string literal.

### Examining subdivision properties

- [identifier](subdivision-swift.struct/identifier.md) — The subdivision’s Unicode identifier.

## See Also

### Getting region components

- [region](region-swift.property.md) — The region used by the locale.
- [Region](region-swift.struct.md) — A type that represents a geographic region, for use in specifying a locale or language.
- [subdivision](subdivision-swift.property.md) — The optional subdivision of the region used by this locale.
- [variant](variant-swift.property.md) — An optional variant used by the locale.
- [Variant](variant-swift.struct.md) — A type that represents a locale’s language variant.
