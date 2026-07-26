---
title: Decimal.FormatStyle.Percent
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/decimal/formatstyle/percent
source_url: 'https://developer.apple.com/documentation/foundation/decimal/formatstyle/percent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal/formatstyle/percent.json'
content_hash: 'sha256:640a230455532de5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Decimal](../../decimal.md) · [FormatStyle](../formatstyle.md)

# Decimal.FormatStyle.Percent

<sub>Structure</sub>

A format style that converts between decimal percentage values and their textual representations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Percent
```

## Relationships

- **Conforms To**: [Copyable](../../../swift/copyable.md), [CustomConsumingRegexComponent](../../../swift/customconsumingregexcomponent.md), [Decodable](../../../swift/decodable.md), [Encodable](../../../swift/encodable.md), [Equatable](../../../swift/equatable.md), [Escapable](../../../swift/escapable.md), [FormatStyle](../../formatstyle.md), [Hashable](../../../swift/hashable.md), [ParseableFormatStyle](../../parseableformatstyle.md), [RegexComponent](../../../swift/regexcomponent.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Creating a decimal percent format style

- [init(locale:)](<percent/init(locale_).md>) — Creates a decimal percent format style that uses the given locale.

### Customizing style behavior

- [decimalSeparator(strategy:)](<percent/decimalseparator(strategy_).md>) — Modifies the format style to use the specified decimal separator display strategy.
- [grouping(_:)](<percent/grouping(__).md>) — Modifies the format style to use the specified grouping.
- [locale(_:)](<percent/locale(__).md>) — Modifies the format style to use the specified locale.
- [notation(_:)](<percent/notation(__).md>) — Modifies the format style to use the specified notation.
- [precision(_:)](<percent/precision(__).md>) — Modifies the format style to use the specified precision.
- [rounded(rule:increment:)](<percent/rounded(rule_increment_).md>) — Modifies the format style to use the specified rounding rule and increment.
- [scale(_:)](<percent/scale(__).md>) — Modifies the format style to use the specified scale.
- [sign(strategy:)](<percent/sign(strategy_).md>) — Modifies the format style to use the specified sign display strategy.
- [Configuration](percent/configuration.md) — The type the format style uses for configuration settings.
- [NumberFormatStyleConfiguration](../../numberformatstyleconfiguration.md) — Configuration settings for formatting numbers of different types.

### Formatting decimal percent values

- [format(_:)](<percent/format(__).md>) — Formats an decimal, using this style.

### Creating attributed strings

- [attributed](percent/attributed.md) — An attributed format style based on the decimal percent format style.
- [Attributed](attributed-swift.struct.md) — A format style that converts integers into attributed strings.

### Accessing style properties

- [locale](percent/locale.md) — The locale of the format style.

### Parsing decimal percent values

- [parseStrategy](percent/parsestrategy.md) — The parse strategy that this format style uses.

### Locating decimal values in regular expressions

- [consuming(_:startingAt:in:)](<percent/consuming(__startingat_in_).md>) — Process the input string within the specified bounds, beginning at the given index, and return the end position (upper bound) of the match and the produced output.

### Default Implementations

- [CustomConsumingRegexComponent Implementations](percent/customconsumingregexcomponent-implementations.md)
- [ParseableFormatStyle Implementations](percent/parseableformatstyle-implementations.md)

## See Also

### Supporting types

- [Currency](currency.md) — A format style that converts between decimal currency values and their textual representations.
