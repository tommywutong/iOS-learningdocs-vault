---
title: 'parse(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/parsestrategy/parse(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/parsestrategy/parse(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/parsestrategy/parse%28_%3A%29.json'
content_hash: 'sha256:eac47677325c92ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ParseStrategy](../parsestrategy.md)

# parse(_:)

<sub>Instance Method</sub>

Parses a value, using this strategy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func parse(_ value: Self.ParseInput) throws -> Self.ParseOutput
```

## Parameters

- `value` — A value whose type matches the strategy’s [ParseInput](parseinput.md) type.

## Return Value

A parsed value of the type declared by [ParseOutput](parseoutput.md).

## Discussion

This method throws an error if the parse strategy can’t parse `value`.
