---
title: Decimal.FormatStyle
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/decimal/formatstyle
source_url: 'https://developer.apple.com/documentation/foundation/decimal/formatstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal/formatstyle.json'
content_hash: 'sha256:377302b13ec38949'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Decimal](../decimal.md)

# Decimal.FormatStyle

<sub>Structure</sub>

A structure that converts between decimal values and their textual representations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FormatStyle
```

## Overview

Instances of [FormatStyle](formatstyle.md) create localized, human-readable text from [Decimal](../decimal.md) numbers and parse string representations of numbers into instances of [Decimal](../decimal.md).

[FormatStyle](formatstyle.md) includes two nested types, [Percent](formatstyle/percent.md) and [Currency](formatstyle/currency.md), for working with percentages and currencies, respectively. Each format style includes a configuration that determines how it represents numeric values, for things like grouping, displaying signs, and variant presentations like scientific notation. [FormatStyle](formatstyle.md) and [Percent](formatstyle/percent.md) include a [NumberFormatStyleConfiguration](../numberformatstyleconfiguration.md), and [Currency](formatstyle/currency.md) includes a [CurrencyFormatStyleConfiguration](../currencyformatstyleconfiguration.md). You can customize numeric formatting for a style by adjusting its backing configuration. The system automatically caches unique configurations of a format style to enhance performance.

> [!note] Note
> Foundation provides other format style types for working with the numeric types that the Swift standard library defines. [IntegerFormatStyle](../integerformatstyle.md) works with types that conform to [BinaryInteger](../../swift/binaryinteger.md), and [FloatingPointFormatStyle](../floatingpointformatstyle.md) works with types that conform to [BinaryFloatingPoint](../../swift/binaryfloatingpoint.md).

### Formatting decimal values

Use the [formatted()](<formatted().md>) method to create a string representation of a decimal value using the default [FormatStyle](formatstyle.md) configuration:

```swift
let formattedDefault = Decimal(12345.67).formatted()
// formattedDefault is "12,345.67" in en_US locale.
// Other locales may use different separator and grouping behavior.
```

You can specify a format style by providing an argument to the [formatted(_:)](<formatted(__).md>) method. The following example shows the decimal `0.1` represented in each of the available styles in the `en_US` locale:

```swift
let number: Decimal = 0.1

let formattedNumber = number.formatted(.number)
// formattedNumber is "0.1"

let formattedPercent = number.formatted(.percent)
// formattedPercent is "10%"

let formattedCurrency = number.formatted(.currency(code: "USD"))
// formattedCurrency is "$0.10"
```

Each style provides methods for updating its numeric configuration, including the number of significant digits, grouping length, and more. You can specify a numeric configuration by calling as many of these methods as you need in any order you choose. The following example shows the same number with default and custom configurations:

```swift
let exampleNumber: Decimal = 125000.12

let defaultFormatting = exampleNumber.formatted(.number)
// defaultFormatting is "125 000,12" for the "fr_FR" locale
// defaultFormatting is "125,000.12" for the "en_US" locale

let customFormatting = exampleNumber.formatted(
    .number
    .grouping(.never)
    .sign(strategy: .always()))
// customFormatting is "+125000.12"
```

### Creating a decimal format style instance

The previous examples use static instances like [number](../formatstyle/number-3luf2.md) to create format styles within the call to the [formatted(_:)](<formatted(__).md>) method. You can also create a [FormatStyle](formatstyle.md) instance and use it to repeatedly format different values by using the [format(_:)](<formatstyle/format(__).md>) method, as shown here:

```swift
let percentFormatStyle = Decimal.FormatStyle.Percent()

percentFormatStyle.format(0.5) // "50%"
percentFormatStyle.format(0.855) // "85.5%"
percentFormatStyle.format(1.0) // "100%"
```

### Parsing decimal values

You can use [FormatStyle](formatstyle.md) to parse strings into decimal values. You can define the format style within the type’s initializer or pass in a format style created outside the function. The following demonstrates both approaches:

```swift
let price = try? Decimal("$3,500.63",
                         format: .currency(code: "USD")) // 3500.63

let priceFormatStyle = Decimal.FormatStyle.Currency(code: "USD")
let salePrice = try? Decimal("$731.67",
                             format: priceFormatStyle) // 731.67
```

### Matching regular expressions

Along with parsing numeric values in strings, you can use the Swift regular expression domain-specific language to match and capture numeric substrings. The following example defines a currency format style to match and capture a currency value using US dollars and `en_US` numeric conventions. The rest of the regular expression ignores any characters prior to a `": "` sequence that precedes the currency substring.

```swift
import RegexBuilder
let source = "Payment due: $49,525.99"
let matcher = Regex {
    OneOrMore(.any)
    ": "
    Capture {
        One(.localizedCurrency(code:Locale.Currency("USD"),
                               locale:Locale(identifier: "en_US")))
    }
}
let match = source.firstMatch(of: matcher)
let localizedDecimal = match?.1 // 49525.99
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomConsumingRegexComponent](../../swift/customconsumingregexcomponent.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [FormatStyle](../formatstyle.md), [Hashable](../../swift/hashable.md), [ParseableFormatStyle](../parseableformatstyle.md), [RegexComponent](../../swift/regexcomponent.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a decimal format style

- [init(locale:)](<formatstyle/init(locale_).md>) — Creates a decimal format style that uses the given locale.

### Formatting decimal values

- [format(_:)](<formatstyle/format(__).md>) — Formats a decimal value using this style.

### Customizing style behavior

- [decimalSeparator(strategy:)](<formatstyle/decimalseparator(strategy_).md>) — Modifies the format style to use the specified decimal separator display strategy.
- [grouping(_:)](<formatstyle/grouping(__).md>) — Modifies the format style to use the specified grouping.
- [locale(_:)](<formatstyle/locale(__).md>) — Modifies the format style to use the specified locale.
- [notation(_:)](<formatstyle/notation(__).md>) — Modifies the format style to use the specified notation.
- [precision(_:)](<formatstyle/precision(__).md>) — Modifies the format style to use the specified precision.
- [rounded(rule:increment:)](<formatstyle/rounded(rule_increment_).md>) — Modifies the format style to use the specified rounding rule and increment.
- [scale(_:)](<formatstyle/scale(__).md>) — Modifies the format style to use the specified scale.
- [sign(strategy:)](<formatstyle/sign(strategy_).md>) — Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [Configuration](formatstyle/configuration.md) — The type the format style uses for configuration settings.
- [NumberFormatStyleConfiguration](../numberformatstyleconfiguration.md) — Configuration settings for formatting numbers of different types.

### Accesssing style locale

- [locale](formatstyle/locale.md) — The locale of the format style.

### Applying currency styles

- [Currency](formatstyle/currency.md) — A format style that converts between decimal currency values and their textual representations.

### Applying measurement styles

- [FormatStyle](../measurement/formatstyle.md) — A type that provides localized representations of measurements.

### Creating attributed strings

- [attributed](formatstyle/attributed-swift.property.md) — An attributed format style based on the decimal format style.
- [Attributed](formatstyle/attributed-swift.struct.md) — A format style that converts integers into attributed strings.

### Parsing decimals

- [parseStrategy](formatstyle/parsestrategy.md) — The parse strategy that this format style uses.
- [ParseStrategy](parsestrategy.md) — A parse strategy for creating decimal values from formatted strings.

### Locating decimals with regular expressions

- [consuming(_:startingAt:in:)](<formatstyle/consuming(__startingat_in_).md>) — Process the input string within the specified bounds, beginning at the given index, and return the end position (upper bound) of the match and the produced output.

### Supporting types

- [Currency](formatstyle/currency.md) — A format style that converts between decimal currency values and their textual representations.
- [Percent](formatstyle/percent.md) — A format style that converts between decimal percentage values and their textual representations.

### Default Implementations

- [CustomConsumingRegexComponent Implementations](formatstyle/customconsumingregexcomponent-implementations.md)
- [ParseableFormatStyle Implementations](formatstyle/parseableformatstyle-implementations.md)

## See Also

### Data formatting in Swift

- [Language Introspector](../language-introspector.md) — Converts data into human-readable text using formatters and locales.
- [FormatStyle](../formatstyle.md) — A type that converts a given data type into a representation in another type, such as a string.
- [IntegerFormatStyle](../integerformatstyle.md) — A structure that converts between integer values and their textual representations.
- [FloatingPointFormatStyle](../floatingpointformatstyle.md) — A structure that converts between floating-point values and their textual representations.
- [ListFormatStyle](../listformatstyle.md) — A type that formats lists of items with a separator and conjunction appropriate for a given locale.
- [StringStyle](../stringstyle.md)
- [FormatStyle](../url/formatstyle.md) — A structure that converts between URL instances and their textual representations.
- [FormatStyleCapitalizationContext](../formatstylecapitalizationcontext.md) — The capitalization formatting context used when formatting dates and times.
- [Format Style Configurations](../format-style-configurations.md) — Behaviors for traits like numeric precision, rounding, and scale, used for formatting and parsing numeric values.
