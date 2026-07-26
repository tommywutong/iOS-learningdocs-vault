---
title: GroupedTabViewStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/groupedtabviewstyle
source_url: 'https://developer.apple.com/documentation/swiftui/groupedtabviewstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/groupedtabviewstyle.json'
content_hash: 'sha256:a3fd893e414b0332'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# GroupedTabViewStyle

<sub>Structure</sub>

A tab view style that displays a tab bar that groups its tabs together.

<sub>macOS</sub>

```swift
nonisolated struct GroupedTabViewStyle
```

## Overview

Use [grouped](tabviewstyle/grouped.md) to construct this style.

To apply this style to a tab view, or to a view that contains tab views, use the [tabViewStyle(_:)](<view/tabviewstyle(__).md>) modifier.

## Relationships

- **Conforms To**: [TabViewStyle](tabviewstyle.md)

## Topics

### Initializers

- [init()](<groupedtabviewstyle/init().md>)

## See Also

### Supporting types

- [DefaultTabViewStyle](defaulttabviewstyle.md) — The default tab view style.
- [SidebarAdaptableTabViewStyle](sidebaradaptabletabviewstyle.md) — A tab bar style that adapts to each platform.
- [TabBarOnlyTabViewStyle](tabbaronlytabviewstyle.md) — A tab view style that displays a tab bar when possible.
- [PageTabViewStyle](pagetabviewstyle.md) — A `TabViewStyle` that displays a paged scrolling `TabView`.
- [VerticalPageTabViewStyle](verticalpagetabviewstyle.md) — A `TabViewStyle` that displays a vertical `TabView` interaction and appearance.
- [CarouselTabViewStyle](carouseltabviewstyle.md) — A style that implements the carousel interaction and appearance. _(deprecated)_
