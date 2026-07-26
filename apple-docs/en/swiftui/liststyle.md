---
title: ListStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/liststyle
source_url: 'https://developer.apple.com/documentation/swiftui/liststyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/liststyle.json'
content_hash: 'sha256:d96aed749a9a194a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ListStyle

<sub>Protocol</sub>

A protocol that describes the behavior and appearance of a list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ListStyle
```

## Relationships

- **Conforming Types**: [BorderedListStyle](borderedliststyle.md), [CarouselListStyle](carouselliststyle.md), [DefaultListStyle](defaultliststyle.md), [EllipticalListStyle](ellipticalliststyle.md), [GroupedListStyle](groupedliststyle.md), [InsetGroupedListStyle](insetgroupedliststyle.md), [InsetListStyle](insetliststyle.md), [PlainListStyle](plainliststyle.md), [SidebarListStyle](sidebarliststyle.md)

## Topics

### Getting built-in list styles

- [automatic](liststyle/automatic.md) — The list style that describes a platform’s default behavior and appearance for a list.
- [bordered](liststyle/bordered.md) — The list style that describes the behavior and appearance of a list with standard border.
- [carousel](liststyle/carousel.md) — The carousel list style.
- [elliptical](liststyle/elliptical.md) — The list style that describes the behavior and appearance of an elliptical list.
- [grouped](liststyle/grouped.md) — The list style that describes the behavior and appearance of a grouped list.
- [inset](liststyle/inset.md) — The list style that describes the behavior and appearance of an inset list.
- [insetGrouped](liststyle/insetgrouped.md) — The list style that describes the behavior and appearance of an inset grouped list.
- [plain](liststyle/plain.md) — The list style that describes the behavior and appearance of a plain list.
- [sidebar](liststyle/sidebar.md) — The list style that describes the behavior and appearance of a sidebar list.

### Deprecated styles

- [bordered(alternatesRowBackgrounds:)](<liststyle/bordered(alternatesrowbackgrounds_).md>) — The list style that describes the behavior and appearance of a list with standard border. _(deprecated)_
- [inset(alternatesRowBackgrounds:)](<liststyle/inset(alternatesrowbackgrounds_).md>) — The list style that describes the behavior and appearance of an inset list with optional alternating row backgrounds. _(deprecated)_

### Supporting types

- [DefaultListStyle](defaultliststyle.md) — The list style that describes a platform’s default behavior and appearance for a list.
- [BorderedListStyle](borderedliststyle.md) — The list style that describes the behavior and appearance of a list with standard border.
- [CarouselListStyle](carouselliststyle.md) — The carousel list style.
- [EllipticalListStyle](ellipticalliststyle.md) — The list style that describes the behavior and appearance of an elliptical list.
- [GroupedListStyle](groupedliststyle.md) — The list style that describes the behavior and appearance of a grouped list.
- [InsetListStyle](insetliststyle.md) — The list style that describes the behavior and appearance of an inset list.
- [InsetGroupedListStyle](insetgroupedliststyle.md) — The list style that describes the behavior and appearance of an inset grouped list.
- [PlainListStyle](plainliststyle.md) — The list style that describes the behavior and appearance of a plain list.
- [SidebarListStyle](sidebarliststyle.md) — The list style that describes the behavior and appearance of a sidebar list.

## See Also

### Styling collection views

- [listStyle(_:)](<view/liststyle(__).md>) — Sets the style for lists within this view.
- [tableStyle(_:)](<view/tablestyle(__).md>) — Sets the style for tables within this view.
- [TableStyle](tablestyle.md) — A type that applies a custom appearance to all tables within a view.
- [TableStyleConfiguration](tablestyleconfiguration.md) — The properties of a table.
- [disclosureGroupStyle(_:)](<view/disclosuregroupstyle(__).md>) — Sets the style for disclosure groups within this view.
- [DisclosureGroupStyle](disclosuregroupstyle.md) — A type that specifies the appearance and interaction of disclosure groups within a view hierarchy.
