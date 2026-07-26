---
title: 'dropDestination(for:action:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tabcontent/dropdestination(for:action:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tabcontent/dropdestination(for:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabcontent/dropdestination%28for%3Aaction%3A%29.json'
content_hash: 'sha256:ceec6069e19675c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabContent](../tabcontent.md)

# dropDestination(for:action:)

<sub>Instance Method</sub>

Defines the destination of a drag and drop operation that handles the dropped content with a closure that you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency func dropDestination<T>(for payloadType: T.Type = T.self, action: @escaping ([T]) -> Void) -> some TabContent<Self.TabValue> where T : Transferable

```

## Parameters

- `payloadType` — Type of the models that are dropped.

- `action` — A closure that takes the dropped content and responds appropriately. The closure takes one argument, which is an array of Transferable items that represents the data to insert.

## Return Value

A view that calls `action` when elements are dropped onto the tab.

## Discussion

The dropped content can be provided as binary data, file URLs, or file promises.

The drop destination is the tab content.

This example adds a profile to a group when the user drops it onto onto that group.

```swift
struct Profile: Identifiable {
    let givenName: String
    let familyName: String
    let image = "person.fill"
    let id = UUID().uuidString
}

@State private var profiles = [
    Profile(givenName: "Juan", familyName: "Chavez"),
    Profile(givenName: "Mei", familyName: "Chen"),
    Profile(givenName: "Tom", familyName: "Clark"),
    Profile(givenName: "Gita", familyName: "Kumar")
]

@State private var favoriteProfiles: [Profile] = []

var body: some View {
    TabView {
        Tab("All Profiles", systemImage: "list.bullet") {
            List(profiles) { profile in
                Text(profile.givenName)
                    .draggable(profile.id)
            }
        }

        Tab("Favorites", systemImage: "star.fill") {
            ForEach(favoritedProfiles) { profile in
                Tab(profile.givenName, image: profile.image) {
                    Label(profile.givenName, systemImage: "star.fill")
                }
            }
        }
        .dropDestination(for: String.self) { receivedIds in
             // Add profiles with `receivedIds` to favorites
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
- [help(_:)](<help(__).md>) — Adds help text to a tab using a text view that you provide. _(beta)_
- [hidden(_:)](<hidden(__).md>) — Hides the tab from the user.
- [popover(isPresented:attachmentAnchor:arrowEdge:content:)](<popover(ispresented_attachmentanchor_arrowedge_content_).md>) — Presents a popover when a given condition is true.
- [popover(item:attachmentAnchor:arrowEdge:content:)](<popover(item_attachmentanchor_arrowedge_content_).md>) — Presents a popover using the given item as a data source for the popover’s content.
- [sectionActions(content:)](<sectionactions(content_).md>) — Adds custom actions to a tab section.
- [springLoadingBehavior(_:)](<springloadingbehavior(__).md>) — Sets the spring loading behavior for the tab.
