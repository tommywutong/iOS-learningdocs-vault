---
title: sidebarVisibility
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.4+, iPadOS 18.4+, Mac Catalyst 18.4+, macOS 15.4+, visionOS 2.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tabviewcustomization/tabcustomization/sidebarvisibility
source_url: 'https://developer.apple.com/documentation/swiftui/tabviewcustomization/tabcustomization/sidebarvisibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabviewcustomization/tabcustomization/sidebarvisibility.json'
content_hash: 'sha256:36d5e40e9f8d5d82'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [TabViewCustomization](../../tabviewcustomization.md) · [TabCustomization](../tabcustomization.md)

# sidebarVisibility

<sub>Instance Property</sub>

The visibility of the tab in the sidebar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var sidebarVisibility: Visibility { get set }
```

## Discussion

Visibility can be set imperatively by subscripting with the tab’s id:

```swift
customization[tab: "com.myApp.alerts"].sidebarVisibility = .hidden
```

You can change the default visibility by using `TabContent/defaultVisibility(_:for)` with a `AdaptableTabBarPlacement.sidebar` placement.

```swift
Tab("Alerts", systemImage: "bell", value: .alerts) {
    AlertsView()
}
.customizationID("com.myApp.alerts")
.defaultVisibility(.hidden, for: .sidebar)
```

If the ID isn’t associated with a tab or the tab has not been customized, a default value of `.automatic` is returned.
