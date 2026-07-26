---
title: locale
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/listformatstyle/locale
source_url: 'https://developer.apple.com/documentation/foundation/listformatstyle/locale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/listformatstyle/locale.json'
content_hash: 'sha256:99a1c7331667ae63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ListFormatStyle](../listformatstyle.md)

# locale

<sub>Instance Property</sub>

The locale to use when formatting items in the list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var locale: Locale
```

## Discussion

A [Locale](../locale.md) instance is typically used to provide, format, and interpret information about and according to the user’s customs and preferences.

Examples include ISO region and language codes, currency code, calendar, system of measurement, and decimal separator.

The default value is [autoupdatingCurrent](../locale/autoupdatingcurrent.md). If you set this property to `nil`, the formatter resets to using `autoupdatingCurrent`.

## See Also

### Modifying a list format style

- [width](width-swift.property.md) — The size of the list.
- [Width](width-swift.enum.md) — The type representing the width of a list.
- [listType](listtype-swift.property.md) — The type of the list.
- [ListType](listtype-swift.enum.md) — A type that describes whether the returned list contains cumulative or alternative elements.
- [locale(_:)](<locale(__).md>) — Modifies the list format style to use the specified locale.
