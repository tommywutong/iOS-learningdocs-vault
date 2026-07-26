---
title: 'month(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/attributed-swift.struct/month(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/attributed-swift.struct/month(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/attributed-swift.struct/month%28_%3A%29.json'
content_hash: 'sha256:a9e97175b2f89062'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [FormatStyle](../../formatstyle.md) · [Attributed](../attributed-swift.struct.md)

# month(_:)

<sub>Instance Method</sub>

Change the representation of the month in the format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func month(_ format: Date.FormatStyle.Symbol.Month = .abbreviated) -> Date.FormatStyle.Attributed
```

## Parameters

- `format` — Set the symbol representation or pass `nil` to remove it.
