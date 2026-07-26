---
title: Locale.NumberingSystem
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/numberingsystem-swift.struct
source_url: 'https://developer.apple.com/documentation/foundation/locale/numberingsystem-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/numberingsystem-swift.struct.json'
content_hash: 'sha256:c27873ed939fd521'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# Locale.NumberingSystem

<sub>Structure</sub>

A type that represents the numbering system used in a locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NumberingSystem
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [ExpressibleByExtendedGraphemeClusterLiteral](../../swift/expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByStringLiteral](../../swift/expressiblebystringliteral.md), [ExpressibleByUnicodeScalarLiteral](../../swift/expressiblebyunicodescalarliteral.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a numbering system instance

- [init(_:)](<numberingsystem-swift.struct/init(__).md>) — Creates a numbering system instance from a BCP 47 identifier.
- [init(stringLiteral:)](<numberingsystem-swift.struct/init(stringliteral_).md>) — Creates a numbering system instance from a BCP 47 identifier as a string literal.

### Examining numbering system properties

- [identifier](numberingsystem-swift.struct/identifier.md) — The numbering system’s BCP 47 identifier.

### Type Properties

- [availableNumberingSystems](numberingsystem-swift.struct/availablenumberingsystems.md) — A list of available numbering systems on the system.

## See Also

### Getting measurement and counting components

- [currency](currency-swift.property.md) — The currency used by the locale.
- [Currency](currency-swift.struct.md) — A type that represents the currency system used by a locale, like dollars or euros.
- [measurementSystem](measurementsystem-swift.property.md) — The measurement system used by the locale, like metric or the US system.
- [MeasurementSystem](measurementsystem-swift.struct.md) — A type that represents the measurement system used by a locale, like metric or the US system.
- [numberingSystem](numberingsystem-swift.property.md) — The numbering system used by the locale.
- [availableNumberingSystems](availablenumberingsystems.md) — An array containing all the valid numbering systems for the locale.
