---
title: 'timeZone(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/formatstyle/attributed-swift.struct/timezone(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/formatstyle/attributed-swift.struct/timezone(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/formatstyle/attributed-swift.struct/timezone%28_%3A%29.json'
content_hash: 'sha256:fa22a3ba9f297196'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Foundation](../../../../foundation.md) · [Date](../../../date.md) · [FormatStyle](../../formatstyle.md) · [Attributed](../attributed-swift.struct.md)

# timeZone(_:)

<sub>Instance Method</sub>

Change the representation of the time zone in the format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func timeZone(_ format: Date.FormatStyle.Symbol.TimeZone = .specificName(.short)) -> Date.FormatStyle.Attributed
```

## Parameters

- `format` — Set the symbol representation or pass `nil` to remove it.
