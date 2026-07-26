---
title: 'tabViewSidebarFooter(content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 27.0+ beta, visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/tabviewsidebarfooter(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/tabviewsidebarfooter(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/tabviewsidebarfooter%28content%3A%29.json'
content_hash: 'sha256:6970ef618d23360e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# tabViewSidebarFooter(content:)

<sub>Instance Method</sub>

Adds a custom footer to the sidebar of a tab view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated func tabViewSidebarFooter<Content>(@ContentBuilder content: () -> Content) -> some View where Content : View

```

## Discussion

The footer appears at the bottom of the sidebar after any tab labels and can scroll with the content. The footer is only visible when the [TabView](../tabview.md) is displaying the sidebar.

The following example adds a link to contact support to the bottom of the sidebar content:

```swift
TabView {
    Tab("Home", systemImage: "house") {
        HomeView()
    }

    Tab("Alerts", systemImage: "bell") {
        AlertsView()
    }

    Tab("Browse", systemImage: "list.bullet") {
        MyBrowseView()
    }
}
.tabViewStyle(.sidebarAdaptable)
.tabViewSidebarFooter {
    ContactSupportLink()
}
```

## See Also

### Configuring a tab bar

- [defaultAdaptableTabBarPlacement(_:)](<defaultadaptabletabbarplacement(__).md>) — Specifies the default placement for the tabs in a tab view using the adaptable sidebar style.
- [defaultTabBarPlacement(_:)](<defaulttabbarplacement(__).md>) — Specifies the preferred placement for the tabs of a [TabView](../tabview.md) in the [sidebarAdaptable](../tabviewstyle/sidebaradaptable.md) style on platforms where the tab bar cannot adapt between different representations, and only one representation can be shown. _(beta)_
- [tabViewSidebarHeader(content:)](<tabviewsidebarheader(content_).md>) — Adds a custom header to the sidebar of a tab view.
- [tabViewSidebarBottomBar(content:)](<tabviewsidebarbottombar(content_).md>) — Adds a custom bottom bar to the sidebar of a tab view.
- [AdaptableTabBarPlacement](../adaptabletabbarplacement.md) — A placement for tabs in a tab view using the adaptable sidebar style.
- [tabBarPlacement](../environmentvalues/tabbarplacement.md) — The current placement of the tab bar.
- [TabBarPlacement](../tabbarplacement.md) — A placement for tabs in a tab view.
- [isTabBarShowingSections](../environmentvalues/istabbarshowingsections.md) — A Boolean value that determines whether a tab view shows the expanded contents of a tab section.
- [tabBarMinimizeBehavior(_:)](<tabbarminimizebehavior(__).md>) — Sets the behavior for tab bar minimization.
- [TabBarMinimizeBehavior](../tabbarminimizebehavior.md)
- [TabViewBottomAccessoryPlacement](../tabviewbottomaccessoryplacement.md) — A placement of the bottom accessory in a tab view. You can use this to adjust the content of the accessory view based on the placement.
