---
title: TabViewCustomization
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tabviewcustomization
source_url: 'https://developer.apple.com/documentation/swiftui/tabviewcustomization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabviewcustomization.json'
content_hash: 'sha256:e2ed0b2a2a71258f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TabViewCustomization

<sub>Structure</sub>

The customizations a person makes to an adaptable sidebar tab view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct TabViewCustomization
```

## Overview

By default, if a person hasn’t made customizations, tabs appear according to the default builder visibilities and sections appear in the order you declare in the tab view’s tab builder.

You can change the default visibility by using the [defaultVisibility(_:for:)](<tabcontent/defaultvisibility(__for_).md>) with a [sidebar](adaptabletabbarplacement/sidebar.md) placement.

You can change the default section order by changing the order in the builder. If there’s an existing persisted customization, reset the order by calling [resetTabOrder()](<tabviewcustomization/sectioncustomization/resettaborder().md>) when you change the order.

All tabs and tab sections that support customization need to have a customization ID. You can mark a tab as being non-customizable by specifying a [disabled](tabcustomizationbehavior/disabled.md) behavior in all adaptable tab bar placements using [customizationBehavior(_:for:)](<tabcontent/customizationbehavior(__for_).md>).

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

## Relationships

- **Conforms To**: [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Structures

- [SectionCustomization](tabviewcustomization/sectioncustomization.md) — The customizations a user has made to a [TabSection](tabsection.md).
- [TabCustomization](tabviewcustomization/tabcustomization.md) — The customizations a user has made to a [Tab](tab.md).

### Initializers

- [init()](<tabviewcustomization/init().md>) — Creates an empty tab sidebar customization.

### Instance Methods

- [resetSectionOrder()](<tabviewcustomization/resetsectionorder().md>) — Resets ordering back to the default for all sections, preserving the customized tab visibilities.
- [resetSectionOrder(for:)](<tabviewcustomization/resetsectionorder(for_).md>) — Resets ordering back to the default for the section with `sectionID`, preserving any customized tab visibilities. _(deprecated)_
- [resetVisibility()](<tabviewcustomization/resetvisibility().md>) — Resets all tab sidebar visibilities back to the default, preserving the section customizations.

### Subscripts

- [subscript(section:)](<tabviewcustomization/subscript(section_).md>) — The customization of the section, identified by its customization identifier.
- [subscript(sectionID:)](<tabviewcustomization/subscript(sectionid_).md>) — The customization for a section’s children, identified by the section’s customization identifier. _(deprecated)_
- [subscript(sidebarVisibility:)](<tabviewcustomization/subscript(sidebarvisibility_).md>) — The visibility of the tab identified by its customization identifier. _(deprecated)_
- [subscript(tab:)](<tabviewcustomization/subscript(tab_).md>) — The customization of the tab, identified by its customization identifier.

## See Also

### Enabling tab customization

- [tabViewCustomization(_:)](<view/tabviewcustomization(__).md>) — Specifies the customizations to apply to the sidebar representation of the tab view.
- [TabCustomizationBehavior](tabcustomizationbehavior.md) — The customization behavior of customizable tab view content.
