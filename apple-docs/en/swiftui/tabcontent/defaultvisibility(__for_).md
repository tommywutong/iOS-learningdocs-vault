---
title: 'defaultVisibility(_:for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tabcontent/defaultvisibility(_:for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabcontent/defaultvisibility(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabcontent/defaultvisibility%28_%3Afor%3A%29.json'
content_hash: 'sha256:a0b865903e237655'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabContent](../tabcontent.md)

# defaultVisibility(_:for:)

<sub>Instance Method</sub>

Configures the default visibility of a tab in customizable contexts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func defaultVisibility(_ visibility: Visibility, for placements: AdaptableTabBarPlacement...) -> some TabContent<Self.TabValue>

```

## Parameters

- `visibility` — The tab’s visibility.

- `placements` — The locations to apply the visibility.

## Discussion

The [sidebarAdaptable](../tabviewstyle/sidebaradaptable.md) style supports customization of the tab bar and sidebar on iPad. To enable customization, attach a [TabViewCustomization](../tabviewcustomization.md) to the [TabView](../tabview.md) using [tabViewCustomization(_:)](<../view/tabviewcustomization(__).md>).

This modifier has no effect on other platforms or on a [TabViewStyle](../tabviewstyle.md) that doesn’t support customization.

> [!note] Note
> Tabs in the sidebar represent all of the of tabs in [TabView](../tabview.md). A tab that’s hidden from the sidebar is also hidden from the top bar.

The following example shows a `TabView` with three tabs, one of which is hidden by default in the sidebar.

```swift
@AppStorage("MyAppTabViewCustomization")
private var customization: TabViewCustomization

TabView(selection: $selection) {
    Tab("Home", systemImage: "house", value: MyTab.home) {
        MyHomeView()
    }
    .customizationID("com.myApp.home")

    Tab("Reports", systemImage: "chart.bar", value: MyTab.reports) {
        MyReportsView()
    }
    .customizationID("com.myApp.reports")

    Tab("Browse", systemImage: "list.bullet", value: MyTab.browse) {
        MyBrowseView()
    }
    .customizationID("com.myApp.browse")
    .defaultVisibility(.hidden, for: .sidebar)
}
.tabViewStyle(.sidebarAdaptable)
.tabViewCustomization($customization)
```

## See Also

### Configuring tab content

- [badge(_:)](<badge(__).md>) — Generates a badge for the tab from a localized string resource.
- [contextMenu(menuItems:)](<contextmenu(menuitems_).md>) — Adds a context menu to a tab.
- [customizationBehavior(_:for:)](<customizationbehavior(__for_).md>) — Configures the customization behavior of customizable tab view content.
- [customizationID(_:)](<customizationid(__).md>) — Sets the identifier for a tab to persist its state.
- [defaultSectionExpansion(_:)](<defaultsectionexpansion(__).md>) — Sets the default expansion state for the section containing this tab when displayed in the sidebar. _(beta)_
- [TabSectionExpansion](../tabsectionexpansion.md) — The default expansion state for a tab section in the sidebar. _(beta)_
- [disabled(_:)](<disabled(__).md>) — Controls whether users can interact with this tab.
- [draggable(_:)](<draggable(__).md>) — Activates this tab as the source of a drag and drop operation. This tab can only be dragged when in the sidebar.
- [dropDestination(for:action:)](<dropdestination(for_action_).md>) — Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [help(_:)](<help(__).md>) — Adds help text to a tab using a text view that you provide. _(beta)_
- [hidden(_:)](<hidden(__).md>) — Hides the tab from the user.
- [popover(isPresented:attachmentAnchor:arrowEdge:content:)](<popover(ispresented_attachmentanchor_arrowedge_content_).md>) — Presents a popover when a given condition is true.
- [popover(item:attachmentAnchor:arrowEdge:content:)](<popover(item_attachmentanchor_arrowedge_content_).md>) — Presents a popover using the given item as a data source for the popover’s content.
- [sectionActions(content:)](<sectionactions(content_).md>) — Adds custom actions to a tab section.
- [springLoadingBehavior(_:)](<springloadingbehavior(__).md>) — Sets the spring loading behavior for the tab.
