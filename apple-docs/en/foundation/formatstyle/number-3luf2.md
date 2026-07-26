---
title: number
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/formatstyle/number-3luf2
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/number-3luf2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/number-3luf2.json'
content_hash: 'sha256:c123529d6c459bfb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# number

<sub>Type Property</sub>

A style for formatting decimal values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var number: Decimal.FormatStyle { get }
```

## Discussion

Use this type property when the call point allows the use of [FormatStyle](../decimal/formatstyle.md). You typically do this when calling the [formatted(_:)](<../decimal/formatted(__).md>) method of [Decimal](../decimal.md).

## See Also

### Applying numeric styles for decimals

- [FormatStyle](../decimal/formatstyle.md) — A structure that converts between decimal values and their textual representations.
