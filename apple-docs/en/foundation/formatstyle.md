---
title: FormatStyle
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/formatstyle
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle.json'
content_hash: 'sha256:cd745558caec7552'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# FormatStyle

<sub>Protocol</sub>

A type that converts a given data type into a representation in another type, such as a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol FormatStyle<FormatInput, FormatOutput> : Decodable, Encodable, Hashable
```

## Overview

Types conforming to the [FormatStyle](formatstyle.md) protocol take their input type and produce formatted instances of their output type. The formatting process accounts for locale-specific conventions, like grouping and separators for numbers, and presentation of units for measurements. The format styles Foundation provides produce their output as [String](../swift/string.md) or [AttributedString](attributedstring.md) instances. You can also create custom styles that format their output as any type, like XML or JSON [Data](data.md) or an image.

There are two basic approaches to using a [FormatStyle](formatstyle.md):

- Create an instance of a type that conforms to [FormatStyle](formatstyle.md) and apply it to one or more instances of the input type, by calling the style’s [format(_:)](<formatstyle/format(__).md>) method. Use this when you want to customize a style once and apply it repeatedly to many instances.
- Pass an instance of a type that conforms to [FormatStyle](formatstyle.md) to the data type’s `formatted(_:)` method, which takes the style as a parameter. Use this for one-off formatting scenarios, or when you want to apply different format styles to the same data value. For the simplest cases, most types that support formatting also have a no-argument `formatted()` method that applies a locale-appropriate default format style.

Foundation provides format styles for integers ([IntegerFormatStyle](integerformatstyle.md)), floating-point numbers ([FloatingPointFormatStyle](floatingpointformatstyle.md)), decimals ([FormatStyle](decimal/formatstyle.md)), measurements ([FormatStyle](measurement/formatstyle.md)), arrays ([ListFormatStyle](listformatstyle.md)), and more. The “Conforming types” section below shows all the format styles available from Foundation and any system frameworks that implement the [FormatStyle](formatstyle.md) protocol. The numeric format styles also provide supporting format styles to format currency and percent values, like [Currency](integerformatstyle/currency.md) and [Percent](decimal/formatstyle/percent.md).

### Modifying a format style

Format styles include modifier methods that return a new format style with an adjusted behavior. The following example creates an [IntegerFormatStyle](integerformatstyle.md), then applies modifiers to round values down to the nearest 1,000 and applies formatting appropriate to the `fr_FR` locale:

```swift
let style = IntegerFormatStyle<Int>()
    .rounded(rule: .down, increment: 1000)
    .locale(Locale(identifier: "fr_FR"))
let rounded = 123456789.formatted(style) // "123 456 000"
```

Foundation caches identical instances of a customized format style, so you don’t need to pass format style instances around unrelated parts of your app’s source code.

### Accessing static instances

Types that conform to [FormatStyle](formatstyle.md) typically extend the base protocol with type properties or type methods to provide convenience instances. These are available for use in a data type’s `formatted(_:)` method when the format style’s input type matches the data type. For example, the various numeric format styles define `number` properties with generic constraints to match the different numeric types ([Double](../swift/double.md), [Int](../swift/int.md), [Float16](../swift/float16.md), and so on).

To see how this works, consider this example of a default formatter for an [Int](../swift/int.md) value. Because `123456789` is a [BinaryInteger](../swift/binaryinteger.md), its [formatted(_:)](<../swift/binaryinteger/formatted(__)-4qd73.md>) method accepts an [IntegerFormatStyle](integerformatstyle.md) parameter. The following example shows the style’s default behavior in the `en_US` locale.

```swift
let formatted = 123456789.formatted(IntegerFormatStyle()) // "123,456,789"
```

[IntegerFormatStyle](integerformatstyle.md) extends [FormatStyle](formatstyle.md) with multiple type properties called `number`, each of which is an [IntegerFormatStyle](integerformatstyle.md) instance; these properties differ by which [BinaryInteger](../swift/binaryinteger.md)-conforming type they take as input. Since one of these statically-defined properties ([number](formatstyle/number-7fxvo.md)) takes [Int](../swift/int.md) as its input, you can use this type property instead of instantiating a new format style instance. Using dot notation to access this property on the inferred [FormatStyle](formatstyle.md) makes the call point much easier to read, as seen here:

```swift
let formatted = 123456789.formatted( .number) // "123,456,789"
```

Furthermore, since you can customize these statically-accessed format style instances, you can rewrite the example from the previous section without instantiating a new [IntegerFormatStyle](integerformatstyle.md), like this:

```swift
let rounded = 123456789.formatted( .number
    .rounded(rule: .down, increment: 1000)
    .locale(Locale(identifier: "fr_FR"))) // "123 456 000"
```

### Parsing with a format style

To perform the opposite conversion — from formatted output type to input data type — some format styles provide a corresponding [ParseStrategy](parsestrategy.md) type. These format styles typically expose an instance of this type as a variable, called `parseStrategy`.

You can use a [ParseStrategy](parsestrategy.md) one of two ways:

- Initialize the data type by calling an initializer of that type that takes a formatted instance and a parse strategy as parameters. For example, you can create a [Decimal](decimal.md) from a formatted string with the initializer [init(_:format:lenient:)](<decimal/init(__format_lenient_)-6fk71.md>).
- Create a parse strategy and call its [parse(_:)](<parsestrategy/parse(__).md>) method on one or more formatted instances.

## Relationships

- **Inherits From**: [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

- **Inherited By**: [DiscreteFormatStyle](discreteformatstyle.md), [ParseableFormatStyle](parseableformatstyle.md)

- **Conforming Types**: [ByteCountFormatStyle](bytecountformatstyle.md), [Attributed](bytecountformatstyle/attributed-swift.struct.md), [AnchoredRelativeFormatStyle](date/anchoredrelativeformatstyle.md), [AttributedStyle](date/attributedstyle.md), [ComponentsFormatStyle](date/componentsformatstyle.md), [FormatStyle](date/formatstyle.md), [Attributed](date/formatstyle/attributed-swift.struct.md), [HTTPFormatStyle](date/httpformatstyle.md), [ISO8601FormatStyle](date/iso8601formatstyle.md), [IntervalFormatStyle](date/intervalformatstyle.md), [RelativeFormatStyle](date/relativeformatstyle.md), [VerbatimFormatStyle](date/verbatimformatstyle.md), [Attributed](date/verbatimformatstyle/attributed-swift.struct.md), [HTTPFormatStyle](datecomponents/httpformatstyle.md), [ISO8601FormatStyle](datecomponents/iso8601formatstyle.md), [FormatStyle](decimal/formatstyle.md), [Attributed](decimal/formatstyle/attributed-swift.struct.md), [Currency](decimal/formatstyle/currency.md), [Percent](decimal/formatstyle/percent.md), [FloatingPointFormatStyle](floatingpointformatstyle.md), [Attributed](floatingpointformatstyle/attributed-swift.struct.md), [Currency](floatingpointformatstyle/currency.md), [Percent](floatingpointformatstyle/percent.md), [IntegerFormatStyle](integerformatstyle.md), [Attributed](integerformatstyle/attributed-swift.struct.md), [Currency](integerformatstyle/currency.md), [Percent](integerformatstyle/percent.md), [ListFormatStyle](listformatstyle.md), [AttributedStyle](measurement/attributedstyle.md), [ByteCount](measurement/attributedstyle/bytecount.md), [FormatStyle](measurement/formatstyle.md), [ByteCount](measurement/formatstyle/bytecount.md), [AttributedStyle](personnamecomponents/attributedstyle.md), [FormatStyle](personnamecomponents/formatstyle.md), [StringStyle](stringstyle.md), [FormatStyle](url/formatstyle.md)

## Topics

### Performing formatting

- [format(_:)](<formatstyle/format(__).md>) — Formats a value, using this style.

### Setting style Locale

- [locale(_:)](<formatstyle/locale(__).md>) — Modifies the format style to use the specified locale.

### Applying numeric styles for integers

- [number](formatstyle/number-7fxvo.md) — A style for formatting the Swift default integer type.
- [number](formatstyle/number-4ttgp.md) — A style for formatting the Swift unsigned integer type.
- [number](formatstyle/number-5hzgj.md) — A style for formatting 8-bit signed integers.
- [number](formatstyle/number-1o8fx.md) — A style for formatting 16-bit signed integers.
- [number](formatstyle/number-4cj49.md) — A style for formatting 32-bit signed integers.
- [number](formatstyle/number-3925i.md) — A style for formatting 64-bit signed integers.
- [number](formatstyle/number-8fms6.md) — A style for formatting 8-bit unsigned integers.
- [number](formatstyle/number-fak0.md) — A style for formatting 16-bit unsigned integers.
- [number](formatstyle/number-13mra.md) — A style for formatting 32-bit unsigned integers.
- [number](formatstyle/number-iyry.md) — A style for formatting 64-bit unsigned integers.
- [IntegerFormatStyle](integerformatstyle.md) — A structure that converts between integer values and their textual representations.

### Applying numeric styles for floating-point values

- [number](formatstyle/number-432x3.md) — A style for formatting the Swift standard single-precision floating-point type.
- [number](formatstyle/number-8c8rj.md) — A style for formatting the Swift standard double-precision floating-point type.
- [number](formatstyle/number-3qe2o.md) — A style for formatting 16-bit floating-point values.
- [FloatingPointFormatStyle](floatingpointformatstyle.md) — A structure that converts between floating-point values and their textual representations.

### Applying numeric styles for decimals

- [number](formatstyle/number-3luf2.md) — A style for formatting decimal values.
- [FormatStyle](decimal/formatstyle.md) — A structure that converts between decimal values and their textual representations.

### Applying percentage styles for integers

- [percent](formatstyle/percent-cl9k.md) — A style for formatting signed integer types in Swift as a percent representation.
- [percent](formatstyle/percent-9pj79.md) — A style for formatting signed integer types in Swift as a percent representation.
- [percent](formatstyle/percent-7r4rl.md) — A style for formatting 8-bit signed integers as a percent representation.
- [percent](formatstyle/percent-3qjzh.md) — A style for formatting 16-bit signed integers as a percent representation.
- [percent](formatstyle/percent-1f0q.md) — A style for formatting 32-bit signed integers as a percent representation.
- [percent](formatstyle/percent-934se.md) — A style for formatting 64-bit signed integers as a percent representation.
- [percent](formatstyle/percent-8izzv.md) — A style for formatting 8-bit unsigned integers as a percent representation.
- [percent](formatstyle/percent-4kdme.md) — A style for formatting 16-bit unsigned integers as a percent representation.
- [percent](formatstyle/percent-2f11j.md) — A style for formatting 32-bit unsigned integers as a percent representation.
- [percent](formatstyle/percent-8bxla.md) — A style for formatting 64-bit unsigned integers as a percent representation.
- [Percent](integerformatstyle/percent.md) — A format style that converts between integer percentage values and their textual representations.

### Applying percentage styles for floating-point values

- [percent](formatstyle/percent-2gva1.md) — A style for formatting the Swift standard single-precision floating-point type as a percent representation.
- [percent](formatstyle/percent-6cwuv.md) — A style for formatting the Swift standard single-precision floating-point type as a percent representation.
- [percent](formatstyle/percent-grss.md) — A style for formatting 16-bit floating-point values as a percent representation.
- [Percent](floatingpointformatstyle/percent.md) — A format style that converts between floating-point percentage values and their textual representations.

### Applying percentage styles for decimals

- [percent](formatstyle/percent-4knsm.md) — A style for formatting decimal values as a percent represntation.
- [Percent](decimal/formatstyle/percent.md) — A format style that converts between decimal percentage values and their textual representations.

### Applying date and time styles

- [dateTime](formatstyle/datetime.md) — A style for formatting a date and time.
- [FormatStyle](date/formatstyle.md) — A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.
- [ISO8601FormatStyle](date/iso8601formatstyle.md) — A type that converts between dates and their ISO-8601 string representations.
- [verbatim(_:locale:timeZone:calendar:)](<formatstyle/verbatim(__locale_timezone_calendar_).md>) — Returns a style for formatting a date with an explicitly-specified style.
- [VerbatimFormatStyle](date/verbatimformatstyle.md) — A style that formats a date with an explicitly-specified style.
- [interval](formatstyle/interval.md) — A style for formatting a date interval.
- [IntervalFormatStyle](date/intervalformatstyle.md) — A format style that creates string representations of date intervals.
- [relative(presentation:unitsStyle:)](<formatstyle/relative(presentation_unitsstyle_).md>) — Returns a style for formatting a date as relative to the current date.
- [RelativeFormatStyle](date/relativeformatstyle.md) — A format style that forms locale-aware string representations of a relative date or time.
- [components(style:fields:)](<formatstyle/components(style_fields_).md>) — Returns a style for formatting a date interval in terms of specific date components.
- [ComponentsFormatStyle](date/componentsformatstyle.md) — A style for formatting a date interval in terms of specific date components.

### Applying duration styles

- [timeDuration](formatstyle/timeduration.md) — A style for formatting a duration expressed as a range of dates.
- [ComponentsFormatStyle](date/componentsformatstyle.md) — A style for formatting a date interval in terms of specific date components.
- [time(pattern:)](<formatstyle/time(pattern_).md>) — Returns a style for formatting a duration using a provided pattern.
- [units(allowed:width:maximumUnitCount:zeroValueUnits:valueLength:fractionalPart:)](<formatstyle/units(allowed_width_maximumunitcount_zerovalueunits_valuelength_fractionalpart_).md>) — Returns a style for formatting a duration that uses the specified units.
- [units(allowed:width:maximumUnitCount:zeroValueUnits:valueLengthLimits:fractionalPart:)](<formatstyle/units(allowed_width_maximumunitcount_zerovalueunits_valuelengthlimits_fractionalpart_).md>) — Returns a style for formatting a duration range that uses the specified units, with padding/truncating behavior defined as a range.

### Applying currency styles

- [currency(code:)](<formatstyle/currency(code_)-is0v.md>) — Returns a format style to use integer currency notation.
- [currency(code:)](<formatstyle/currency(code_)-1yg68.md>) — Returns a format style to use floating-point currency notation.
- [currency(code:)](<formatstyle/currency(code_)-6fhr2.md>) — Returns a format style to use decimal currency notation.

### Applying measurement styles

- [measurement(width:usage:numberFormatStyle:)](<formatstyle/measurement(width_usage_numberformatstyle_).md>) — Returns a format style to format measurement units.
- [measurement(width:usage:hidesScaleName:numberFormatStyle:)](<formatstyle/measurement(width_usage_hidesscalename_numberformatstyle_).md>) — Returns a format style to format temperature units.

### Applying person name styles

- [name(style:)](<formatstyle/name(style_).md>) — Returns a format style to use the given name style for formatting a name from its components.

### Applying list styles

- [list(memberStyle:type:width:)](<formatstyle/list(memberstyle_type_width_).md>) — Returns a format style to format a list of items.
- [list(type:width:)](<formatstyle/list(type_width_).md>) — Returns a format style to format a list of strings.

### Applying byte-count styles

- [byteCount(style:allowedUnits:spellsOutZero:includesActualByteCount:)](<formatstyle/bytecount(style_allowedunits_spellsoutzero_includesactualbytecount_)-59ep0.md>) — Returns a format style to format a data storage value.
- [ByteCountFormatStyle](bytecountformatstyle.md) — A format style that provides string representations of byte counts.
- [byteCount(style:allowedUnits:spellsOutZero:includesActualByteCount:)](<formatstyle/bytecount(style_allowedunits_spellsoutzero_includesactualbytecount_)-ev0u.md>) — Returns a format style to format a data storage value represented with Foundation’s measurement type.
- [ByteCount](measurement/formatstyle/bytecount.md) — A format style that provides string representations of byte counts, expressed as measurements of information storage.

### Applying URL styles

- [url](formatstyle/url.md) — A style for formatting a URL.
- [FormatStyle](url/formatstyle.md) — A structure that converts between URL instances and their textual representations.

### Declaring input and output types

- [FormatInput](formatstyle/formatinput.md) — The type this format style accepts as input.
- [FormatOutput](formatstyle/formatoutput.md) — The type this format style produces as output.

### Type Properties

- [http](formatstyle/http-5jh9g.md)
- [http](formatstyle/http-9pwm2.md)
- [iso8601](formatstyle/iso8601-4smgu.md)
- [iso8601](formatstyle/iso8601-773rn.md)

### Type Methods

- [offset(to:allowedFields:maxFieldCount:sign:)](<formatstyle/offset(to_allowedfields_maxfieldcount_sign_).md>)
- [reference(to:allowedFields:maxFieldCount:thresholdField:)](<formatstyle/reference(to_allowedfields_maxfieldcount_thresholdfield_).md>)
- [stopwatch(startingAt:showsHours:maxFieldCount:maxPrecision:)](<formatstyle/stopwatch(startingat_showshours_maxfieldcount_maxprecision_).md>)
- [timer(countingDownIn:showsHours:maxFieldCount:maxPrecision:)](<formatstyle/timer(countingdownin_showshours_maxfieldcount_maxprecision_).md>)
- [timer(countingUpIn:showsHours:maxFieldCount:maxPrecision:)](<formatstyle/timer(countingupin_showshours_maxfieldcount_maxprecision_).md>)

## See Also

### Data formatting in Swift

- [Language Introspector](language-introspector.md) — Converts data into human-readable text using formatters and locales.
- [IntegerFormatStyle](integerformatstyle.md) — A structure that converts between integer values and their textual representations.
- [FloatingPointFormatStyle](floatingpointformatstyle.md) — A structure that converts between floating-point values and their textual representations.
- [FormatStyle](decimal/formatstyle.md) — A structure that converts between decimal values and their textual representations.
- [ListFormatStyle](listformatstyle.md) — A type that formats lists of items with a separator and conjunction appropriate for a given locale.
- [StringStyle](stringstyle.md)
- [FormatStyle](url/formatstyle.md) — A structure that converts between URL instances and their textual representations.
- [FormatStyleCapitalizationContext](formatstylecapitalizationcontext.md) — The capitalization formatting context used when formatting dates and times.
- [Format Style Configurations](format-style-configurations.md) — Behaviors for traits like numeric precision, rounding, and scale, used for formatting and parsing numeric values.
