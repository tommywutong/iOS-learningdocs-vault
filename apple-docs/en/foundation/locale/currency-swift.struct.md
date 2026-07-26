---
title: Locale.Currency
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/locale/currency-swift.struct
source_url: 'https://developer.apple.com/documentation/foundation/locale/currency-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/locale/currency-swift.struct.json'
content_hash: 'sha256:9a5ec0df83ca0043'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Locale](../locale.md)

# Locale.Currency

<sub>Structure</sub>

A type that represents the currency system used by a locale, like dollars or euros.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Currency
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [ExpressibleByExtendedGraphemeClusterLiteral](../../swift/expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByStringLiteral](../../swift/expressiblebystringliteral.md), [ExpressibleByUnicodeScalarLiteral](../../swift/expressiblebyunicodescalarliteral.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a currency instance

- [init(_:)](<currency-swift.struct/init(__).md>) — Creates a currency instance from a BCP 47 identifier.
- [init(stringLiteral:)](<currency-swift.struct/init(stringliteral_).md>) — Creates a currency instance from a BCP 47 identifier as a string literal.

### Examining currency properties

- [identifier](currency-swift.struct/identifier.md) — The currency’s identifier.
- [isISOCurrency](currency-swift.struct/isisocurrency.md) — A Boolean value that indicates whether the currency is in the list of ISO-defined currencies.

### Using common currencies

- [isoCurrencies](currency-swift.struct/isocurrencies.md) — An array containing currencies defined by the currency codes in ISO-4217.
- [unknown](currency-swift.struct/unknown.md) — A representation of an “unknown” currency, for use with transactions that don’t involve any currency.

## See Also

### Getting measurement and counting components

- [currency](currency-swift.property.md) — The currency used by the locale.
- [measurementSystem](measurementsystem-swift.property.md) — The measurement system used by the locale, like metric or the US system.
- [MeasurementSystem](measurementsystem-swift.struct.md) — A type that represents the measurement system used by a locale, like metric or the US system.
- [numberingSystem](numberingsystem-swift.property.md) — The numbering system used by the locale.
- [availableNumberingSystems](availablenumberingsystems.md) — An array containing all the valid numbering systems for the locale.
- [NumberingSystem](numberingsystem-swift.struct.md) — A type that represents the numbering system used in a locale.
