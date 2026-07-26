---
title: tabOrder
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.4+, iPadOS 18.4+, Mac Catalyst 18.4+, macOS 15.4+, visionOS 2.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tabviewcustomization/sectioncustomization/taborder
source_url: 'https://developer.apple.com/documentation/swiftui/tabviewcustomization/sectioncustomization/taborder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabviewcustomization/sectioncustomization/taborder.json'
content_hash: 'sha256:68f18449cccab86d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [TabViewCustomization](../../tabviewcustomization.md) · [SectionCustomization](../sectioncustomization.md)

# tabOrder

<sub>Instance Property</sub>

The order customization for the tabs in a section, identified by customization identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var tabOrder: [String]? { get }
```

## Discussion

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

Section tab order can be read by subscripting the customization with the tab section’s id:

```swift
let order = customization[section: "com.myApp.categories"].tabOrder
```

If the section has been customized, this returns the current order for all the tabs in the section, including tabs that have not been customized. If the section has not been customized or the identifier does not correspond to a section, the order will be nil to indicate the tab order matches that of the builder.
