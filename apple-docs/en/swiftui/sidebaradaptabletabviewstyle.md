---
title: SidebarAdaptableTabViewStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sidebaradaptabletabviewstyle
source_url: 'https://developer.apple.com/documentation/swiftui/sidebaradaptabletabviewstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sidebaradaptabletabviewstyle.json'
content_hash: 'sha256:460a9e8fcd53aec4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SidebarAdaptableTabViewStyle

<sub>Structure</sub>

A tab bar style that adapts to each platform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated struct SidebarAdaptableTabViewStyle
```

## Overview

Tab views using the sidebar adaptable style have an appearance that varies depending on the platform:

- iPadOS displays a top tab bar that can adapt into a sidebar.
- iOS displays a bottom tab bar.
- macOS and tvOS always show a sidebar.
- visionOS shows an ornament and also shows a sidebar for secondary tabs within a [TabSection](tabsection.md).

Use [sidebarAdaptable](tabviewstyle/sidebaradaptable.md) to construct this style.

To apply this style to a tab view, or to a view that contains tab views, use the [tabViewStyle(_:)](<view/tabviewstyle(__).md>) modifier.

## Relationships

- **Conforms To**: [TabViewStyle](tabviewstyle.md)

## Topics

### Initializers

- [init()](<sidebaradaptabletabviewstyle/init().md>)

## See Also

### Supporting types

- [DefaultTabViewStyle](defaulttabviewstyle.md) — The default tab view style.
- [TabBarOnlyTabViewStyle](tabbaronlytabviewstyle.md) — A tab view style that displays a tab bar when possible.
- [GroupedTabViewStyle](groupedtabviewstyle.md) — A tab view style that displays a tab bar that groups its tabs together.
- [PageTabViewStyle](pagetabviewstyle.md) — A `TabViewStyle` that displays a paged scrolling `TabView`.
- [VerticalPageTabViewStyle](verticalpagetabviewstyle.md) — A `TabViewStyle` that displays a vertical `TabView` interaction and appearance.
- [CarouselTabViewStyle](carouseltabviewstyle.md) — A style that implements the carousel interaction and appearance. _(deprecated)_
