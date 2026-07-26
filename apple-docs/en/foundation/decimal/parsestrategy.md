---
title: Decimal.ParseStrategy
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/decimal/parsestrategy
source_url: 'https://developer.apple.com/documentation/foundation/decimal/parsestrategy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal/parsestrategy.json'
content_hash: 'sha256:8b9ab95ede1ceeba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Decimal](../decimal.md)

# Decimal.ParseStrategy

<sub>Structure</sub>

A parse strategy for creating decimal values from formatted strings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ParseStrategy<Format> where Format : FormatStyle, Format.FormatInput == Decimal
```

## Overview

Create an explicit [ParseStrategy](parsestrategy.md) to parse mulitple strings according to the same parse strategy. In the following example, `usCurrencyStrategy` is a [ParseStrategy](parsestrategy.md) that uses US dollars and the `en_US` locale’s conventions for number formatting. The example then uses this strategy to parse an array of strings, some of which represent valid US currency values.

```swift
let usCurrencyStrategy: Decimal.ParseStrategy =
Decimal.FormatStyle.Currency(code: "USD",
                             locale: Locale(identifier: "en_US"))
.parseStrategy
let currencyValues = ["$100.11", "$1,000.22", "$10,000.33", "€100.44"]
let parsedValues = currencyValues.map { try? usCurrencyStrategy.parse($0) } // [Optional(100.11), Optional(1000.22), Optional(10000.33), nil]
```

You don’t need to instantiate a parse strategy variable to parse a single string. Instead, use the [init(_:format:lenient:)](<init(__format_lenient_)-3u6o6.md>) initializer, which takes a source [String](../../swift/string.md) and a `format` parameter to parse the string according to the provided [FormatStyle](formatstyle.md). The following example parses a string that represents a currency value in US dollars.

```swift
let formattedUSDollars = "$1,234.56"
let parsedUSDollars = try? Decimal(formattedUSDollars, format: .currency(code: "USD")
    .locale(Locale(identifier: "en_US"))) // 1234.56
```

Decimal also has an [init(_:strategy:)](<init(__strategy_).md>) initializer, if it’s more convenient to pass a [ParseStrategy](parsestrategy.md) instance rather than implicitly derive a strategy from a [FormatStyle](formatstyle.md).

## Relationships

- **Conforms To**: [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [ParseStrategy](../parsestrategy.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a decimal parse strategy

- [init(format:lenient:)](<parsestrategy/init(format_lenient_)-46ix2.md>) — Creates a parse strategy instance using the specified decimal format style.
- [init(format:lenient:)](<parsestrategy/init(format_lenient_)-22h06.md>) — Creates a parse strategy instance using the specified decimal currency format style.
- [init(format:lenient:)](<parsestrategy/init(format_lenient_)-36ja3.md>) — Creates a parse strategy instance using the specified decimal percentage format style.

### Parsing strings

- [parse(_:)](<parsestrategy/parse(__).md>) — Parses a decimal string in accordance with this strategy and returns the parsed value.

### Accessing strategy properties

- [formatStyle](parsestrategy/formatstyle.md) — The format style this strategy uses when parsing strings.
- [lenient](parsestrategy/lenient.md) — A Boolean value that indicates whether parsing allows any discrepencies in the expected format.

### Default Implementations

- [ParseStrategy Implementations](parsestrategy/parsestrategy-implementations.md)

## See Also

### Data parsing in Swift

- [ParseableFormatStyle](../parseableformatstyle.md) — A type that can convert a given input data type into a representation in an output type.
- [ParseStrategy](../parsestrategy.md) — A type that parses an input representation, such as a formatted string, into a provided data type.
- [IntegerParseStrategy](../integerparsestrategy.md) — A parse strategy for creating integer values from formatted strings.
- [FloatingPointParseStrategy](../floatingpointparsestrategy.md) — A parse strategy for creating floating-point values from formatted strings.
