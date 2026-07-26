---
title: carousel
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [watchOS 7.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/tabviewstyle/carousel
source_url: 'https://developer.apple.com/documentation/swiftui/tabviewstyle/carousel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabviewstyle/carousel.json'
content_hash: 'sha256:38922605b2c3367a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabViewStyle](../tabviewstyle.md)

# carousel

<sub>Type Property</sub>

A style that implements the carousel interaction and appearance.

> [!warning] Deprecated
> Use [verticalPage](verticalpage.md) or [verticalPage(transitionStyle:)](<verticalpage(transitionstyle_).md>) instead.

<sub>watchOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var carousel: CarouselTabViewStyle { get }
```

## See Also

### Getting built-in tab view styles

- [automatic](automatic.md) — The default tab view style.
- [sidebarAdaptable](sidebaradaptable.md) — A tab bar style that adapts to each platform.
- [tabBarOnly](tabbaronly.md) — A tab view style that displays a tab bar when possible.
- [grouped](grouped.md) — A tab view style that displays a tab bar that groups its tabs together.
- [page](page.md) — A `TabViewStyle` that displays a paged scrolling `TabView`.
- [page(indexDisplayMode:)](<page(indexdisplaymode_).md>) — A `TabViewStyle` that implements a paged scrolling `TabView` with an index display mode.
- [verticalPage](verticalpage.md) — A `TabViewStyle` that displays a vertical page `TabView` interaction and appearance.
- [verticalPage(transitionStyle:)](<verticalpage(transitionstyle_).md>) — A `TabViewStyle` that implements the vertical page `TabView` interaction and appearance, and performs the specified transition.
