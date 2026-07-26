---
title: 'format(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/formatstyle/format(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/format(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/format%28_%3A%29.json'
content_hash: 'sha256:0937aaf7098aef47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# format(_:)

<sub>Instance Method</sub>

Formats a value, using this style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func format(_ value: Self.FormatInput) -> Self.FormatOutput
```

## Parameters

- `value` — The value to format.

## Return Value

A representation of `value`, in the [FormatOutput](formatoutput.md) type, formatted according to the style’s configuration.

## Discussion

Use this method when you want to create a single style instance, and then use it to format multiple values.
