---
title: tabBarOnly
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tabviewstyle/tabbaronly
source_url: 'https://developer.apple.com/documentation/swiftui/tabviewstyle/tabbaronly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabviewstyle/tabbaronly.json'
content_hash: 'sha256:ca757217be03086d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabViewStyle](../tabviewstyle.md)

# tabBarOnly

<sub>Type Property</sub>

A tab view style that displays a tab bar when possible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var tabBarOnly: TabBarOnlyTabViewStyle { get }
```

## Discussion

To apply this style to a tab view, or to a view that contains tab views, use the [tabViewStyle(_:)](<../view/tabviewstyle(__).md>) modifier.

## See Also

### Getting built-in tab view styles

- [automatic](automatic.md) — The default tab view style.
- [sidebarAdaptable](sidebaradaptable.md) — A tab bar style that adapts to each platform.
- [grouped](grouped.md) — A tab view style that displays a tab bar that groups its tabs together.
- [page](page.md) — A `TabViewStyle` that displays a paged scrolling `TabView`.
- [page(indexDisplayMode:)](<page(indexdisplaymode_).md>) — A `TabViewStyle` that implements a paged scrolling `TabView` with an index display mode.
- [verticalPage](verticalpage.md) — A `TabViewStyle` that displays a vertical page `TabView` interaction and appearance.
- [verticalPage(transitionStyle:)](<verticalpage(transitionstyle_).md>) — A `TabViewStyle` that implements the vertical page `TabView` interaction and appearance, and performs the specified transition.
- [carousel](carousel.md) — A style that implements the carousel interaction and appearance. _(deprecated)_
