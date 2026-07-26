---
title: IntegerFormatStyle
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/integerformatstyle
source_url: 'https://developer.apple.com/documentation/foundation/integerformatstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/integerformatstyle.json'
content_hash: 'sha256:a3477eeeb6aaab93'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# IntegerFormatStyle

<sub>Structure</sub>

A structure that converts between integer values and their textual representations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct IntegerFormatStyle<Value> where Value : BinaryInteger
```

## Overview

Instances of [IntegerFormatStyle](integerformatstyle.md) create localized, human-readable text from [BinaryInteger](../swift/binaryinteger.md) numbers and parse string representations of numbers into instances of [BinaryInteger](../swift/binaryinteger.md) types. All of the Swift standard library’s integer types, such as [Int](../swift/int.md) and [UInt32](../swift/uint32.md), conform to [BinaryInteger](../swift/binaryinteger.md), and therefore work with this format style.

[IntegerFormatStyle](integerformatstyle.md) includes two nested types, [Percent](integerformatstyle/percent.md) and [Currency](integerformatstyle/currency.md), for working with percentages and currencies. Each format style includes a configuration that determines how it represents numeric values, for things like grouping, displaying signs, and variant presentations like scientific notation. [IntegerFormatStyle](integerformatstyle.md) and [Percent](integerformatstyle/percent.md) include a [NumberFormatStyleConfiguration](numberformatstyleconfiguration.md), and [Currency](integerformatstyle/currency.md) includes a [CurrencyFormatStyleConfiguration](currencyformatstyleconfiguration.md). You can customize numeric formatting for a style by adjusting its backing configuration. The system automatically caches unique configurations of a format style to enhance performance.

> [!note] Note
> Foundation provides another format style type, [FloatingPointFormatStyle](floatingpointformatstyle.md), for working with numbers that conform to [BinaryFloatingPoint](../swift/binaryfloatingpoint.md). For Foundation’s [Decimal](decimal.md) type, use [FormatStyle](decimal/formatstyle.md).

### Formatting integers

Use the [formatted()](<../swift/binaryinteger/formatted().md>) method to create a string representation of an integer using the default [IntegerFormatStyle](integerformatstyle.md) configuration.

```swift
let formattedDefault = 123456.formatted()
// formattedDefault is "123,456" in en_US locale.
// Other locales may use different separator and grouping behavior.
```

You can specify a format style by providing an argument to the [formatted(_:)](<../swift/binaryinteger/formatted(__)-73k3e.md>) method. The following example shows the number `12345` represented in each of the available styles, in the `en_US` locale:

```swift
let number = 123456

let formattedNumber = number.formatted(.number)
// formattedNumber is "123,456".

let formattedPercent = number.formatted(.percent)
// formattedPercent is "123,456%".

let formattedCurrency = number.formatted(.currency(code: "USD"))
// formattedCurrency is "$123,456.00".
```

Each style provides methods for updating its numeric configuration, including the number of significant digits, grouping length, and more. You can specify a numeric configuration by calling as many of these methods as you need in any order you choose. The following example shows the same number with default and custom configurations:

```swift
let exampleNumber = 123456

let defaultFormatting = exampleNumber.formatted(.number)
// defaultFormatting is "125 000" for the "fr_FR" locale
// defaultFormatting is "125000" for the "jp_JP" locale
// defaultFormatting is "125,000" for the "en_US" locale

let customFormatting = exampleNumber.formatted(
    .number
    .grouping(.never)
    .sign(strategy: .always()))
// customFormatting is "+123456"
```

### Creating an integer format style instance

The previous examples use static factory methods like [number](formatstyle/number-7fxvo.md) to create format styles within the call to the [formatted(_:)](<../swift/binaryinteger/formatted(__)-73k3e.md>) method. You can also create an [IntegerFormatStyle](integerformatstyle.md) instance and use it to repeatedly format different values with the [format(_:)](<integerformatstyle/format(__).md>) method:

```swift
let percentFormatStyle = IntegerFormatStyle<Int>.Percent()

percentFormatStyle.format(50) // "50%"
percentFormatStyle.format(85) // "85%"
percentFormatStyle.format(100) // "100%"
```

### Parsing integers

You can use [IntegerFormatStyle](integerformatstyle.md) to parse strings into integer values. You can define the format style within the type’s initializer or pass in a format style you create prior to calling the method, as shown here:

```swift
let price = try? Int("$123,456",
                     format: .currency(code: "USD")) // 123456

let priceFormatStyle = IntegerFormatStyle<Int>.Currency(code: "USD")
let salePrice = try? Int("$120,000",
                          format: priceFormatStyle) // 120000
```

### Matching regular expressions

Along with parsing numeric values in strings, you can use the Swift regular expression domain-specific language to match and capture numeric substrings. The following example defines a currency format style to match and capture a currency value using US dollars and `en_US` numeric conventions. The rest of the regular expression ignores any characters prior to a `": "` sequence that precedes the currency substring.

```swift
import RegexBuilder

let source = "Payment due: $123,456"
let matcher = Regex {
    OneOrMore(.any)
    ": "
    Capture {
        One(.localizedIntegerCurrency(code: Locale.Currency("USD"),
                                      locale: Locale(identifier: "en_US")))
    }
}
let match = source.firstMatch(of: matcher)
let localizedInteger = match?.1 // 123456
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomConsumingRegexComponent](../swift/customconsumingregexcomponent.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [FormatStyle](formatstyle.md), [Hashable](../swift/hashable.md), [ParseableFormatStyle](parseableformatstyle.md), [RegexComponent](../swift/regexcomponent.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an integer format style

- [init(locale:)](<integerformatstyle/init(locale_).md>) — Creates an integer format style that uses the given locale.

### Formatting integer values

- [format(_:)](<integerformatstyle/format(__).md>) — Formats an integer, using this style.

### Customizing style behavior

- [decimalSeparator(strategy:)](<integerformatstyle/decimalseparator(strategy_).md>) — Modifies the format style to use the specified decimal separator display strategy.
- [grouping(_:)](<integerformatstyle/grouping(__).md>) — Modifies the format style to use the specified grouping.
- [notation(_:)](<integerformatstyle/notation(__).md>) — Modifies the format style to use the specified notation.
- [precision(_:)](<integerformatstyle/precision(__).md>) — Modifies the format style to use the specified precision.
- [rounded(rule:increment:)](<integerformatstyle/rounded(rule_increment_).md>) — Modifies the format style to use the specified rounding rule and increment.
- [scale(_:)](<integerformatstyle/scale(__).md>) — Modifies the format style to use the specified scale.
- [sign(strategy:)](<integerformatstyle/sign(strategy_).md>) — Modifies the format style to use the specified sign display strategy for displaying or omitting sign symbols.
- [Configuration](integerformatstyle/configuration.md) — The type the format style uses for configuration settings.
- [NumberFormatStyleConfiguration](numberformatstyleconfiguration.md) — Configuration settings for formatting numbers of different types.

### Acessing style locale

- [locale](integerformatstyle/locale.md) — The locale of the format style.

### Applying currency styles

- [Currency](integerformatstyle/currency.md) — A format style that converts between integer currency values and their textual representations.

### Applying measurement styles

- [FormatStyle](measurement/formatstyle.md) — A type that provides localized representations of measurements.

### Applying list styles

- [ListFormatStyle](listformatstyle.md) — A type that formats lists of items with a separator and conjunction appropriate for a given locale.

### Creating attributed strings

- [attributed](integerformatstyle/attributed-swift.property.md) — An attributed format style based on the integer format style.
- [Attributed](integerformatstyle/attributed-swift.struct.md) — A format style that converts integers into attributed strings.

### Parsing integers

- [IntegerParseStrategy](integerparsestrategy.md) — A parse strategy for creating integer values from formatted strings.

### Supporting types

- [Currency](integerformatstyle/currency.md) — A format style that converts between integer currency values and their textual representations.
- [Percent](integerformatstyle/percent.md) — A format style that converts between integer percentage values and their textual representations.

### Default Implementations

- [CustomConsumingRegexComponent Implementations](integerformatstyle/customconsumingregexcomponent-implementations.md)
- [FormatStyle Implementations](integerformatstyle/formatstyle-implementations.md)
- [ParseableFormatStyle Implementations](integerformatstyle/parseableformatstyle-implementations.md)

## See Also

### Data formatting in Swift

- [Language Introspector](language-introspector.md) — Converts data into human-readable text using formatters and locales.
- [FormatStyle](formatstyle.md) — A type that converts a given data type into a representation in another type, such as a string.
- [FloatingPointFormatStyle](floatingpointformatstyle.md) — A structure that converts between floating-point values and their textual representations.
- [FormatStyle](decimal/formatstyle.md) — A structure that converts between decimal values and their textual representations.
- [ListFormatStyle](listformatstyle.md) — A type that formats lists of items with a separator and conjunction appropriate for a given locale.
- [StringStyle](stringstyle.md)
- [FormatStyle](url/formatstyle.md) — A structure that converts between URL instances and their textual representations.
- [FormatStyleCapitalizationContext](formatstylecapitalizationcontext.md) — The capitalization formatting context used when formatting dates and times.
- [Format Style Configurations](format-style-configurations.md) — Behaviors for traits like numeric precision, rounding, and scale, used for formatting and parsing numeric values.
