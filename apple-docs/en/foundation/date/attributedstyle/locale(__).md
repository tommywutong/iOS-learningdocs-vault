---
title: 'locale(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+（18.0 起废弃）, iPadOS 15.0+（18.0 起废弃）, Mac Catalyst 15.0+（18.0 起废弃）, macOS 12.0+（15.0 起废弃）, tvOS 15.0+（18.0 起废弃）, visionOS 1.0+, watchOS 8.0+（11.0 起废弃）]
languages: [swift, swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/foundation/date/attributedstyle/locale(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/attributedstyle/locale(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/attributedstyle/locale%28_%3A%29.json'
content_hash: 'sha256:7292cd7dcc329854'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [AttributedStyle](../attributedstyle.md)

# locale(_:)

<sub>Instance Method</sub>

Modifies the date attributed style to use the specified locale.

> [!warning] Deprecated
> Use Date.FormatStyle.Attributed or Date.VerbatimFormatStyle.Attributed instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func locale(_ locale: Locale) -> Date.AttributedStyle
```

## Parameters

- `locale` — The locale to use when formatting a date.

## Return Value

A date attributed style with the provided locale.
