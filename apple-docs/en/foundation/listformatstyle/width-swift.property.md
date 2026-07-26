---
title: width
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/listformatstyle/width-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/listformatstyle/width-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/listformatstyle/width-swift.property.json'
content_hash: 'sha256:617cc26dc32bca6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ListFormatStyle](../listformatstyle.md)

# width

<sub>Instance Property</sub>

The size of the list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var width: ListFormatStyle<Style, Base>.Width
```

## Discussion

The `width` property controls the size of the list. The [locale](locale.md) determines the formatting and abbreviation of the string for the given `width`.

For example, for English:

```swift
["One", "Two", "Three"].formatted(.list(type: .and, width: .standard))
// “One, Two, and Three”

["One", "Two", "Three"].formatted(.list(type: .and, width: .short))
// “One, Two, & Three” 

["One", "Two", "Three"].formatted(.list(type: .and, width: .narrow))
// “One, Two, Three” 
```

The default value is [ListFormatStyle.Width.standard](width-swift.enum/standard.md).

## See Also

### Modifying a list format style

- [Width](width-swift.enum.md) — The type representing the width of a list.
- [listType](listtype-swift.property.md) — The type of the list.
- [ListType](listtype-swift.enum.md) — A type that describes whether the returned list contains cumulative or alternative elements.
- [locale](locale.md) — The locale to use when formatting items in the list.
- [locale(_:)](<locale(__).md>) — Modifies the list format style to use the specified locale.
