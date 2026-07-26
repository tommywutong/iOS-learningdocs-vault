---
title: listType
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/listformatstyle/listtype-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/listformatstyle/listtype-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/listformatstyle/listtype-swift.property.json'
content_hash: 'sha256:e83476ca6de33931'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ListFormatStyle](../listformatstyle.md)

# listType

<sub>Instance Property</sub>

The type of the list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var listType: ListFormatStyle<Style, Base>.ListType
```

## Discussion

The list type determines the semantics used in the return string.

For example, for en_US:

```swift
["One", "Two", "Three"].formatted(.list(type: .and))
// “One, Two, and Three”

["One", "Two", "Three"].formatted(.list(type: .or))
// “One, Two, or Three” 
```

The default value is [ListFormatStyle.ListType.and](listtype-swift.enum/and.md).

## See Also

### Modifying a list format style

- [width](width-swift.property.md) — The size of the list.
- [Width](width-swift.enum.md) — The type representing the width of a list.
- [ListType](listtype-swift.enum.md) — A type that describes whether the returned list contains cumulative or alternative elements.
- [locale](locale.md) — The locale to use when formatting items in the list.
- [locale(_:)](<locale(__).md>) — Modifies the list format style to use the specified locale.
