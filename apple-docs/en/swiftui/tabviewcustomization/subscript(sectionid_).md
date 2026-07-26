---
title: 'subscript(sectionID:)'
framework: SwiftUI
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 18.0+（27.0 起废弃）, iPadOS 18.0+（27.0 起废弃）, Mac Catalyst 18.0+（27.0 起废弃）, macOS 15.0+（27.0 起废弃）, visionOS 2.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/tabviewcustomization/subscript(sectionid:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabviewcustomization/subscript(sectionid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabviewcustomization/subscript%28sectionid%3A%29.json'
content_hash: 'sha256:8b2f79ae460f5a0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabViewCustomization](../tabviewcustomization.md)

# subscript(sectionID:)

<sub>Instance Subscript</sub>

The customization for a section’s children, identified by the section’s customization identifier.

> [!warning] Deprecated
> Use the `section` subscript and read `tabOrder` instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
subscript(sectionID id: String) -> [String]? { get }
```

## Overview

Section order can be read by subscripting with the tab section’s id:

```swift
let order = customization[sectionID: "com.myApp.categories"]
```

Identifiers can be associated with a `Tab` or `TabSection` using the `customizationID(_:)` modifier.

```swift
TabSection("Categories") {
    Tab("Climate", systemImage: "fan") {
        ClimateView()
    }
    .customizationID("com.myApp.climate")

    Tab("Lights", systemImage: "lightbulb") {
        LightsView()
    }
    .customizationID("com.myApp.lights")
}
.customizationID("com.myApp.categories")
```

If the ID isn’t associated with a section or the section has not been customized, a default value of `nil` is returned.
