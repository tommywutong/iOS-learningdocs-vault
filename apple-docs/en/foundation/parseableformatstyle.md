---
title: ParseableFormatStyle
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/parseableformatstyle
source_url: 'https://developer.apple.com/documentation/foundation/parseableformatstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/parseableformatstyle.json'
content_hash: 'sha256:82ec66a9e09b05e8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# ParseableFormatStyle

<sub>Protocol</sub>

A type that can convert a given input data type into a representation in an output type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ParseableFormatStyle : FormatStyle
```

## Relationships

- **Inherits From**: [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [FormatStyle](formatstyle.md), [Hashable](../swift/hashable.md)

- **Conforming Types**: [FormatStyle](date/formatstyle.md), [HTTPFormatStyle](date/httpformatstyle.md), [ISO8601FormatStyle](date/iso8601formatstyle.md), [VerbatimFormatStyle](date/verbatimformatstyle.md), [HTTPFormatStyle](datecomponents/httpformatstyle.md), [ISO8601FormatStyle](datecomponents/iso8601formatstyle.md), [FormatStyle](decimal/formatstyle.md), [Currency](decimal/formatstyle/currency.md), [Percent](decimal/formatstyle/percent.md), [FloatingPointFormatStyle](floatingpointformatstyle.md), [Currency](floatingpointformatstyle/currency.md), [Percent](floatingpointformatstyle/percent.md), [IntegerFormatStyle](integerformatstyle.md), [Currency](integerformatstyle/currency.md), [Percent](integerformatstyle/percent.md), [FormatStyle](personnamecomponents/formatstyle.md), [FormatStyle](url/formatstyle.md)

## Topics

### Declaring Parse Strategy

- [parseStrategy](parseableformatstyle/parsestrategy.md) — A `ParseStrategy` that can be used to parse this `FormatStyle`’s output
- [Strategy](parseableformatstyle/strategy.md)

### Type Properties

- [http](parseableformatstyle/http-6qda5.md)
- [http](parseableformatstyle/http-yfpc.md)
- [iso8601](parseableformatstyle/iso8601-41vzo.md)
- [iso8601](parseableformatstyle/iso8601-55wjm.md)

### Type Methods

- [currency(code:)](<parseableformatstyle/currency(code_).md>)

### Default Implementations

- [FormatStyle Implementations](parseableformatstyle/formatstyle-implementations.md)

## See Also

### Data parsing in Swift

- [ParseStrategy](parsestrategy.md) — A type that parses an input representation, such as a formatted string, into a provided data type.
- [IntegerParseStrategy](integerparsestrategy.md) — A parse strategy for creating integer values from formatted strings.
- [FloatingPointParseStrategy](floatingpointparsestrategy.md) — A parse strategy for creating floating-point values from formatted strings.
- [ParseStrategy](decimal/parsestrategy.md) — A parse strategy for creating decimal values from formatted strings.
