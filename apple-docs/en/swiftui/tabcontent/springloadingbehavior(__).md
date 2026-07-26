---
title: 'springLoadingBehavior(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tabcontent/springloadingbehavior(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabcontent/springloadingbehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabcontent/springloadingbehavior%28_%3A%29.json'
content_hash: 'sha256:036e2767ece7fed6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabContent](../tabcontent.md)

# springLoadingBehavior(_:)

<sub>Instance Method</sub>

Sets the spring loading behavior for the tab.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func springLoadingBehavior(_ behavior: SpringLoadingBehavior) -> some TabContent<Self.TabValue>

```

## Parameters

- `behavior` — Whether spring loading is enabled or not. If unspecified, the default behavior is `.automatic.`

## Discussion

Spring loading refers to a view being activated during a drag and drop interaction. On iOS this can occur when pausing briefly on top of a view with dragged content. On macOS this can occur with similar brief pauses or on pressure-sensitive systems by “force clicking” during the drag. This has no effect on tvOS or watchOS.

This is commonly used with views that have a navigation or presentation effect, allowing the destination to be revealed without pausing the drag interaction. For example, a button that reveals a list of folders that a dragged item can be dropped onto.

Unlike `disabled(_:)`, this modifier overrides the value set by an ancestor view rather than being unioned with it. For example, the tab below would allow spring loading:

```swift
TabView {
    Tab("Favorites", systemImage: "star") {
        MyFavoritesView()
    }
    .springLoadingBehavior(.enabled)

    ...
}
.springLoadingBehavior(.disabled)
```

## See Also

### Configuring tab content

- [badge(_:)](<badge(__).md>) — Generates a badge for the tab from a localized string resource.
- [contextMenu(menuItems:)](<contextmenu(menuitems_).md>) — Adds a context menu to a tab.
- [customizationBehavior(_:for:)](<customizationbehavior(__for_).md>) — Configures the customization behavior of customizable tab view content.
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
