---
title: verticalPage
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tabviewstyle/verticalpage
source_url: 'https://developer.apple.com/documentation/swiftui/tabviewstyle/verticalpage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabviewstyle/verticalpage.json'
content_hash: 'sha256:52ec5d4504f742b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabViewStyle](../tabviewstyle.md)

# verticalPage

<sub>Type Property</sub>

A `TabViewStyle` that displays a vertical page `TabView` interaction and appearance.

<sub>watchOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var verticalPage: VerticalPageTabViewStyle { get }
```

## Discussion

To apply this style to a tab view, or to a view that contains tab views, use the [tabViewStyle(_:)](<../view/tabviewstyle(__).md>) modifier.

## See Also

### Getting built-in tab view styles

- [automatic](automatic.md) — The default tab view style.
- [sidebarAdaptable](sidebaradaptable.md) — A tab bar style that adapts to each platform.
- [tabBarOnly](tabbaronly.md) — A tab view style that displays a tab bar when possible.
- [grouped](grouped.md) — A tab view style that displays a tab bar that groups its tabs together.
- [page](page.md) — A `TabViewStyle` that displays a paged scrolling `TabView`.
- [page(indexDisplayMode:)](<page(indexdisplaymode_).md>) — A `TabViewStyle` that implements a paged scrolling `TabView` with an index display mode.
- [verticalPage(transitionStyle:)](<verticalpage(transitionstyle_).md>) — A `TabViewStyle` that implements the vertical page `TabView` interaction and appearance, and performs the specified transition.
- [carousel](carousel.md) — A style that implements the carousel interaction and appearance. _(deprecated)_
