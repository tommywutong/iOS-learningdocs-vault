---
title: 'help(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/tabcontent/help(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabcontent/help(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabcontent/help%28_%3A%29.json'
content_hash: 'sha256:2664f4cb01403276'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabContent](../tabcontent.md)

# help(_:)

<sub>Instance Method</sub>

Adds help text to a tab using a text view that you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func help(_ text: Text) -> some TabContent<Self.TabValue>

```

## Parameters

- `text` — The [Text](../text.md) view to use as help.

## Discussion

Adding help to a tab configures the tab’s accessibility hint and its help tag (also called a _tooltip_) in macOS or visionOS. For more information on using help tags, see [Offering help](../../design/human-interface-guidelines/offering-help.md) in the Human Interface Guidelines.

```swift
TabView {
    Tab("List", systemImage: "list.dash") {
        ListView()
    }
    .help(Text("Display symbols in list format"))
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
- [draggable(_:)](<draggable(__).md>) — Activates this tab as the source of a drag and drop operation. This tab can only be dragged when in the sidebar.
- [dropDestination(for:action:)](<dropdestination(for_action_).md>) — Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.
- [hidden(_:)](<hidden(__).md>) — Hides the tab from the user.
- [popover(isPresented:attachmentAnchor:arrowEdge:content:)](<popover(ispresented_attachmentanchor_arrowedge_content_).md>) — Presents a popover when a given condition is true.
- [popover(item:attachmentAnchor:arrowEdge:content:)](<popover(item_attachmentanchor_arrowedge_content_).md>) — Presents a popover using the given item as a data source for the popover’s content.
- [sectionActions(content:)](<sectionactions(content_).md>) — Adds custom actions to a tab section.
- [springLoadingBehavior(_:)](<springloadingbehavior(__).md>) — Sets the spring loading behavior for the tab.
