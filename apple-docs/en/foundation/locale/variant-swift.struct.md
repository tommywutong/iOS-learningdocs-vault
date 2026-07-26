---
title: Locale.Variant
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/variant-swift.struct
source_url: 'https://developer.apple.com/documentation/foundation/locale/variant-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/variant-swift.struct.json'
content_hash: 'sha256:1eea00b14c9b0d2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# Locale.Variant

<sub>Structure</sub>

A type that represents a locale’s language variant.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Variant
```

## Overview

This type corresponds to the Unicode variant subtag, such as `posix`.

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [ExpressibleByExtendedGraphemeClusterLiteral](../../swift/expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByStringLiteral](../../swift/expressiblebystringliteral.md), [ExpressibleByUnicodeScalarLiteral](../../swift/expressiblebyunicodescalarliteral.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a variant

- [init(_:)](<variant-swift.struct/init(__).md>) — Creates a variant from a BCP 47 identifier.
- [init(stringLiteral:)](<variant-swift.struct/init(stringliteral_).md>) — Creates a variant from a BCP 47 identifier as a string literal.

### Examining variant properties

- [identifier](variant-swift.struct/identifier.md) — The variant’s BCP 47 identifier.

### Using defined variants

- [posix](variant-swift.struct/posix.md)

## See Also

### Getting region components

- [region](region-swift.property.md) — The region used by the locale.
- [Region](region-swift.struct.md) — A type that represents a geographic region, for use in specifying a locale or language.
- [subdivision](subdivision-swift.property.md) — The optional subdivision of the region used by this locale.
- [Subdivision](subdivision-swift.struct.md) — A type that represents a subdivision of a region, such as a state in the US or a province in Canada.
- [variant](variant-swift.property.md) — An optional variant used by the locale.
