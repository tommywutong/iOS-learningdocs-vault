---
title: 'formatted(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/datecomponents/formatted(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/datecomponents/formatted(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponents/formatted%28_%3A%29.json'
content_hash: 'sha256:fa5711ee906f61a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponents](../datecomponents.md)

# formatted(_:)

<sub>Instance Method</sub>

Converts `self` to its textual representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formatted<F>(_ format: F) -> F.FormatOutput where F : FormatStyle, F.FormatInput == DateComponents
```

## Parameters

- `format` — The format for formatting `self`.

## Return Value

A representation of `self` using the given `format`. The type of the representation is specified by `FormatStyle.FormatOutput`.
