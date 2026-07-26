---
title: 'contentToolbar(for:content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.4+, iPadOS 18.4+, Mac Catalyst 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/contenttoolbar(for:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/contenttoolbar(for:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/contenttoolbar%28for%3Acontent%3A%29.json'
content_hash: 'sha256:6e39c681f17720d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# contentToolbar(for:content:)

<sub>Instance Method</sub>

Populates the toolbar of the specified content view type with the views you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func contentToolbar<Content>(for placement: ContentToolbarPlacement, @ContentBuilder content: () -> Content) -> some View where Content : View

```

## Parameters

- `content` — The views representing the content of the toolbar.

## Discussion

Use this modifier to add toolbar content that remains consistent regardless of the content view.

Unlike the toolbar modifier, which configures the toolbar of the modified view’s container, the `contentToolbar` modifier configures the toolbar within the modified view’s content instead. This means that the `contentToolbar` modifier should generally be applied directly to a container view, instead of to the content within a container view. For example, to configure the toolbar of tab view’s sidebar, apply the `contentToolbar` modifier to the `TabView` itself, not to any of the tabs within the `TabView`.

The example below adds a button to the tab view sidebar.

```swift
TabView {
    Tab("Home", systemImage: "house") {
        HomeView()
    }

    Tab("Alerts", systemImage: "bell") {
        AlertsView()
    }

    TabSection("Categories") {
        Tab("Climate", systemImage: "fan") {
            ClimateView()
        }

        Tab("Lights", systemImage: "lightbulb") {
            LightsView()
        }
    }
}
.tabViewStyle(.sidebarAdaptable)
.contentToolbar(for: .tabViewSidebar) {
    DisconnectDevicesButton()
}
```

## See Also

### Toolbars

- [toolbar(content:)](<toolbar(content_).md>) — Populates the toolbar or navigation bar with the specified items.
- [toolbar(id:content:)](<toolbar(id_content_).md>) — Populates the toolbar or navigation bar with the specified items, allowing for user customization.
- [toolbar(_:for:)](<toolbar(__for_).md>) — Specifies the visibility of a bar managed by SwiftUI.
- [toolbar(removing:)](<toolbar(removing_).md>) — Remove a toolbar item present by default
- [toolbarVisibility(_:for:)](<toolbarvisibility(__for_).md>) — Specifies the visibility of a bar managed by SwiftUI.
- [toolbarBackground(_:for:)](<toolbarbackground(__for_).md>) — Specifies the preferred shape style of the background of a bar managed by SwiftUI.
- [toolbarBackgroundVisibility(_:for:)](<toolbarbackgroundvisibility(__for_).md>) — Specifies the preferred visibility of backgrounds on a bar managed by SwiftUI.
- [toolbarItemHidden(_:)](<toolbaritemhidden(__).md>) — Hides an individual view within a control group toolbar item.
- [toolbarForegroundStyle(_:for:)](<toolbarforegroundstyle(__for_).md>) — Specifies the preferred foreground style of bars managed by SwiftUI.
- [toolbarColorScheme(_:for:)](<toolbarcolorscheme(__for_).md>) — Specifies the preferred color scheme of a bar managed by SwiftUI.
- [toolbarOverflowMenu(content:)](<toolbaroverflowmenu(content_).md>) — Configures the overflow menu of a toolbar. _(beta)_
- [toolbarRole(_:)](<toolbarrole(__).md>) — Configures the semantic role for the content populating the toolbar.
- [toolbarMinimizationBehavior(_:for:)](<toolbarminimizationbehavior(__for_).md>) — Sets the minimize behavior for the specified bars. _(beta)_
- [toolbarMinimizationRestoration(_:for:)](<toolbarminimizationrestoration(__for_).md>) — Sets the restoration behavior for the specified bars during minimization. _(beta)_
- [toolbarMinimizationSafeAreaAdjustment(_:for:)](<toolbarminimizationsafeareaadjustment(__for_).md>) — Sets the safe area adjustment for the specified bars during minimization. _(beta)_
