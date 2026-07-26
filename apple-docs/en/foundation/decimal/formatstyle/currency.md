---
title: Decimal.FormatStyle.Currency
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/decimal/formatstyle/currency
source_url: 'https://developer.apple.com/documentation/foundation/decimal/formatstyle/currency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal/formatstyle/currency.json'
content_hash: 'sha256:504bf87526932998'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Decimal](../../decimal.md) · [FormatStyle](../formatstyle.md)

# Decimal.FormatStyle.Currency

<sub>Structure</sub>

A format style that converts between decimal currency values and their textual representations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Currency
```

## Relationships

- **Conforms To**: [Copyable](../../../swift/copyable.md), [CustomConsumingRegexComponent](../../../swift/customconsumingregexcomponent.md), [Decodable](../../../swift/decodable.md), [Encodable](../../../swift/encodable.md), [Equatable](../../../swift/equatable.md), [Escapable](../../../swift/escapable.md), [FormatStyle](../../formatstyle.md), [Hashable](../../../swift/hashable.md), [ParseableFormatStyle](../../parseableformatstyle.md), [RegexComponent](../../../swift/regexcomponent.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Creating a decimal currency style

- [init(code:locale:)](<currency/init(code_locale_).md>) — Creates a decimal currency format style that uses the given currency code and locale.

### Customizing style behavior

- [decimalSeparator(strategy:)](<currency/decimalseparator(strategy_).md>) — Modifies the format style to use the specified decimal separator display strategy.
- [grouping(_:)](<currency/grouping(__).md>) — Modifies the format style to use the specified grouping.
- [locale(_:)](<currency/locale(__).md>) — Modifies the format style to use the specified locale.
- [precision(_:)](<currency/precision(__).md>) — Modifies the format style to use the specified precision.
- [presentation(_:)](<currency/presentation(__).md>) — Modifies the format style to use the specified presentation.
- [rounded(rule:increment:)](<currency/rounded(rule_increment_).md>) — Modifies the format style to use the specified rounding rule and increment.
- [scale(_:)](<currency/scale(__).md>) — Modifies the format style to use the specified scale.
- [sign(strategy:)](<currency/sign(strategy_).md>) — Modifies the format style to use the specified sign display strategy.
- [Configuration](currency/configuration.md) — The type the format style uses for configuration settings.
- [CurrencyFormatStyleConfiguration](../../currencyformatstyleconfiguration.md) — Configuration settings for formatting currency values.

### Formatting decimal currency values

- [format(_:)](<currency/format(__).md>) — Formats a decimal value, using this style.

### Creating attributed strings

- [attributed](currency/attributed.md) — An attributed format style based on the decimal currency format style.
- [Attributed](attributed-swift.struct.md) — A format style that converts integers into attributed strings.

### Accessing style properties

- [currencyCode](currency/currencycode.md) — The currency code this format style uses.
- [locale](currency/locale.md) — The locale of the format style.

### Parsing decimal currency values

- [parseStrategy](currency/parsestrategy.md) — The parse strategy that this format style uses.

### Locating currency values in regular expressions

- [consuming(_:startingAt:in:)](<currency/consuming(__startingat_in_).md>) — Process the input string within the specified bounds, beginning at the given index, and return the end position (upper bound) of the match and the produced output.

### Instance Methods

- [notation(_:)](<currency/notation(__).md>) — Modifies the format style to use the specified notation.

### Default Implementations

- [CustomConsumingRegexComponent Implementations](currency/customconsumingregexcomponent-implementations.md)
- [ParseableFormatStyle Implementations](currency/parseableformatstyle-implementations.md)
