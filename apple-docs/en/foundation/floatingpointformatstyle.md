---
title: FloatingPointFormatStyle
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/floatingpointformatstyle
source_url: 'https://developer.apple.com/documentation/foundation/floatingpointformatstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/floatingpointformatstyle.json'
content_hash: 'sha256:ddbda8797ca46138'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# FloatingPointFormatStyle

<sub>Structure</sub>

A structure that converts between floating-point values and their textual representations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FloatingPointFormatStyle<Value> where Value : BinaryFloatingPoint
```

## Overview

Instances of [FloatingPointFormatStyle](floatingpointformatstyle.md) create localized, human-readable text from [BinaryFloatingPoint](../swift/binaryfloatingpoint.md) numbers and parse string representations of numbers into instances of [BinaryFloatingPoint](../swift/binaryfloatingpoint.md) types. All of the Swift standard library’s floating-point types, such as [Double](../swift/double.md), [Float](../swift/float.md), and [Float80](../swift/float80.md), conform to [BinaryFloatingPoint](../swift/binaryfloatingpoint.md), and therefore work with this format style.

[FloatingPointFormatStyle](floatingpointformatstyle.md) includes two nested types, [Percent](floatingpointformatstyle/percent.md) and [Currency](floatingpointformatstyle/currency.md), for working with percentages and currencies, respectively. Each format style includes a configuration that determines how it represents numeric values, for things like grouping, displaying signs, and variant presentations like scientific notation. [FloatingPointFormatStyle](floatingpointformatstyle.md) and [Percent](floatingpointformatstyle/percent.md) include a [NumberFormatStyleConfiguration](numberformatstyleconfiguration.md), and [Currency](floatingpointformatstyle/currency.md) includes a [CurrencyFormatStyleConfiguration](currencyformatstyleconfiguration.md). You can customize numeric formatting for a style by adjusting its backing configuration. The system automatically caches unique configurations of a format style to enhance performance.

> [!note] Note
> Foundation provides another format style type, [IntegerFormatStyle](integerformatstyle.md), for working with numbers that conform to [BinaryInteger](../swift/binaryinteger.md). For Foundation’s [Decimal](decimal.md) type, use [FormatStyle](decimal/formatstyle.md).

### Formatting floating-point values

Use the [formatted()](<../swift/binaryfloatingpoint/formatted().md>) method to create a string representation of a floating-point value using the default [FloatingPointFormatStyle](floatingpointformatstyle.md) configuration.

```swift
let formattedDefault = 12345.67.formatted()
// formattedDefault is "12,345.67" in the en_US locale.
// Other locales may use different separator and grouping behavior.
```

You can specify a format style by providing an argument to the [formatted(_:)](<../swift/binaryfloatingpoint/formatted(__)-4ksqj.md>) method. The following example shows the number `0.1` represented in each of the available styles, in the `en_US` locale:

```swift
let number = 0.1

let formattedNumber = number.formatted(.number)
// formattedNumber is "0.1".

let formattedPercent = number.formatted(.percent)
// formattedPercent is "10%".

let formattedCurrency = number.formatted(.currency(code: "USD"))
// formattedCurrency is "$0.10".
```

Each style provides methods for updating its numeric configuration, including the number of significant digits, grouping length, and more. You can specify a numeric configuration by calling as many of these methods as you need in any order you choose. The following example shows the same number with default and custom configurations:

```swift
let exampleNumber = 123456.78

let defaultFormatting = exampleNumber.formatted(.number)
// defaultFormatting is "123 456,78" for the "fr_FR" locale.
// defaultFormatting is "123,456.78" for the "en_US" locale.

let customFormatting = exampleNumber.formatted(
    .number
        .grouping(.never)
        .sign(strategy: .always()))
// customFormatting is "+123456.78"
```

### Creating a floating-point format style instance

The previous examples use static factory methods like [number](formatstyle/number-8c8rj.md) to create format styles within the call to the [formatted(_:)](<../swift/binaryfloatingpoint/formatted(__)-4ksqj.md>) method. You can also create a [FloatingPointFormatStyle](floatingpointformatstyle.md) instance and use it to repeatedly format different values, with the [format(_:)](<floatingpointformatstyle/format(__).md>) method:

```swift
let percentFormatStyle = FloatingPointFormatStyle<Double>.Percent()

percentFormatStyle.format(0.5) // "50%"
percentFormatStyle.format(0.855) // "85.5%"
percentFormatStyle.format(1.0) // "100%"

```

### Parsing floating-point values

You can use [FloatingPointFormatStyle](floatingpointformatstyle.md) to parse strings into floating-point values. You can define the format style within the type’s initializer or pass in a format style created outside the function, as shown here:

```swift
let price = try? Double("$3,500.63",
                         format: .currency(code: "USD")) // 3500.63

let priceFormatStyle = FloatingPointFormatStyle<Double>.Currency(code: "USD")
let salePrice = try? Double("$731.67",
                             format: priceFormatStyle) // 731.67
```

### Matching regular expressions

Along with parsing numeric values in strings, you can use theSwift regular expression domain-specific language to match and capture numeric substrings. The following example defines a percentage format style to match a percentage value using `en_US` numeric conventions. The rest of the regular expression ignores any characters prior to a `": "` sequence that precedes the percentage substring.

```swift
import RegexBuilder
let source = "Percentage complete: 55.1%"
let matcher = Regex {
    OneOrMore(.any)
    ": "
    Capture {
        One(.localizedDoublePercentage(locale: Locale(identifier: "en_US")))
    }
}
let match = source.firstMatch(of: matcher)
let localizedPercentage = match?.1
print("\(localizedPercentage!)") // 0.551
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomConsumingRegexComponent](../swift/customconsumingregexcomponent.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [FormatStyle](formatstyle.md), [Hashable](../swift/hashable.md), [ParseableFormatStyle](parseableformatstyle.md), [RegexComponent](../swift/regexcomponent.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a floating-point format style

- [init(locale:)](<floatingpointformatstyle/init(locale_).md>) — Creates a floating-point format style that uses the given locale.

### Formatting floating-point values

- [format(_:)](<floatingpointformatstyle/format(__).md>) — Formats a floating-point value, using this style.

### Customizing style behavior

- [decimalSeparator(strategy:)](<floatingpointformatstyle/decimalseparator(strategy_).md>) — Modifies the format style to use the specified decimal separator display strategy.
- [grouping(_:)](<floatingpointformatstyle/grouping(__).md>) — Modifies the format style to use the specified grouping.
- [locale(_:)](<floatingpointformatstyle/locale(__).md>) — Modifies the format style to use the specified locale.
- [notation(_:)](<floatingpointformatstyle/notation(__).md>) — Modifies the format style to use the specified notation.
- [precision(_:)](<floatingpointformatstyle/precision(__).md>) — Modifies the format style to use the specified precision.
- [rounded(rule:increment:)](<floatingpointformatstyle/rounded(rule_increment_).md>) — Modifies the format style to use the specified rounding rule and increment.
- [scale(_:)](<floatingpointformatstyle/scale(__).md>) — Modifies the format style to use the specified scale.
- [sign(strategy:)](<floatingpointformatstyle/sign(strategy_).md>) — Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [Configuration](floatingpointformatstyle/configuration.md) — The type the format style uses for configuration settings.
- [NumberFormatStyleConfiguration](numberformatstyleconfiguration.md) — Configuration settings for formatting numbers of different types.

### Accessing style locale

- [locale](floatingpointformatstyle/locale.md) — The locale of the format style.

### Applying currency styles

- [Currency](floatingpointformatstyle/currency.md) — A format style that converts between floating-point currency values and their textual representations.

### Applying measurement styles

- [FormatStyle](measurement/formatstyle.md) — A type that provides localized representations of measurements.

### Applying list styles

- [ListFormatStyle](listformatstyle.md) — A type that formats lists of items with a separator and conjunction appropriate for a given locale.

### Creating attributed strings

- [attributed](floatingpointformatstyle/attributed-swift.property.md) — An attributed format style based on the floating-point format style.
- [Attributed](floatingpointformatstyle/attributed-swift.struct.md) — A format style that converts integers into attributed strings.

### Parsing floating-point numbers

- [parseStrategy](floatingpointformatstyle/parsestrategy.md) — The parse strategy that this format style uses.
- [FloatingPointParseStrategy](floatingpointparsestrategy.md) — A parse strategy for creating floating-point values from formatted strings.

### Locating floating-point numbers with regular expressions

- [consuming(_:startingAt:in:)](<floatingpointformatstyle/consuming(__startingat_in_).md>) — Process the input string within the specified bounds, beginning at the given index, and return the end position (upper bound) of the match and the produced output.

### Supporting types

- [Currency](floatingpointformatstyle/currency.md) — A format style that converts between floating-point currency values and their textual representations.
- [Percent](floatingpointformatstyle/percent.md) — A format style that converts between floating-point percentage values and their textual representations.

### Default Implementations

- [CustomConsumingRegexComponent Implementations](floatingpointformatstyle/customconsumingregexcomponent-implementations.md)
- [FormatStyle Implementations](floatingpointformatstyle/formatstyle-implementations.md)
- [ParseableFormatStyle Implementations](floatingpointformatstyle/parseableformatstyle-implementations.md)

## See Also

### Data formatting in Swift

- [Language Introspector](language-introspector.md) — Converts data into human-readable text using formatters and locales.
- [FormatStyle](formatstyle.md) — A type that converts a given data type into a representation in another type, such as a string.
- [IntegerFormatStyle](integerformatstyle.md) — A structure that converts between integer values and their textual representations.
- [FormatStyle](decimal/formatstyle.md) — A structure that converts between decimal values and their textual representations.
- [ListFormatStyle](listformatstyle.md) — A type that formats lists of items with a separator and conjunction appropriate for a given locale.
- [StringStyle](stringstyle.md)
- [FormatStyle](url/formatstyle.md) — A structure that converts between URL instances and their textual representations.
- [FormatStyleCapitalizationContext](formatstylecapitalizationcontext.md) — The capitalization formatting context used when formatting dates and times.
- [Format Style Configurations](format-style-configurations.md) — Behaviors for traits like numeric precision, rounding, and scale, used for formatting and parsing numeric values.
