---
title: 'tabViewCustomization(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/tabviewcustomization(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/tabviewcustomization(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/tabviewcustomization%28_%3A%29.json'
content_hash: 'sha256:578afebd70e1d0dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# tabViewCustomization(_:)

<sub>Instance Method</sub>

Specifies the customizations to apply to the sidebar representation of the tab view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func tabViewCustomization(_ customization: Binding<TabViewCustomization>?) -> some View

```

## Parameters

- `customization` — The customization object to store user customization in.

## Discussion

Only the [sidebarAdaptable](../tabviewstyle/sidebaradaptable.md) style supports supports customization. Specifying a non-nil [TabViewCustomization](../tabviewcustomization.md) object using this modifier enables customization.

By default, if a person hasn’t made customizations, tabs appear according to the default builder visibilities and sections appear in the order you declare in the tab view’s tab builder.

You can change the default visibility by using the [defaultVisibility(_:for:)](<../tabcontent/defaultvisibility(__for_).md>) with a [sidebar](../adaptabletabbarplacement/sidebar.md) placement.

You can change the default section order by changing the order in the builder. If there’s an existing persisted customization, reset the order by calling [resetTabOrder()](<../tabviewcustomization/sectioncustomization/resettaborder().md>) when you change the order.

All tabs and tab sections that support customization need to have a customization ID. You can mark a tab as being non-customizable by specifying a [disabled](../tabcustomizationbehavior/disabled.md) behavior in all adaptable tab bar placements using [customizationBehavior(_:for:)](<../tabcontent/customizationbehavior(__for_).md>).

On macOS, a default interaction is provided for reordering sections but not for controlling the visibility of individual tabs. A custom experience should be provided if desired by setting the visibility of the tab on the customization.

The following code example uses `@AppStorage` to automatically persist any visibility or section order customizations a person makes.

```swift
@AppStorage
private var customization: TabViewCustomization

TabView {
    Tab("Home", systemImage: "house") {
        MyHomeView()
    }
    .customizationID("com.myApp.home")

    Tab("Reports", systemImage: "chart.bar") {
        MyReportsView()
    }
    .customizationID("com.myApp.reports")

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
    .customizationID("com.myApp.browse")
}
.tabViewStyle(.sidebarAdaptable)
.tabViewCustomization($customization)
```

## See Also

### Enabling tab customization

- [TabViewCustomization](../tabviewcustomization.md) — The customizations a person makes to an adaptable sidebar tab view.
- [TabCustomizationBehavior](../tabcustomizationbehavior.md) — The customization behavior of customizable tab view content.
