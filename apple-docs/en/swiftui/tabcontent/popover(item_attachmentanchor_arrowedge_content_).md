---
title: 'popover(item:attachmentAnchor:arrowEdge:content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tabcontent/popover(item:attachmentanchor:arrowedge:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabcontent/popover(item:attachmentanchor:arrowedge:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabcontent/popover%28item%3Aattachmentanchor%3Aarrowedge%3Acontent%3A%29.json'
content_hash: 'sha256:2c160ad4a4e88601'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabContent](../tabcontent.md)

# popover(item:attachmentAnchor:arrowEdge:content:)

<sub>Instance Method</sub>

Presents a popover using the given item as a data source for the popover’s content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds), arrowEdge: Edge? = nil, @ContentBuilder content: @escaping (Item) -> Content) -> some TabContent<Self.TabValue> where Item : Identifiable, Content : View

```

## Parameters

- `item` — A binding to an optional source of truth for the popover. When `item` is non-`nil`, the system passes the contents to the modifier’s closure. You use this content to populate the fields of a popover that you create that the system displays to the user. If `item` changes, the system dismisses the currently presented popover and replaces it with a new popover using the same process.

- `attachmentAnchor` — The positioning anchor that defines the attachment point of the popover. The default is [bounds](../anchor/source/bounds.md).

- `arrowEdge` — The edge of the `attachmentAnchor` that defines the location of the popover’s arrow in macOS. The default is [Edge.top](../edge/top.md).

- `content` — A closure returning the content of the popover.

## Discussion

Use this method when you need to present a popover with content from a custom data source. The example below uses data in the `PopoverModel` structure to populate the view in the `content` closure that the popover displays to the user:

```swift
struct PopoverExample: View {
    @State private var popover: PopoverModel?

    var body: some View {
        TabView {
            Tab("Popover Anchor", systemImage: "arrow.down") {
                Button("Show Popover") {
                    popover = PopoverModel(message: "Custom Message")
                }
            }
            .popover(item: $popover) { detail in
                 Text("\(detail.message)")
                    .padding()
             }
        }
    }
}

struct PopoverModel: Identifiable {
    var id: String { message }
    let message: String
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
- [help(_:)](<help(__).md>) — Adds help text to a tab using a text view that you provide. _(beta)_
- [hidden(_:)](<hidden(__).md>) — Hides the tab from the user.
- [popover(isPresented:attachmentAnchor:arrowEdge:content:)](<popover(ispresented_attachmentanchor_arrowedge_content_).md>) — Presents a popover when a given condition is true.
- [sectionActions(content:)](<sectionactions(content_).md>) — Adds custom actions to a tab section.
- [springLoadingBehavior(_:)](<springloadingbehavior(__).md>) — Sets the spring loading behavior for the tab.
