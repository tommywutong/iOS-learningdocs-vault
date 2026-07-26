---
title: sidebarAdaptable
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tabviewstyle/sidebaradaptable
source_url: 'https://developer.apple.com/documentation/swiftui/tabviewstyle/sidebaradaptable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabviewstyle/sidebaradaptable.json'
content_hash: 'sha256:9f4a4c3e71d76104'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabViewStyle](../tabviewstyle.md)

# sidebarAdaptable

<sub>Type Property</sub>

A tab bar style that adapts to each platform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var sidebarAdaptable: SidebarAdaptableTabViewStyle { get }
```

## Discussion

Tab views using the sidebar adaptable style have an appearance that varies depending on the platform:

- iPadOS displays a top tab bar that can adapt into a sidebar.
- iOS displays a bottom tab bar.
- macOS and tvOS always show a sidebar.
- visionOS shows an ornament and also shows a sidebar for secondary tabs within a [TabSection](../tabsection.md).

To apply this style to a tab view, or to a view that contains tab views, use the [tabViewStyle(_:)](<../view/tabviewstyle(__).md>) modifier.

## See Also

### Getting built-in tab view styles

- [automatic](automatic.md) — The default tab view style.
- [tabBarOnly](tabbaronly.md) — A tab view style that displays a tab bar when possible.
- [grouped](grouped.md) — A tab view style that displays a tab bar that groups its tabs together.
- [page](page.md) — A `TabViewStyle` that displays a paged scrolling `TabView`.
- [page(indexDisplayMode:)](<page(indexdisplaymode_).md>) — A `TabViewStyle` that implements a paged scrolling `TabView` with an index display mode.
- [verticalPage](verticalpage.md) — A `TabViewStyle` that displays a vertical page `TabView` interaction and appearance.
- [verticalPage(transitionStyle:)](<verticalpage(transitionstyle_).md>) — A `TabViewStyle` that implements the vertical page `TabView` interaction and appearance, and performs the specified transition.
- [carousel](carousel.md) — A style that implements the carousel interaction and appearance. _(deprecated)_
