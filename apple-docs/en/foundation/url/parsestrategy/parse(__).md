---
title: 'parse(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/parsestrategy/parse(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/parsestrategy/parse(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/parsestrategy/parse%28_%3A%29.json'
content_hash: 'sha256:7af5b2e202136c94'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URL](../../url.md) · [ParseStrategy](../parsestrategy.md)

# parse(_:)

<sub>Instance Method</sub>

Parses a URL string in accordance with this strategy and returns the parsed value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func parse(_ value: String) throws -> URL
```

## Parameters

- `value` — The string to parse.

## Return Value

The parsed integer value.

## Discussion

Use this method to repeatedly parse integer strings with the same [ParseStrategy](../parsestrategy.md). To parse a single integer string, use the URL initializer [init(_:strategy:)](<../init(__strategy_).md>).

This method throws an error if the parse strategy can’t parse the provided string.
