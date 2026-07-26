---
title: IntegerFormatStyle.Percent
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/integerformatstyle/percent
source_url: 'https://developer.apple.com/documentation/foundation/integerformatstyle/percent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/integerformatstyle/percent.json'
content_hash: 'sha256:bb706580cf2f4260'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IntegerFormatStyle](../integerformatstyle.md)

# IntegerFormatStyle.Percent

<sub>Structure</sub>

A format style that converts between integer percentage values and their textual representations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Percent
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomConsumingRegexComponent](../../swift/customconsumingregexcomponent.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [FormatStyle](../formatstyle.md), [Hashable](../../swift/hashable.md), [ParseableFormatStyle](../parseableformatstyle.md), [RegexComponent](../../swift/regexcomponent.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating an integer percent format style

- [init(locale:)](<percent/init(locale_).md>) — Creates an integer percent format style that uses the given locale.

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
- [NumberFormatStyleConfiguration](../numberformatstyleconfiguration.md) — Configuration settings for formatting numbers of different types.

### Formatting integer percent values

- [format(_:)](<percent/format(__).md>) — Formats an integer, using this style.

### Creating attributed strings

- [attributed](percent/attributed.md) — An attributed format style based on the integer percent format style.
- [Attributed](attributed-swift.struct.md) — A format style that converts integers into attributed strings.

### Accessing style properties

- [locale](percent/locale.md) — The locale of the format style.

### Parsing integer percent values

- [parseStrategy](percent/parsestrategy.md) — The parse strategy that this format style uses.

### Locating percent values in regular expressions

- [consuming(_:startingAt:in:)](<percent/consuming(__startingat_in_).md>) — Process the input string within the specified bounds, beginning at the given index, and return the end position (upper bound) of the match and the produced output.

### Default Implementations

- [CustomConsumingRegexComponent Implementations](percent/customconsumingregexcomponent-implementations.md)
- [FormatStyle Implementations](percent/formatstyle-implementations.md)
- [ParseableFormatStyle Implementations](percent/parseableformatstyle-implementations.md)

## See Also

### Applying percentage styles for integers

- [percent](../formatstyle/percent-cl9k.md) — A style for formatting signed integer types in Swift as a percent representation.
- [percent](../formatstyle/percent-9pj79.md) — A style for formatting signed integer types in Swift as a percent representation.
- [percent](../formatstyle/percent-7r4rl.md) — A style for formatting 8-bit signed integers as a percent representation.
- [percent](../formatstyle/percent-3qjzh.md) — A style for formatting 16-bit signed integers as a percent representation.
- [percent](../formatstyle/percent-1f0q.md) — A style for formatting 32-bit signed integers as a percent representation.
- [percent](../formatstyle/percent-934se.md) — A style for formatting 64-bit signed integers as a percent representation.
- [percent](../formatstyle/percent-8izzv.md) — A style for formatting 8-bit unsigned integers as a percent representation.
- [percent](../formatstyle/percent-4kdme.md) — A style for formatting 16-bit unsigned integers as a percent representation.
- [percent](../formatstyle/percent-2f11j.md) — A style for formatting 32-bit unsigned integers as a percent representation.
- [percent](../formatstyle/percent-8bxla.md) — A style for formatting 64-bit unsigned integers as a percent representation.
