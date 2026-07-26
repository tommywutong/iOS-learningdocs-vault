---
title: 'parse(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/decimal/parsestrategy/parse(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/decimal/parsestrategy/parse(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal/parsestrategy/parse%28_%3A%29.json'
content_hash: 'sha256:61d1383f99e3f16f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Decimal](../../decimal.md) · [ParseStrategy](../parsestrategy.md)

# parse(_:)

<sub>Instance Method</sub>

Parses a decimal string in accordance with this strategy and returns the parsed value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func parse(_ value: String) throws -> Format.FormatInput
```

## Parameters

- `value` — The string to parse.

## Return Value

The parsed integer value.

## Discussion

Use this method to repeatedly parse decimal strings with the same [ParseStrategy](../parsestrategy.md). To parse a single decimal string, use the initializers inherited from [Decimal](../../decimal.md) that take a [String](../../../swift/string.md) and a [FormatStyle](../formatstyle.md) as parameters.

This method throws an error if the parse strategy can’t parse the provided string.
