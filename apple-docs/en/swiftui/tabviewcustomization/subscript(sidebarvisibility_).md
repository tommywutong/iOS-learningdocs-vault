---
title: 'subscript(sidebarVisibility:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 18.0+（27.0 起废弃）, iPadOS 18.0+（27.0 起废弃）, Mac Catalyst 18.0+（27.0 起废弃）, macOS 15.0+（27.0 起废弃）, visionOS 2.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/tabviewcustomization/subscript(sidebarvisibility:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabviewcustomization/subscript(sidebarvisibility:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabviewcustomization/subscript%28sidebarvisibility%3A%29.json'
content_hash: 'sha256:7394db9ff35ca2f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabViewCustomization](../tabviewcustomization.md)

# subscript(sidebarVisibility:)

<sub>Instance Subscript</sub>

The visibility of the tab identified by its customization identifier.

> [!warning] Deprecated
> Use the `tab` subscript and read `sidebarVisibility` instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
subscript(sidebarVisibility id: String) -> Visibility { get set }
```

## Overview

Visibility can be set imperatively by subscripting with the tab’s id:

```swift
customization[sidebarVisibility: "com.myApp.alerts"] = .hidden
```

You can change the default visibility by using the [defaultVisibility(_:for:)](<../tabcontent/defaultvisibility(__for_).md>) with a [sidebar](../adaptabletabbarplacement/sidebar.md) placement.

```swift
Tab("Alerts", systemImage: "bell", value: .alerts) {
    AlertsView()
}
.customizationID("com.myApp.alerts")
.defaultVisibility(.hidden, for: .sidebar)
```

If the ID isn’t associated with a tab or the tab has not been customized, a default value of `.automatic` is returned.
