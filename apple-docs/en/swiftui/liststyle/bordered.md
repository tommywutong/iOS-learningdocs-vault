---
title: bordered
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 12.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/liststyle/bordered
source_url: 'https://developer.apple.com/documentation/swiftui/liststyle/bordered'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/liststyle/bordered.json'
content_hash: 'sha256:2783f053846289c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ListStyle](../liststyle.md)

# bordered

<sub>Type Property</sub>

The list style that describes the behavior and appearance of a list with standard border.

<sub>macOS</sub>

```swift
@export(implementation) static var bordered: BorderedListStyle { get }
```

## Discussion

Bordered lists are expected to be inset from their outer containers, but do not have inset style rows or selection.

To customize whether the rows of the list should alternate their backgrounds, use [bordered(alternatesRowBackgrounds:)](<bordered(alternatesrowbackgrounds_).md>).

## See Also

### Getting built-in list styles

- [automatic](automatic.md) — The list style that describes a platform’s default behavior and appearance for a list.
- [carousel](carousel.md) — The carousel list style.
- [elliptical](elliptical.md) — The list style that describes the behavior and appearance of an elliptical list.
- [grouped](grouped.md) — The list style that describes the behavior and appearance of a grouped list.
- [inset](inset.md) — The list style that describes the behavior and appearance of an inset list.
- [insetGrouped](insetgrouped.md) — The list style that describes the behavior and appearance of an inset grouped list.
- [plain](plain.md) — The list style that describes the behavior and appearance of a plain list.
- [sidebar](sidebar.md) — The list style that describes the behavior and appearance of a sidebar list.
