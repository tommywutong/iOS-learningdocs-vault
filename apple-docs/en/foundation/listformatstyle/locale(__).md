---
title: 'locale(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/listformatstyle/locale(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/listformatstyle/locale(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/listformatstyle/locale%28_%3A%29.json'
content_hash: 'sha256:30faa3ee6d39a909'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ListFormatStyle](../listformatstyle.md)

# locale(_:)

<sub>Instance Method</sub>

Modifies the list format style to use the specified locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func locale(_ locale: Locale) -> ListFormatStyle<Style, Base>
```

## Parameters

- `locale` — The locale to use when formatting items in the list.

## Return Value

A list format style with the provided locale.

## See Also

### Modifying a list format style

- [width](width-swift.property.md) — The size of the list.
- [Width](width-swift.enum.md) — The type representing the width of a list.
- [listType](listtype-swift.property.md) — The type of the list.
- [ListType](listtype-swift.enum.md) — A type that describes whether the returned list contains cumulative or alternative elements.
- [locale](locale.md) — The locale to use when formatting items in the list.
