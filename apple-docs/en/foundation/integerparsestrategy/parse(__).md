---
title: 'parse(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/integerparsestrategy/parse(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/integerparsestrategy/parse(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/integerparsestrategy/parse%28_%3A%29.json'
content_hash: 'sha256:a4b53d19991cfac0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IntegerParseStrategy](../integerparsestrategy.md)

# parse(_:)

<sub>Instance Method</sub>

Parses an integer string in accordance with this strategy and returns the parsed value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func parse(_ value: String) throws -> Format.FormatInput
```

## Parameters

- `value` — The string to parse.

## Return Value

The parsed integer value.

## Discussion

Use this method to repeatedly parse integer strings with the same [IntegerParseStrategy](../integerparsestrategy.md). To parse a single integer string, use the initializers inherited from [BinaryInteger](../../swift/binaryinteger.md) that take a [String](../../swift/string.md) and a [FormatStyle](../formatstyle.md) as parameters.

This method throws an error if the parse strategy can’t parse the provided string.
