---
title: TabBarOnlyTabViewStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tabbaronlytabviewstyle
source_url: 'https://developer.apple.com/documentation/swiftui/tabbaronlytabviewstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabbaronlytabviewstyle.json'
content_hash: 'sha256:22d48c60cf40ffde'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TabBarOnlyTabViewStyle

<sub>Structure</sub>

A tab view style that displays a tab bar when possible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated struct TabBarOnlyTabViewStyle
```

## Overview

Use [tabBarOnly](tabviewstyle/tabbaronly.md) to construct this style.

To apply this style to a tab view, or to a view that contains tab views, use the [tabViewStyle(_:)](<view/tabviewstyle(__).md>) modifier.

## Relationships

- **Conforms To**: [TabViewStyle](tabviewstyle.md)

## Topics

### Initializers

- [init()](<tabbaronlytabviewstyle/init().md>)

## See Also

### Supporting types

- [DefaultTabViewStyle](defaulttabviewstyle.md) — The default tab view style.
- [SidebarAdaptableTabViewStyle](sidebaradaptabletabviewstyle.md) — A tab bar style that adapts to each platform.
- [GroupedTabViewStyle](groupedtabviewstyle.md) — A tab view style that displays a tab bar that groups its tabs together.
- [PageTabViewStyle](pagetabviewstyle.md) — A `TabViewStyle` that displays a paged scrolling `TabView`.
- [VerticalPageTabViewStyle](verticalpagetabviewstyle.md) — A `TabViewStyle` that displays a vertical `TabView` interaction and appearance.
- [CarouselTabViewStyle](carouseltabviewstyle.md) — A style that implements the carousel interaction and appearance. _(deprecated)_
