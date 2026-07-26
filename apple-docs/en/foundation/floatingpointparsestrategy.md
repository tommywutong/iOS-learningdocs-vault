---
title: FloatingPointParseStrategy
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/floatingpointparsestrategy
source_url: 'https://developer.apple.com/documentation/foundation/floatingpointparsestrategy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/floatingpointparsestrategy.json'
content_hash: 'sha256:5ae3ceade38a2a0c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# FloatingPointParseStrategy

<sub>Structure</sub>

A parse strategy for creating floating-point values from formatted strings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FloatingPointParseStrategy<Format> where Format : FormatStyle, Format.FormatInput : BinaryFloatingPoint
```

## Overview

Create an explicit [FloatingPointParseStrategy](floatingpointparsestrategy.md) to parse multiple strings according to the same parse strategy. In the following example, `usCurrencyStrategy` is a [FloatingPointParseStrategy](floatingpointparsestrategy.md) that uses US dollars and the `en_US` locale’s conventions for number formatting. The example then uses this strategy to parse an array of strings, some of which represent valid US currency values.

```swift
let usCurrencyStrategy: FloatingPointParseStrategy =
FloatingPointFormatStyle<Double>.Currency(code: "USD",
                                          locale: Locale(identifier: "en_US"))
    .parseStrategy
let currencyValues = ["$100.11", "$1,000.22", "$10,000.33", "€100.44"]
let parsedValues = currencyValues.map { try? usCurrencyStrategy.parse($0) } // [Optional(100.11), Optional(1000.22), Optional(10000.33), nil]
```

You don’t need to instantiate a parse strategy variable to parse a single string. Instead, use the [BinaryFloatingPoint](../swift/binaryfloatingpoint.md) initializers that take a source [String](../swift/string.md) and a `format` parameter to parse the string according to the provided [FormatStyle](formatstyle.md). The following example parses a string that represents a currency value in US dollars.

```swift
let formattedUSDollars = "$1,234.56"
let parsedUSDollars = try? Double(formattedUSDollars, format: .currency(code: "USD")
    .locale(Locale(identifier: "en_US"))) // 1234.56
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [ParseStrategy](parsestrategy.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a floating-point parse strategy

- [init(format:lenient:)](<floatingpointparsestrategy/init(format_lenient_)-5nxey.md>) — Creates a parse strategy instance using the specified floating-point format style.
- [init(format:lenient:)](<floatingpointparsestrategy/init(format_lenient_)-9g6wm.md>) — Creates a parse strategy instance using the specified floating-point currency format style.
- [init(format:lenient:)](<floatingpointparsestrategy/init(format_lenient_)-1nldg.md>) — Creates a parse strategy instance using the specified floating-point percentage format style.

### Parsing strings

- [parse(_:)](<floatingpointparsestrategy/parse(__).md>) — Parses a floating-point string in accordance with this strategy and returns the parsed value.

### Accessing strategy properties

- [formatStyle](floatingpointparsestrategy/formatstyle.md) — The format style this strategy uses when parsing strings.
- [lenient](floatingpointparsestrategy/lenient.md) — A Boolean value that indicates whether parsing allows any discrepencies in the expected format.

### Default Implementations

- [ParseStrategy Implementations](floatingpointparsestrategy/parsestrategy-implementations.md)

## See Also

### Data parsing in Swift

- [ParseableFormatStyle](parseableformatstyle.md) — A type that can convert a given input data type into a representation in an output type.
- [ParseStrategy](parsestrategy.md) — A type that parses an input representation, such as a formatted string, into a provided data type.
- [IntegerParseStrategy](integerparsestrategy.md) — A parse strategy for creating integer values from formatted strings.
- [ParseStrategy](decimal/parsestrategy.md) — A parse strategy for creating decimal values from formatted strings.
