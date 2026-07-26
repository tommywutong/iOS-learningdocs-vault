---
title: page
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tabviewstyle/page
source_url: 'https://developer.apple.com/documentation/swiftui/tabviewstyle/page'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabviewstyle/page.json'
content_hash: 'sha256:0e1947afcc5284fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabViewStyle](../tabviewstyle.md)

# page

<sub>Type Property</sub>

A `TabViewStyle` that displays a paged scrolling `TabView`.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var page: PageTabViewStyle { get }
```

## Discussion

To apply this style to a tab view, or to a view that contains tab views, use the [tabViewStyle(_:)](<../view/tabviewstyle(__).md>) modifier.

## See Also

### Getting built-in tab view styles

- [automatic](automatic.md) — The default tab view style.
- [sidebarAdaptable](sidebaradaptable.md) — A tab bar style that adapts to each platform.
- [tabBarOnly](tabbaronly.md) — A tab view style that displays a tab bar when possible.
- [grouped](grouped.md) — A tab view style that displays a tab bar that groups its tabs together.
- [page(indexDisplayMode:)](<page(indexdisplaymode_).md>) — A `TabViewStyle` that implements a paged scrolling `TabView` with an index display mode.
- [verticalPage](verticalpage.md) — A `TabViewStyle` that displays a vertical page `TabView` interaction and appearance.
- [verticalPage(transitionStyle:)](<verticalpage(transitionstyle_).md>) — A `TabViewStyle` that implements the vertical page `TabView` interaction and appearance, and performs the specified transition.
- [carousel](carousel.md) — A style that implements the carousel interaction and appearance. _(deprecated)_
