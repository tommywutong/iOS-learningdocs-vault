---
title: 'format(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/decimal/formatstyle/attributed-swift.struct/format(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/decimal/formatstyle/attributed-swift.struct/format(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/decimal/formatstyle/attributed-swift.struct/format%28_%3A%29.json'
content_hash: 'sha256:5aa38115f75e2a95'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Decimal](../../../decimal.md) · [FormatStyle](../../formatstyle.md) · [Attributed](../attributed-swift.struct.md)

# format(_:)

<sub>Instance Method</sub>

Formats a decimal value, using this style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func format(_ value: Decimal) -> AttributedString
```

## Parameters

- `value` — The decimal value to format.

## Return Value

An attributed string representation of `value`, formatted according to the style’s configuration. The returned string contains attributes from the [NumberFormatAttributes](../../../attributescopes/foundationattributes/numberformatattributes.md) attribute scope to indicate runs formatted by this format style.
