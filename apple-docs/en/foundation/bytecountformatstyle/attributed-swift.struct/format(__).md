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
doc_path: '/documentation/foundation/bytecountformatstyle/attributed-swift.struct/format(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatstyle/attributed-swift.struct/format(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatstyle/attributed-swift.struct/format%28_%3A%29.json'
content_hash: 'sha256:6f07049aff066617'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [ByteCountFormatStyle](../../bytecountformatstyle.md) · [Attributed](../attributed-swift.struct.md)

# format(_:)

<sub>Instance Method</sub>

Formats a numeric byte count, using this style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func format(_ value: Int64) -> AttributedString
```

## Parameters

- `value` — The 64-bit byte count to format.

## Return Value

A formatted representation of `value`, formatted according to the style’s configuration.

## Discussion

Use this method when you want to create a single style instance, and then use it to format multiple values. To format a single integer, use the [BinaryInteger](../../../swift/binaryinteger.md) instance method [formatted(_:)](<../../../swift/binaryinteger/formatted(__)-4qd73.md>), passing in an instance of [Attributed](../attributed-swift.struct.md), or [formatted()](<../../../swift/binaryinteger/formatted().md>) to use a default style.
