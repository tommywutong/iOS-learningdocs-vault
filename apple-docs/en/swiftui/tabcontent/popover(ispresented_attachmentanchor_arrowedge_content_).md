---
title: 'popover(isPresented:attachmentAnchor:arrowEdge:content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tabcontent/popover(ispresented:attachmentanchor:arrowedge:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabcontent/popover(ispresented:attachmentanchor:arrowedge:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabcontent/popover%28ispresented%3Aattachmentanchor%3Aarrowedge%3Acontent%3A%29.json'
content_hash: 'sha256:8ed7fbf4b30da37a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabContent](../tabcontent.md)

# popover(isPresented:attachmentAnchor:arrowEdge:content:)

<sub>Instance Method</sub>

Presents a popover when a given condition is true.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds), arrowEdge: Edge? = nil, @ContentBuilder content: @escaping () -> Content) -> some TabContent<Self.TabValue> where Content : View

```

## Parameters

- `isPresented` — A binding to a Boolean value that determines whether to present the popover content that you return from the modifier’s `content` closure.

- `attachmentAnchor` — The positioning anchor that defines the attachment point of the popover. The default is [bounds](../anchor/source/bounds.md).

- `arrowEdge` — The edge of the `attachmentAnchor` that defines the location of the popover’s arrow in macOS. The default is [Edge.top](../edge/top.md).

- `content` — A closure returning the content of the popover.

## Discussion

Use this method to show a popover whose contents are a SwiftUI view that you provide when a bound Boolean variable is `true`. In the example below, a popover displays whenever the user toggles the `isShowingPopover` state variable by pressing the “Show Popover” button:

```swift
struct PopoverExample: View {
    @State private var isShowingPopover = false

    var body: some View {
        TabView {
            Tab("Popover Anchor", systemImage: "arrow.down") {
                Button("Show Popover") {
                    self.isShowingPopover = true
                }
            }
            .popover(isPresented: $isShowingPopover) {
                Text("Popover Content")
                    .padding()
            }
        }
    }
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
- [popover(item:attachmentAnchor:arrowEdge:content:)](<popover(item_attachmentanchor_arrowedge_content_).md>) — Presents a popover using the given item as a data source for the popover’s content.
- [sectionActions(content:)](<sectionactions(content_).md>) — Adds custom actions to a tab section.
- [springLoadingBehavior(_:)](<springloadingbehavior(__).md>) — Sets the spring loading behavior for the tab.
