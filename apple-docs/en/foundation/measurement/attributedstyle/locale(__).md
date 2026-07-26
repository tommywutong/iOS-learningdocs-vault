---
title: 'locale(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/measurement/attributedstyle/locale(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/measurement/attributedstyle/locale(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/attributedstyle/locale%28_%3A%29.json'
content_hash: 'sha256:ee0f224f14e8df75'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Measurement](../../measurement.md) · [AttributedStyle](../attributedstyle.md)

# locale(_:)

<sub>Instance Method</sub>

Modifies the measurement format style to use the specified locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func locale(_ locale: Locale) -> Measurement<UnitType>.AttributedStyle
```

## Parameters

- `locale` — The locale to use when formatting a measurement.

## Return Value

A measurement format style with the specified locale.
