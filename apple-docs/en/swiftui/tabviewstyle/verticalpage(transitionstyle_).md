---
title: 'verticalPage(transitionStyle:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tabviewstyle/verticalpage(transitionstyle:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabviewstyle/verticalpage(transitionstyle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabviewstyle/verticalpage%28transitionstyle%3A%29.json'
content_hash: 'sha256:352efb5fa91a68c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabViewStyle](../tabviewstyle.md)

# verticalPage(transitionStyle:)

<sub>Type Method</sub>

A `TabViewStyle` that implements the vertical page `TabView` interaction and appearance, and performs the specified transition.

<sub>watchOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static func verticalPage(transitionStyle: VerticalPageTabViewStyle.TransitionStyle) -> VerticalPageTabViewStyle
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
- [carousel](carousel.md) — A style that implements the carousel interaction and appearance. _(deprecated)_
