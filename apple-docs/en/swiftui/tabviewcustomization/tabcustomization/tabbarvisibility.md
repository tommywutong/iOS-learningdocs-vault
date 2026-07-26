---
title: tabBarVisibility
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.4+, iPadOS 18.4+, Mac Catalyst 18.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tabviewcustomization/tabcustomization/tabbarvisibility
source_url: 'https://developer.apple.com/documentation/swiftui/tabviewcustomization/tabcustomization/tabbarvisibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabviewcustomization/tabcustomization/tabbarvisibility.json'
content_hash: 'sha256:d4f1ffb24aaa727d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [TabViewCustomization](../../tabviewcustomization.md) · [TabCustomization](../tabcustomization.md)

# tabBarVisibility

<sub>Instance Property</sub>

The visibility of the tab in the tab bar.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var tabBarVisibility: Visibility { get }
```

## Discussion

You can change the default visibility by using the `TabContent/defaultVisibility(_:for)` with a `AdaptableTabBarPlacement.tabBar` placement.

If the ID isn’t associated with a tab or the tab has not been customized, a default value of `.automatic` is returned.
