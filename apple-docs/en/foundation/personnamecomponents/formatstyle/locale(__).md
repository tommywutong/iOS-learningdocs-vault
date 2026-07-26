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
doc_path: '/documentation/foundation/personnamecomponents/formatstyle/locale(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/personnamecomponents/formatstyle/locale(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/personnamecomponents/formatstyle/locale%28_%3A%29.json'
content_hash: 'sha256:bd6b3b64d98bef2a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [PersonNameComponents](../../personnamecomponents.md) · [FormatStyle](../formatstyle.md)

# locale(_:)

<sub>Instance Method</sub>

Modifies the person name components format style to use the specified locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func locale(_ locale: Locale) -> PersonNameComponents.FormatStyle
```

## Parameters

- `locale` — The locale to use when formatting person name components.

## Return Value

A person name components format style with the provided locale.

## See Also

### Modifying a Format Style

- [style](style-swift.property.md) — Specifies the style of the formatted result.
- [Style](style-swift.enum.md) — The type that represents the style of the formatted result.
- [locale](locale.md) — The locale to use when formatting the person name components.
- [attributed](attributed.md) — The style used to create a locale-aware attributed string representation of an instance of person name components.
