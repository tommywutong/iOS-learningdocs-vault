---
title: 'customizationBehavior(_:for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tabcontent/customizationbehavior(_:for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabcontent/customizationbehavior(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabcontent/customizationbehavior%28_%3Afor%3A%29.json'
content_hash: 'sha256:d21f97a12aeb718a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabContent](../tabcontent.md)

# customizationBehavior(_:for:)

<sub>Instance Method</sub>

Configures the customization behavior of customizable tab view content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func customizationBehavior(_ behavior: TabCustomizationBehavior, for placements: AdaptableTabBarPlacement...) -> some TabContent<Self.TabValue>

```

## Parameters

- `behavior` — The customization behavior of the customizable tab content.

## Discussion

The [sidebarAdaptable](../tabviewstyle/sidebaradaptable.md) style supports customization of the tab bar and sidebar on iPad. To enable customization, attach a [TabViewCustomization](../tabviewcustomization.md) to the [TabView](../tabview.md) using [tabViewCustomization(_:)](<../view/tabviewcustomization(__).md>).

This modifier has no effect on other platforms or on a [TabViewStyle](../tabviewstyle.md) that doesn’t support customization.

Use this modifier to specify the customization behavior a person can perform on items in the specified placement. To enable customization, all tabs need a customization ID.

In the following example, the tabs support all of the different kinds of customizations in both the sidebar and tab bar.

```swift
@AppStorage("MyAppTabViewCustomization")
private var customization: TabViewCustomization

TabView {
    Tab("Home", systemImage: "house") {
        HomeView()
    }
    .customizationID("com.myApp.home")

    Tab("Alerts", systemImage: "bell") {
        AlertsView()
    }
    .customizationID("com.myApp.bell")

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
}
.tabViewStyle(.sidebarAdaptable)
.tabViewCustomization($customization)
```

You can create an item that cannot be hidden or moved by passing a value of [disabled](../tabcustomizationbehavior/disabled.md) to this modifier. Only turn off customization for important tabs that people need for the app to do common functionality. If you turn off customization for both the sidebar and tab bar, then a customization ID isn’t necessary.

```swift
@AppStorage("MyAppTabViewCustomization")
private var customization: TabViewCustomization

TabView {
    Tab("Home", systemImage: "house") {
        HomeView()
    }
    .customizationBehavior(.disabled, for: .sidebar, .tabBar)

    Tab("Alerts", systemImage: "bell") {
        AlertsView()
    }
    .customizationID("com.myApp.bell")

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
}
.tabViewStyle(.sidebarAdaptable)
.tabViewCustomization($customization)
```

Pass a value of [reorderable](../tabcustomizationbehavior/reorderable.md) to create an item that people can move, but can’t hide. In the [sidebar](../adaptabletabbarplacement/sidebar.md), people can only reorder tabs within sections.

```swift
@AppStorage("MyAppTabViewCustomization")
private var customization: TabViewCustomization

TabView {
    Tab("Home", systemImage: "house") {
        HomeView()
    }
    .customizationID("com.myApp.home")

    Tab("Alerts", systemImage: "bell") {
        AlertsView()
    }
    .customizationID("com.myApp.bell")

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
    .customizationBehavior(.reorderable, for: .sidebar)
}
.tabViewStyle(.sidebarAdaptable)
.tabViewCustomization($customization)
```

You can individually customize each placement’s behavior. The following example would allow reordering of children in the sidebar but prohibit hiding or moving the tab in the tab bar.

```swift
@AppStorage("MyAppTabViewCustomization")
private var customization: TabViewCustomization

TabView {
    Tab("Home", systemImage: "house") {
        HomeView()
    }
    .customizationID("com.myApp.home")

    Tab("Alerts", systemImage: "bell") {
        AlertsView()
    }
    .customizationID("com.myApp.bell")

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
    .customizationBehavior(.reorderable, for: .sidebar)
    .customizationBehavior(.disabled, for: .tabBar)
}
.tabViewStyle(.sidebarAdaptable)
.tabViewCustomization($customization)
```

## See Also

### Configuring tab content

- [badge(_:)](<badge(__).md>) — Generates a badge for the tab from a localized string resource.
- [contextMenu(menuItems:)](<contextmenu(menuitems_).md>) — Adds a context menu to a tab.
- [customizationID(_:)](<customizationid(__).md>) — Sets the identifier for a tab to persist its state.
- [defaultSectionExpansion(_:)](<defaultsectionexpansion(__).md>) — Sets the default expansion state for the section containing this tab when displayed in the sidebar. _(beta)_
- [TabSectionExpansion](../tabsectionexpansion.md) — The default expansion state for a tab section in the sidebar. _(beta)_
- [defaultVisibility(_:for:)](<defaultvisibility(__for_).md>) — Configures the default visibility of a tab in customizable contexts.
- [disabled(_:)](<disabled(__).md>) — Controls whether users can interact with this tab.
- [draggable(_:)](<draggable(__).md>) — Activates this tab as the source of a drag and drop operation. This tab can only be dragged when in the sidebar.
- [dropDestination(for:action:)](<dropdestination(for_action_).md>) — Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [help(_:)](<help(__).md>) — Adds help text to a tab using a text view that you provide. _(beta)_
- [hidden(_:)](<hidden(__).md>) — Hides the tab from the user.
- [popover(isPresented:attachmentAnchor:arrowEdge:content:)](<popover(ispresented_attachmentanchor_arrowedge_content_).md>) — Presents a popover when a given condition is true.
- [popover(item:attachmentAnchor:arrowEdge:content:)](<popover(item_attachmentanchor_arrowedge_content_).md>) — Presents a popover using the given item as a data source for the popover’s content.
- [sectionActions(content:)](<sectionactions(content_).md>) — Adds custom actions to a tab section.
- [springLoadingBehavior(_:)](<springloadingbehavior(__).md>) — Sets the spring loading behavior for the tab.
