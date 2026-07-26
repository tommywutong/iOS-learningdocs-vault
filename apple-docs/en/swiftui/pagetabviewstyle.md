---
title: PageTabViewStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/pagetabviewstyle
source_url: 'https://developer.apple.com/documentation/swiftui/pagetabviewstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pagetabviewstyle.json'
content_hash: 'sha256:8053305e877ade02'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PageTabViewStyle

<sub>Structure</sub>

A `TabViewStyle` that displays a paged scrolling `TabView`.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct PageTabViewStyle
```

## Overview

Use [page](tabviewstyle/page.md) or [page(indexDisplayMode:)](<tabviewstyle/page(indexdisplaymode_).md>) to construct this style.

To apply this style to a tab view, or to a view that contains tab views, use the [tabViewStyle(_:)](<view/tabviewstyle(__).md>) modifier.

## Relationships

- **Conforms To**: [TabViewStyle](tabviewstyle.md)

## Topics

### Creating a page tab view style

- [init(indexDisplayMode:)](<pagetabviewstyle/init(indexdisplaymode_).md>) — Creates a new `PageTabViewStyle` with an index display mode
- [IndexDisplayMode](pagetabviewstyle/indexdisplaymode.md) — A style for displaying the page index view

## See Also

### Supporting types

- [DefaultTabViewStyle](defaulttabviewstyle.md) — The default tab view style.
- [SidebarAdaptableTabViewStyle](sidebaradaptabletabviewstyle.md) — A tab bar style that adapts to each platform.
- [TabBarOnlyTabViewStyle](tabbaronlytabviewstyle.md) — A tab view style that displays a tab bar when possible.
- [GroupedTabViewStyle](groupedtabviewstyle.md) — A tab view style that displays a tab bar that groups its tabs together.
- [VerticalPageTabViewStyle](verticalpagetabviewstyle.md) — A `TabViewStyle` that displays a vertical `TabView` interaction and appearance.
- [CarouselTabViewStyle](carouseltabviewstyle.md) — A style that implements the carousel interaction and appearance. _(deprecated)_
