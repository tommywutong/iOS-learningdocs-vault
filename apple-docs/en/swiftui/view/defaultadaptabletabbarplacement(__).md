---
title: 'defaultAdaptableTabBarPlacement(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/defaultadaptabletabbarplacement(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/defaultadaptabletabbarplacement(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/defaultadaptabletabbarplacement%28_%3A%29.json'
content_hash: 'sha256:dce0544fbdc12c94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# defaultAdaptableTabBarPlacement(_:)

<sub>Instance Method</sub>

Specifies the default placement for the tabs in a tab view using the adaptable sidebar style.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
nonisolated func defaultAdaptableTabBarPlacement(_ defaultPlacement: AdaptableTabBarPlacement = .automatic) -> some View

```

## Parameters

- `defaultPlacement` — The default arrangement for the tab view.

## Discussion

This modifier is only effective on iPadOS in the [sidebarAdaptable](../tabviewstyle/sidebaradaptable.md) style. In any other configuration, the system ignores it.

The following example shows a [TabView](../tabview.md) with three tabs, where the tab view displays the sidebar representation when the app initially launches.

```swift
TabView(selection: $selection) {
    Tab("Home", systemImage: "house", value: MyTab.home) {
        MyHomeView()
    }

    Tab("Downloads", systemImage: "square.and.arrow.down.fill",
        value: MyTab.downloads
    ) {
        MyDownloadsView()
    }

    Tab("Browse", systemImage: "list.bullet", value: MyTab.browse) {
        MyBrowseView()
    }
}
.tabViewStyle(.sidebarAdaptable)
.defaultAdaptableTabBarPlacement(.sidebar)
```

## See Also

### Configuring a tab bar

- [defaultTabBarPlacement(_:)](<defaulttabbarplacement(__).md>) — Specifies the preferred placement for the tabs of a [TabView](../tabview.md) in the [sidebarAdaptable](../tabviewstyle/sidebaradaptable.md) style on platforms where the tab bar cannot adapt between different representations, and only one representation can be shown. _(beta)_
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
