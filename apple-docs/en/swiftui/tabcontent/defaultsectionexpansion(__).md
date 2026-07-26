---
title: 'defaultSectionExpansion(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/tabcontent/defaultsectionexpansion(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabcontent/defaultsectionexpansion(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabcontent/defaultsectionexpansion%28_%3A%29.json'
content_hash: 'sha256:626b16bc13b25d23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabContent](../tabcontent.md)

# defaultSectionExpansion(_:)

<sub>Instance Method</sub>

Sets the default expansion state for the section containing this tab when displayed in the sidebar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func defaultSectionExpansion(_ expansion: TabSectionExpansion) -> some TabContent<Self.TabValue>

```

## Parameters

- `expansion` — The default expansion behavior for the containing section. The default is [automatic](../tabsectionexpansion/automatic.md).

## Discussion

Use this modifier to control whether a tab section starts expanded or collapsed in the sidebar. The user can manually change the expansion state, and subsequent user interactions take precedence over this default.

This modifier has no effect in contexts where sections are not collapsible — for example, on platforms that do not present a collapsible sidebar, or when [automatic](../tabsectionexpansion/automatic.md) is supplied.

```swift
TabView {
    TabSection("Library") {
        Tab("Songs", systemImage: "music.note") {
            SongsView()
        }
        Tab("Albums", systemImage: "square.stack") {
            AlbumsView()
        }
    }

    TabSection("Archive") {
        Tab("Old Playlists", systemImage: "archivebox") {
            ArchiveView()
        }
        Tab("Deleted", systemImage: "trash") {
            DeletedView()
        }
    }
    .defaultSectionExpansion(.collapsed)
}
.tabViewStyle(.sidebarAdaptable)
```

## See Also

### Configuring tab content

- [badge(_:)](<badge(__).md>) — Generates a badge for the tab from a localized string resource.
- [contextMenu(menuItems:)](<contextmenu(menuitems_).md>) — Adds a context menu to a tab.
- [customizationBehavior(_:for:)](<customizationbehavior(__for_).md>) — Configures the customization behavior of customizable tab view content.
- [customizationID(_:)](<customizationid(__).md>) — Sets the identifier for a tab to persist its state.
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
