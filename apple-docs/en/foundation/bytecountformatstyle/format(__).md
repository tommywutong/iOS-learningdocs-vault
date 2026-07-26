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
doc_path: '/documentation/foundation/bytecountformatstyle/format(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/bytecountformatstyle/format(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bytecountformatstyle/format%28_%3A%29.json'
content_hash: 'sha256:d3a459ae8e026a09'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ByteCountFormatStyle](../bytecountformatstyle.md)

# format(_:)

<sub>Instance Method</sub>

Formats a numeric byte count, using this style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func format(_ value: Int64) -> String
```

## Parameters

- `value` — The 64-bit byte count to format.

## Return Value

A formatted representation of `value`, formatted according to the style’s configuration.

## Discussion

Use this method when you want to create a single style instance, and then use it to format multiple values. The following example creates a [ByteCountFormatStyle](../bytecountformatstyle.md) to format values as kilobyte counts, then applies this style to an array of [Int64](../../swift/int64.md) values.

```swift
let style = ByteCountFormatStyle(style: .memory,
                                 allowedUnits: [.kb],
                                 spellsOutZero: true,
                                 includesActualByteCount: false,
                                 locale: Locale(identifier: "en_US"))
let counts: [Int64] = [0, 1024, 2048, 4096, 8192, 16384, 32768, 65536]
let formatted = counts.map ( {style.format($0) } ) // ["Zero kB", "1 kB", "2 kB", "4 kB", "8 kB", "16 kB", "32 kB", "64 kB"]

```

To format a single integer, use the [BinaryInteger](../../swift/binaryinteger.md) instance method [formatted(_:)](<../../swift/binaryinteger/formatted(__)-4qd73.md>), passing in an instance of [IntegerFormatStyle](../integerformatstyle.md), or [formatted()](<../../swift/binaryinteger/formatted().md>) to use a default style.
