---
title: VerticalPageTabViewStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/verticalpagetabviewstyle
source_url: 'https://developer.apple.com/documentation/swiftui/verticalpagetabviewstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/verticalpagetabviewstyle.json'
content_hash: 'sha256:5556427352858ca6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# VerticalPageTabViewStyle

<sub>Structure</sub>

A `TabViewStyle` that displays a vertical `TabView` interaction and appearance.

<sub>watchOS</sub>

```swift
nonisolated struct VerticalPageTabViewStyle
```

## Overview

Use [verticalPage](tabviewstyle/verticalpage.md) to construct this style.

To apply this style to a tab view, or to a view that contains tab views, use the [tabViewStyle(_:)](<view/tabviewstyle(__).md>) modifier.

## Relationships

- **Conforms To**: [TabViewStyle](tabviewstyle.md)

## Topics

### Creating the tab view style

- [init()](<verticalpagetabviewstyle/init().md>)
- [init(transitionStyle:)](<verticalpagetabviewstyle/init(transitionstyle_).md>) — Creates a new `VerticalPageTabViewStyle` with a transition style.
- [TransitionStyle](verticalpagetabviewstyle/transitionstyle.md) — A transition style used between tabs.

## See Also

### Supporting types

- [DefaultTabViewStyle](defaulttabviewstyle.md) — The default tab view style.
- [SidebarAdaptableTabViewStyle](sidebaradaptabletabviewstyle.md) — A tab bar style that adapts to each platform.
- [TabBarOnlyTabViewStyle](tabbaronlytabviewstyle.md) — A tab view style that displays a tab bar when possible.
- [GroupedTabViewStyle](groupedtabviewstyle.md) — A tab view style that displays a tab bar that groups its tabs together.
- [PageTabViewStyle](pagetabviewstyle.md) — A `TabViewStyle` that displays a paged scrolling `TabView`.
- [CarouselTabViewStyle](carouseltabviewstyle.md) — A style that implements the carousel interaction and appearance. _(deprecated)_
