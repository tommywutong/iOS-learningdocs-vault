---
title: elliptical
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/liststyle/elliptical
source_url: 'https://developer.apple.com/documentation/swiftui/liststyle/elliptical'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/liststyle/elliptical.json'
content_hash: 'sha256:f0c012f1a42eef9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ListStyle](../liststyle.md)

# elliptical

<sub>Type Property</sub>

The list style that describes the behavior and appearance of an elliptical list.

<sub>watchOS</sub>

```swift
@export(implementation) static var elliptical: EllipticalListStyle { get }
```

## Discussion

On watchOS, the elliptical list style uses a transform for items rolling off the top or bottom of the list, as if on a rounded surface that faces the user.

Apple Watch Series 3 does not support this style and will instead fall back to using the [plain](plain.md) style.

## See Also

### Getting built-in list styles

- [automatic](automatic.md) — The list style that describes a platform’s default behavior and appearance for a list.
- [bordered](bordered.md) — The list style that describes the behavior and appearance of a list with standard border.
- [carousel](carousel.md) — The carousel list style.
- [grouped](grouped.md) — The list style that describes the behavior and appearance of a grouped list.
- [inset](inset.md) — The list style that describes the behavior and appearance of an inset list.
- [insetGrouped](insetgrouped.md) — The list style that describes the behavior and appearance of an inset grouped list.
- [plain](plain.md) — The list style that describes the behavior and appearance of a plain list.
- [sidebar](sidebar.md) — The list style that describes the behavior and appearance of a sidebar list.
