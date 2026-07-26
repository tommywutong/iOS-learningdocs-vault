---
title: ParseStrategy
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/parsestrategy
source_url: 'https://developer.apple.com/documentation/foundation/parsestrategy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/parsestrategy.json'
content_hash: 'sha256:a186ada32b020695'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# ParseStrategy

<sub>Protocol</sub>

A type that parses an input representation, such as a formatted string, into a provided data type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ParseStrategy : Decodable, Encodable, Hashable
```

## Overview

A [ParseStrategy](parsestrategy.md) allows you to convert a formatted representation into a data type, using one of two approaches:

- Initialize the data type by calling an initializer of that type that takes a formatted instance and a parse strategy as parameters. For example, you can create a [Decimal](decimal.md) from a formatted string with the initializer [init(_:format:lenient:)](<decimal/init(__format_lenient_)-6fk71.md>).
- Create a parse strategy and call its [parse(_:)](<parsestrategy/parse(__).md>) method on one or more formatted instances.

[ParseStrategy](parsestrategy.md) is closely related to [FormatStyle](formatstyle.md), which provides the opposite conversion: from data type to formatted representation. To use a parse strategy, you create a [FormatStyle](formatstyle.md) to define the representation you expect, then access the style’s `parseStrategy` property to get a strategy instance.

The following example creates a [Currency](decimal/formatstyle/currency.md) format style that uses US dollars and US English number-formatting conventions. It then creates a [Decimal](decimal.md) instance by providing a formatted string to parse and the format style’s [parseStrategy](decimal/formatstyle/currency/parsestrategy.md).

```swift
let style = Decimal.FormatStyle.Currency(code: "USD",
                                         locale: Locale(identifier: "en_US"))
let parsed = try? Decimal("$12,345.67",
                           strategy: style.parseStrategy) // 12345.67
```

## Relationships

- **Inherits From**: [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

- **Conforming Types**: [FormatStyle](date/formatstyle.md), [HTTPFormatStyle](date/httpformatstyle.md), [ISO8601FormatStyle](date/iso8601formatstyle.md), [ParseStrategy](date/parsestrategy.md), [HTTPFormatStyle](datecomponents/httpformatstyle.md), [ISO8601FormatStyle](datecomponents/iso8601formatstyle.md), [ParseStrategy](decimal/parsestrategy.md), [FloatingPointParseStrategy](floatingpointparsestrategy.md), [IntegerParseStrategy](integerparsestrategy.md), [ParseStrategy](personnamecomponents/parsestrategy.md), [ParseStrategy](url/parsestrategy.md)

## Topics

### Performing parsing

- [parse(_:)](<parsestrategy/parse(__).md>) — Parses a value, using this strategy.

### Commonly-used parsers

- [fixed(format:timeZone:locale:)](<parsestrategy/fixed(format_timezone_locale_).md>) — A fixed-format date parse strategy.
- [url](parsestrategy/url.md) — A parse strategy for URLs.
- [name](parsestrategy/name.md) — A parse strategy for person name components.

### Commonly-used format styles

- [dateTime](parsestrategy/datetime.md) — A default format style for formatting dates.

### Supporting types

- [ParseInput](parsestrategy/parseinput.md) — The input type parsed by this strategy.
- [ParseOutput](parsestrategy/parseoutput.md) — The output type returned by this strategy.

### Type Properties

- [http](parsestrategy/http-5mpzc.md)
- [http](parsestrategy/http-6hyig.md)
- [iso8601](parsestrategy/iso8601-69scf.md)
- [iso8601](parsestrategy/iso8601-8z0au.md) — A style for formatting a date in accordance with the ISO-8601 standard.

## See Also

### Data parsing in Swift

- [ParseableFormatStyle](parseableformatstyle.md) — A type that can convert a given input data type into a representation in an output type.
- [IntegerParseStrategy](integerparsestrategy.md) — A parse strategy for creating integer values from formatted strings.
- [FloatingPointParseStrategy](floatingpointparsestrategy.md) — A parse strategy for creating floating-point values from formatted strings.
- [ParseStrategy](decimal/parsestrategy.md) — A parse strategy for creating decimal values from formatted strings.
