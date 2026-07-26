---
title: 'tabViewBottomAccessory(content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/tabviewbottomaccessory(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/tabviewbottomaccessory(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/tabviewbottomaccessory%28content%3A%29.json'
content_hash: 'sha256:b998331016a88821'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# tabViewBottomAccessory(content:)

<sub>Instance Method</sub>

Places a view as the bottom accessory of the tab view.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
nonisolated func tabViewBottomAccessory<Content>(@ContentBuilder content: () -> Content) -> some View where Content : View

```

## Discussion

On iPhone, the placement of the bottom accessory depends on the tab bar size: when the tab bar is normal size, the accessory appears above it; when the tab bar is collapsed, the accessory displays inline. Use the [tabViewBottomAccessoryPlacement](../environmentvalues/tabviewbottomaccessoryplacement.md) environment value to adjust the accessory’s content based on its placement.

The following example sets a status view as the `TabView` bottom accessory.

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
.tabViewBottomAccessory {
    HomeStatusView()
}
```

## See Also

### Tab views

- [defaultAdaptableTabBarPlacement(_:)](<defaultadaptabletabbarplacement(__).md>) — Specifies the default placement for the tabs in a tab view using the adaptable sidebar style.
- [defaultTabBarPlacement(_:)](<defaulttabbarplacement(__).md>) — Specifies the preferred placement for the tabs of a [TabView](../tabview.md) in the [sidebarAdaptable](../tabviewstyle/sidebaradaptable.md) style on platforms where the tab bar cannot adapt between different representations, and only one representation can be shown. _(beta)_
- [sectionActions(content:)](<sectionactions(content_).md>) — Adds custom actions to a section.
- [tabBarMinimizeBehavior(_:)](<tabbarminimizebehavior(__).md>) — Sets the behavior for tab bar minimization.
- [tabViewBottomAccessory(isEnabled:content:)](<tabviewbottomaccessory(isenabled_content_).md>) — Places a view as the bottom accessory of the tab view. Use this modifier to dynamically show and hide the accessory view.
- [tabViewCustomization(_:)](<tabviewcustomization(__).md>) — Specifies the customizations to apply to the sidebar representation of the tab view.
- [tabViewSearchActivation(_:)](<tabviewsearchactivation(__).md>) — Configures the activation and deactivation behavior of search in the search tab.
- [tabViewSidebarHeader(content:)](<tabviewsidebarheader(content_).md>) — Adds a custom header to the sidebar of a tab view.
- [tabViewSidebarFooter(content:)](<tabviewsidebarfooter(content_).md>) — Adds a custom footer to the sidebar of a tab view.
- [tabViewSidebarBottomBar(content:)](<tabviewsidebarbottombar(content_).md>) — Adds a custom bottom bar to the sidebar of a tab view.
