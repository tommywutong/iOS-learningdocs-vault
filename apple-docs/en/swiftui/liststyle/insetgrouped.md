---
title: insetGrouped
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/liststyle/insetgrouped
source_url: 'https://developer.apple.com/documentation/swiftui/liststyle/insetgrouped'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/liststyle/insetgrouped.json'
content_hash: 'sha256:333cea8d7b5048ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ListStyle](../liststyle.md)

# insetGrouped

<sub>Type Property</sub>

The list style that describes the behavior and appearance of an inset grouped list.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@export(implementation) static var insetGrouped: InsetGroupedListStyle { get }
```

## Discussion

On iOS, the inset grouped list style displays a continuous background color that extends from the section header, around both sides of list items in the section, and down to the section footer. This visually groups the items to a greater degree than either the [inset](inset.md) or [grouped](grouped.md) styles do.

## See Also

### Getting built-in list styles

- [automatic](automatic.md) — The list style that describes a platform’s default behavior and appearance for a list.
- [bordered](bordered.md) — The list style that describes the behavior and appearance of a list with standard border.
- [carousel](carousel.md) — The carousel list style.
- [elliptical](elliptical.md) — The list style that describes the behavior and appearance of an elliptical list.
- [grouped](grouped.md) — The list style that describes the behavior and appearance of a grouped list.
- [inset](inset.md) — The list style that describes the behavior and appearance of an inset list.
- [plain](plain.md) — The list style that describes the behavior and appearance of a plain list.
- [sidebar](sidebar.md) — The list style that describes the behavior and appearance of a sidebar list.
