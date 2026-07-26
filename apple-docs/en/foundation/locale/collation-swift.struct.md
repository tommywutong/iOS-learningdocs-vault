---
title: Locale.Collation
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/collation-swift.struct
source_url: 'https://developer.apple.com/documentation/foundation/locale/collation-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/collation-swift.struct.json'
content_hash: 'sha256:ba040e08835d9a0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# Locale.Collation

<sub>Structure</sub>

A type that represents the string sort order used by the locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Collation
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [ExpressibleByExtendedGraphemeClusterLiteral](../../swift/expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByStringLiteral](../../swift/expressiblebystringliteral.md), [ExpressibleByUnicodeScalarLiteral](../../swift/expressiblebyunicodescalarliteral.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a collation

- [init(_:)](<collation-swift.struct/init(__).md>) — Creates a collation from a BCP 47 identifier.
- [init(stringLiteral:)](<collation-swift.struct/init(stringliteral_).md>) — Creates a collation from a BCP 47 identifier as a string literal.

### Examining collation properties

- [identifier](collation-swift.struct/identifier.md) — The collation’s BCP 47 identifier.

### Using special-purpose collations

- [standard](collation-swift.struct/standard.md) — A collation that provides the default ordering for each language.
- [searchRules](collation-swift.struct/searchrules.md) — A collation used for string search.

### Type Properties

- [availableCollations](collation-swift.struct/availablecollations.md) — A list of available collations on the system.

### Type Methods

- [availableCollations(for:)](<collation-swift.struct/availablecollations(for_).md>) — A list of available collations for the specified `language` in the order that it is most likely to make a difference.

## See Also

### Getting ordering components

- [collation](collation-swift.property.md) — The string sort order of the locale.
