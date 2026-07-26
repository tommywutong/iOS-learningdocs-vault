---
title: Data Formatting
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/data-formatting
source_url: 'https://developer.apple.com/documentation/foundation/data-formatting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data-formatting.json'
content_hash: 'sha256:4590ba992836842e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Data Formatting

<sub>API Collection</sub>

Convert numbers, dates, measurements, and other values to and from locale-aware string representations.

## Overview

Foundation supports two approaches for data formatting:

- When working in Swift, use `formatted` methods directly on the types you want to format, optionally using [FormatStyle](formatstyle.md) and its subtypes to customize formatter output. This approach supports dates, integers, floating-point numbers, measurements, sequences, and person name components. Foundation caches identically-configured formatter instances internally, allowing you to focus on your app’s formatting needs.
- In Objective-C, create instances of [Formatter](formatter.md) and its subtypes, and use the [- stringForObjectValue:](<formatter/string(for_).md>) method to convert objects to formatted strings.

## Topics

### Essentials

- [Building a Localized Food-Ordering App](building-a-localized-food-ordering-app.md) — Format, style, and localize your app’s text for use in multiple languages with string formatting, attributed strings, and automatic grammar agreement.
- [Displaying Human-Friendly Content](displaying-human-friendly-content.md) — Convert data into readable strings or Swift objects using formatters.

### Data formatting in Swift

- [Language Introspector](language-introspector.md) — Converts data into human-readable text using formatters and locales.
- [FormatStyle](formatstyle.md) — A type that converts a given data type into a representation in another type, such as a string.
- [IntegerFormatStyle](integerformatstyle.md) — A structure that converts between integer values and their textual representations.
- [FloatingPointFormatStyle](floatingpointformatstyle.md) — A structure that converts between floating-point values and their textual representations.
- [FormatStyle](decimal/formatstyle.md) — A structure that converts between decimal values and their textual representations.
- [ListFormatStyle](listformatstyle.md) — A type that formats lists of items with a separator and conjunction appropriate for a given locale.
- [StringStyle](stringstyle.md)
- [FormatStyle](url/formatstyle.md) — A structure that converts between URL instances and their textual representations.
- [FormatStyleCapitalizationContext](formatstylecapitalizationcontext.md) — The capitalization formatting context used when formatting dates and times.
- [Format Style Configurations](format-style-configurations.md) — Behaviors for traits like numeric precision, rounding, and scale, used for formatting and parsing numeric values.

### Data parsing in Swift

- [ParseableFormatStyle](parseableformatstyle.md) — A type that can convert a given input data type into a representation in an output type.
- [ParseStrategy](parsestrategy.md) — A type that parses an input representation, such as a formatted string, into a provided data type.
- [IntegerParseStrategy](integerparsestrategy.md) — A parse strategy for creating integer values from formatted strings.
- [FloatingPointParseStrategy](floatingpointparsestrategy.md) — A parse strategy for creating floating-point values from formatted strings.
- [ParseStrategy](decimal/parsestrategy.md) — A parse strategy for creating decimal values from formatted strings.

### Numbers and currency

- [NumberFormatter](numberformatter.md) — A formatter that converts between numeric values and their textual representations.

### Names

- [PersonNameComponentsFormatter](personnamecomponentsformatter.md) — A formatter that provides localized representations of the components of a person’s name.
- [PersonNameComponents](personnamecomponents.md) — The separate parts of a person’s name, allowing locale-aware formatting.

### Dates and times

- [DateFormatter](dateformatter.md) — A formatter that converts between dates and their textual representations.
- [DateComponentsFormatter](datecomponentsformatter.md) — A formatter that creates string representations of quantities of time.
- [RelativeDateTimeFormatter](relativedatetimeformatter.md) — A formatter that creates locale-aware string representations of a relative date or time.
- [DateIntervalFormatter](dateintervalformatter.md) — A formatter that creates string representations of time intervals.
- [ISO8601DateFormatter](iso8601dateformatter.md) — A formatter that converts between dates and their ISO 8601 string representations.

### Data sizes

- [ByteCountFormatter](bytecountformatter.md) — A formatter that converts a byte count value into a localized description that is formatted with the appropriate byte modifier (KB, MB, GB and so on).

### Measurements

- [MeasurementFormatter](measurementformatter.md) — A formatter that provides localized representations of units and measurements.

### Lists

- [ListFormatter](listformatter.md) — An object that provides locale-correct formatting of a list of items using the appropriate separator and conjunction.

### Internationalization

- [Locale](locale.md) — Information about linguistic, cultural, and technological conventions for use in formatting data for presentation.

### Custom formatters

- [Formatter](formatter.md) — An abstract class that declares an interface for objects that create, interpret, and validate the textual representation of values.

### Automatic grammar agreement

- [InflectionRule](inflectionrule.md) — A rule that affects how an attributed string performs automatic grammatical agreement.
- [Morphology](morphology.md) — A description of the grammatical properties of a string.
- [TermOfAddress](termofaddress.md) — The type for representing grammatical gender in localized text.
- [InflectionConcept](inflectionconcept.md) — An inflection method to use when localizing text.
- [Pronoun](morphology/pronoun.md) — A custom pronoun for referring to a third person.

### Deprecated

- [LengthFormatter](lengthformatter.md) — A formatter that provides localized descriptions of linear distances, such as length and height measurements.
- [MassFormatter](massformatter.md) — A formatter that provides localized descriptions of mass and weight values.
- [EnergyFormatter](energyformatter.md) — A formatter that provides localized descriptions of energy values.

## See Also

### Fundamentals

- [Numbers, Data, and Basic Values](numbers-data-and-basic-values.md) — Work with primitive values and other fundamental types used throughout Cocoa.
- [Strings and Text](strings-and-text.md) — Create and process strings of Unicode characters, use regular expressions to find patterns, and perform natural language analysis of text.
- [Collections](collections.md) — Use arrays, dictionaries, sets, and specialized collections to store and iterate groups of objects or values.
- [Dates and Times](dates-and-times.md) — Compare dates and times, and perform calendar and time zone calculations.
- [Units and Measurement](units-and-measurement.md) — Label numeric quantities with physical dimensions to allow locale-aware formatting and conversion between related units.
- [Filters and Sorting](filters-and-sorting.md) — Use predicates, expressions, and sort descriptors to examine elements in collections and other services.
