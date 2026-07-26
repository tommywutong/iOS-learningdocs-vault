---
title: 'draggable(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.1+, iPadOS 18.1+, Mac Catalyst 18.1+, macOS 15.1+, visionOS 2.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tabcontent/draggable(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabcontent/draggable(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabcontent/draggable%28_%3A%29.json'
content_hash: 'sha256:b482289315fb4002'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabContent](../tabcontent.md)

# draggable(_:)

<sub>Instance Method</sub>

Activates this tab as the source of a drag and drop operation. This tab can only be dragged when in the sidebar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func draggable<T>(_ payload: @autoclosure @escaping () -> T) -> some TabContent<Self.TabValue> where T : Transferable

```

## Parameters

- `payload` — A closure that returns a single instance or a value conforming to [Transferable](../../coretransferable/transferable.md) that represents the draggable data from this tab.

## Discussion

Applying the `draggable(_:)` modifier adds the appropriate gestures for drag and drop to this tab. When a drag operation begins, a rendering of the tab is generated and used as the preview image.

The following example allows the ‘Family’ tab to be dragged and dropped.

```swift
TabView {
    Tab("Family", systemImage: "list.bullet") {
        MyFamilyView()
    }
    .draggable(AppSections.family)
}
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
- [dropDestination(for:action:)](<dropdestination(for_action_).md>) — Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [help(_:)](<help(__).md>) — Adds help text to a tab using a text view that you provide. _(beta)_
- [hidden(_:)](<hidden(__).md>) — Hides the tab from the user.
- [popover(isPresented:attachmentAnchor:arrowEdge:content:)](<popover(ispresented_attachmentanchor_arrowedge_content_).md>) — Presents a popover when a given condition is true.
- [popover(item:attachmentAnchor:arrowEdge:content:)](<popover(item_attachmentanchor_arrowedge_content_).md>) — Presents a popover using the given item as a data source for the popover’s content.
- [sectionActions(content:)](<sectionactions(content_).md>) — Adds custom actions to a tab section.
- [springLoadingBehavior(_:)](<springloadingbehavior(__).md>) — Sets the spring loading behavior for the tab.
