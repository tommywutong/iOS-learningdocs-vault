---
title: 'format(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/decimal/formatstyle/percent/format(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/decimal/formatstyle/percent/format(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal/formatstyle/percent/format%28_%3A%29.json'
content_hash: 'sha256:cbda6bd8ec2bbf08'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Decimal](../../../decimal.md) · [FormatStyle](../../formatstyle.md) · [Percent](../percent.md)

# format(_:)

<sub>Instance Method</sub>

Formats an decimal, using this style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func format(_ value: Decimal) -> String
```

## Parameters

- `value` — The decimal to format.

## Return Value

A string representation of `value`, formatted according to the style’s configuration.

## Discussion

Use this method when you want to create a single style instance, and then use it to format multiple decimal. To format a single integer, use the 1414588 instance method [formatted(_:)](<../../formatted(__).md>), passing in an instance of [Percent](../percent.md), or call [formatted()](<../../formatted().md>) to use a default style.
