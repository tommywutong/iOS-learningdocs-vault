---
title: 'defaultTabBarPlacement(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/defaulttabbarplacement(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/defaulttabbarplacement(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/defaulttabbarplacement%28_%3A%29.json'
content_hash: 'sha256:2ba4a9f261ce1940'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# defaultTabBarPlacement(_:)

<sub>Instance Method</sub>

Specifies the preferred placement for the tabs of a [TabView](../tabview.md) in the [sidebarAdaptable](../tabviewstyle/sidebaradaptable.md) style on platforms where the tab bar cannot adapt between different representations, and only one representation can be shown.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func defaultTabBarPlacement(_ defaultPlacement: AdaptableTabBarPlacement) -> some View

```

## Discussion

On platforms that support adapting between a sidebar and tab bar (currently iPadOS), use [defaultAdaptableTabBarPlacement(_:)](<defaultadaptabletabbarplacement(__).md>) to configure the adaptable tab bar.

This modifier is effective on platforms where the [sidebarAdaptable](../tabviewstyle/sidebaradaptable.md) style statically resolves to either a sidebar or tab bar, such as iPhone, macOS, tvOS, and visionOS. On iPadOS (where the bar is adaptable), this modifier has no effect.

The following example shows a `TabView` that prefers to display a sidebar on platforms where the bar cannot morph:

```swift
TabView {
    Tab("Home", systemImage: "house") {
        HomeView()
    }

    Tab("Favorites", systemImage: "star") {
        FavoritesView()
    }
}
.tabViewStyle(.sidebarAdaptable)
.defaultTabBarPlacement(.sidebar)
```

## See Also

### Configuring a tab bar

- [defaultAdaptableTabBarPlacement(_:)](<defaultadaptabletabbarplacement(__).md>) — Specifies the default placement for the tabs in a tab view using the adaptable sidebar style.
- [tabViewSidebarHeader(content:)](<tabviewsidebarheader(content_).md>) — Adds a custom header to the sidebar of a tab view.
- [tabViewSidebarFooter(content:)](<tabviewsidebarfooter(content_).md>) — Adds a custom footer to the sidebar of a tab view.
- [tabViewSidebarBottomBar(content:)](<tabviewsidebarbottombar(content_).md>) — Adds a custom bottom bar to the sidebar of a tab view.
- [AdaptableTabBarPlacement](../adaptabletabbarplacement.md) — A placement for tabs in a tab view using the adaptable sidebar style.
- [tabBarPlacement](../environmentvalues/tabbarplacement.md) — The current placement of the tab bar.
- [TabBarPlacement](../tabbarplacement.md) — A placement for tabs in a tab view.
- [isTabBarShowingSections](../environmentvalues/istabbarshowingsections.md) — A Boolean value that determines whether a tab view shows the expanded contents of a tab section.
- [tabBarMinimizeBehavior(_:)](<tabbarminimizebehavior(__).md>) — Sets the behavior for tab bar minimization.
- [TabBarMinimizeBehavior](../tabbarminimizebehavior.md)
- [TabViewBottomAccessoryPlacement](../tabviewbottomaccessoryplacement.md) — A placement of the bottom accessory in a tab view. You can use this to adjust the content of the accessory view based on the placement.
