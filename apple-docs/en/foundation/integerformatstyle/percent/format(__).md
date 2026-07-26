---
title: 'format(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/integerformatstyle/percent/format(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/integerformatstyle/percent/format(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/integerformatstyle/percent/format%28_%3A%29.json'
content_hash: 'sha256:19017a2ccb13994c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [IntegerFormatStyle](../../integerformatstyle.md) · [Percent](../percent.md)

# format(_:)

<sub>Instance Method</sub>

Formats an integer, using this style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func format(_ value: Value) -> String
```

## Parameters

- `value` — The integer to format.

## Return Value

A string representation of `value`, formatted according to the style’s configuration.

## Discussion

Use this method when you want to create a single style instance, and then use it to format multiple integers. To format a single integer, use the [BinaryInteger](../../../swift/binaryinteger.md) instance method [formatted(_:)](<../../../swift/binaryinteger/formatted(__)-4qd73.md>), passing in an instance of [Percent](../percent.md), or [formatted()](<../../../swift/binaryinteger/formatted().md>) to use a default style.
