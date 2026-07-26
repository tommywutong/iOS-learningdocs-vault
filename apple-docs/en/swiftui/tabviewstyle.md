---
title: TabViewStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tabviewstyle
source_url: 'https://developer.apple.com/documentation/swiftui/tabviewstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabviewstyle.json'
content_hash: 'sha256:919e7ce9c651e134'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TabViewStyle

<sub>Protocol</sub>

A specification for the appearance and interaction of a tab view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol TabViewStyle
```

## Overview

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Relationships

- **Conforming Types**: [CarouselTabViewStyle](carouseltabviewstyle.md), [DefaultTabViewStyle](defaulttabviewstyle.md), [GroupedTabViewStyle](groupedtabviewstyle.md), [PageTabViewStyle](pagetabviewstyle.md), [SidebarAdaptableTabViewStyle](sidebaradaptabletabviewstyle.md), [TabBarOnlyTabViewStyle](tabbaronlytabviewstyle.md), [VerticalPageTabViewStyle](verticalpagetabviewstyle.md)

## Topics

### Getting built-in tab view styles

- [automatic](tabviewstyle/automatic.md) — The default tab view style.
- [sidebarAdaptable](tabviewstyle/sidebaradaptable.md) — A tab bar style that adapts to each platform.
- [tabBarOnly](tabviewstyle/tabbaronly.md) — A tab view style that displays a tab bar when possible.
- [grouped](tabviewstyle/grouped.md) — A tab view style that displays a tab bar that groups its tabs together.
- [page](tabviewstyle/page.md) — A `TabViewStyle` that displays a paged scrolling `TabView`.
- [page(indexDisplayMode:)](<tabviewstyle/page(indexdisplaymode_).md>) — A `TabViewStyle` that implements a paged scrolling `TabView` with an index display mode.
- [verticalPage](tabviewstyle/verticalpage.md) — A `TabViewStyle` that displays a vertical page `TabView` interaction and appearance.
- [verticalPage(transitionStyle:)](<tabviewstyle/verticalpage(transitionstyle_).md>) — A `TabViewStyle` that implements the vertical page `TabView` interaction and appearance, and performs the specified transition.
- [carousel](tabviewstyle/carousel.md) — A style that implements the carousel interaction and appearance. _(deprecated)_

### Supporting types

- [DefaultTabViewStyle](defaulttabviewstyle.md) — The default tab view style.
- [SidebarAdaptableTabViewStyle](sidebaradaptabletabviewstyle.md) — A tab bar style that adapts to each platform.
- [TabBarOnlyTabViewStyle](tabbaronlytabviewstyle.md) — A tab view style that displays a tab bar when possible.
- [GroupedTabViewStyle](groupedtabviewstyle.md) — A tab view style that displays a tab bar that groups its tabs together.
- [PageTabViewStyle](pagetabviewstyle.md) — A `TabViewStyle` that displays a paged scrolling `TabView`.
- [VerticalPageTabViewStyle](verticalpagetabviewstyle.md) — A `TabViewStyle` that displays a vertical `TabView` interaction and appearance.
- [CarouselTabViewStyle](carouseltabviewstyle.md) — A style that implements the carousel interaction and appearance. _(deprecated)_

## See Also

### Styling navigation views

- [navigationSplitViewStyle(_:)](<view/navigationsplitviewstyle(__).md>) — Sets the style for navigation split views within this view.
- [NavigationSplitViewStyle](navigationsplitviewstyle.md) — A type that specifies the appearance and interaction of navigation split views within a view hierarchy.
- [tabViewStyle(_:)](<view/tabviewstyle(__).md>) — Sets the style for the tab view within the current environment.
