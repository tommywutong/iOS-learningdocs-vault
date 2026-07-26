---
title: IntegerParseStrategy
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/integerparsestrategy
source_url: 'https://developer.apple.com/documentation/foundation/integerparsestrategy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/integerparsestrategy.json'
content_hash: 'sha256:f4f96a021d9bac94'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# IntegerParseStrategy

<sub>Structure</sub>

A parse strategy for creating integer values from formatted strings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct IntegerParseStrategy<Format> where Format : FormatStyle, Format.FormatInput : BinaryInteger
```

## Overview

Create an explicit [IntegerParseStrategy](integerparsestrategy.md) to parse multiple strings according to the same parse strategy. In the following example, `usCurrencyStrategy` is an [IntegerParseStrategy](integerparsestrategy.md) that uses US dollars and the `en_US` locale’s conventions for number formatting. The example then uses this strategy to parse an array of strings, some of which represent valid US currency values.

```swift
let usCurrencyStrategy: IntegerParseStrategy =
    IntegerFormatStyle<Int>.Currency(code: "USD",
                                     locale: Locale(identifier: "en_US"))
    .parseStrategy
let currencyValues = ["$100", "$1,000", "$10,000", "€100"]
let parsedValues = currencyValues.map { try? usCurrencyStrategy.parse($0) } // [Optional(100), Optional(1000), Optional(10000), nil]
```

You don’t need to instantiate a parse strategy variable to parse a single string. Instead, use the [BinaryInteger](../swift/binaryinteger.md) initializers that take a source [String](../swift/string.md) and a `format` parameter to parse the string according to the provided [FormatStyle](formatstyle.md). The following example parses a string that represents a currency value in US dollars.

```swift
let formattedUSDollars = "$1,234"
let parsedUSDollars = try? Int(formattedUSDollars, format: .currency(code: "USD")
    .locale(Locale(identifier: "en_US"))) // 1234
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [ParseStrategy](parsestrategy.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an integer parse strategy

- [init(format:lenient:)](<integerparsestrategy/init(format_lenient_)-124xn.md>) — Creates a parse strategy instance using the specified integer format style.
- [init(format:lenient:)](<integerparsestrategy/init(format_lenient_)-7tox3.md>) — Creates a parse strategy instance using the specified integer currency format style.
- [init(format:lenient:)](<integerparsestrategy/init(format_lenient_)-3gbvo.md>) — Creates a parse strategy instance using the specified integer percentage format style.

### Parsing strings

- [parse(_:)](<integerparsestrategy/parse(__).md>) — Parses an integer string in accordance with this strategy and returns the parsed value.

### Accessing strategy properties

- [formatStyle](integerparsestrategy/formatstyle.md) — The format style this strategy uses when parsing strings.
- [lenient](integerparsestrategy/lenient.md) — A Boolean value that indicates whether parsing allows any discrepencies in the expected format.

### Default Implementations

- [ParseStrategy Implementations](integerparsestrategy/parsestrategy-implementations.md)

## See Also

### Data parsing in Swift

- [ParseableFormatStyle](parseableformatstyle.md) — A type that can convert a given input data type into a representation in an output type.
- [ParseStrategy](parsestrategy.md) — A type that parses an input representation, such as a formatted string, into a provided data type.
- [FloatingPointParseStrategy](floatingpointparsestrategy.md) — A parse strategy for creating floating-point values from formatted strings.
- [ParseStrategy](decimal/parsestrategy.md) — A parse strategy for creating decimal values from formatted strings.
