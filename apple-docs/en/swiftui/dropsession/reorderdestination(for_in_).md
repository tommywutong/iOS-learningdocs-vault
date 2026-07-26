---
title: 'reorderDestination(for:in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/dropsession/reorderdestination(for:in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/dropsession/reorderdestination(for:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dropsession/reorderdestination%28for%3Ain%3A%29.json'
content_hash: 'sha256:caba5b16bcb6be6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DropSession](../dropsession.md)

# reorderDestination(for:in:)

<sub>Instance Method</sub>

Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func reorderDestination<Item, CollectionID>(for item: Item.Type, in collectionID: CollectionID.Type = ReorderableSingleCollectionIdentifier.self) -> ReorderDifference<Item.ID, CollectionID>.Destination? where Item : Identifiable
```

## Parameters

- `item` — The type of reorderable items in the container.

- `collectionID` — The identifier type for collections in your container.

## Discussion

Use the `ItemID` and `CollectionID` types of your [reorderContainer(for:in:isEnabled:move:)](<../view/reordercontainer(for_in_isenabled_move_).md>) modifier to look up the destination value.

This value can be `nil`, if the container was unable to determine a placement for the items. This can happen if someone drags items into the destination but does not interact with any of the container items to determine a concrete position. You should still accept these items into the container. The following example demonstrates appending those values to the end of the collection:

```swift
struct ContentView: View {
    @State var contacts: [Contact] = []

    var body: some View {
        VStack {
            ForEach(contacts) { contact in
                ContactView(contact)
            }
            .reorderable()
        }
        .reorderContainer(for: Contact.ID.self) { difference in
            apply(difference: difference)
        }
        .dragContainer(for: Contact.self) { itemID in
            contacts.first { $0.id == itemID }.map { [$0] } ?? []
        }
        .dropDestination(for: Contact.self) { items, session in
            if let destinationIndex = session.reorderDestination(
                for: Contact.ID.self)?.index(in: contacts)
            {
                contacts.insert(
                    contentsOf: items, at: destinationIndex)
            } else {
                contacts.append(contentsOf: items)
            }
        }
    }
}
```

## See Also

### Reordering items

- [Making a card game with drag, drop, and reordering in SwiftUI](../making-a-card-game-with-drag-drop-and-reordering-in-swiftui.md) — Move cards between positions in a card game using drag, drop, and reordering modifiers.
- [reorderable()](<../dynamicviewcontent/reorderable().md>) — Enables reordering of views from this content inside the scope of a reorderable container modifier. _(beta)_
- [reorderable(collectionID:)](<../dynamicviewcontent/reorderable(collectionid_).md>) — Enables reordering views from this content within and between sections in the scope of a reorderable container modifier. _(beta)_
- [ReorderableSingleCollectionIdentifier](../reorderablesinglecollectionidentifier.md) — An opaque, empty type used to identify reorderable containers and modifiers with only a single collection. _(beta)_
- [reorderContainer(for:isEnabled:move:)](<../view/reordercontainer(for_isenabled_move_).md>) — Defines a container of reorderable views. _(beta)_
- [reorderContainer(for:in:isEnabled:move:)](<../view/reordercontainer(for_in_isenabled_move_).md>) — Defines a container of reorderable views, with a type you specify to identify sections. _(beta)_
- [reorderContainer(for:itemID:isEnabled:move:)](<../view/reordercontainer(for_itemid_isenabled_move_).md>) — Defines a container of reorderable views, with a type and keypath you specify to identify items. _(beta)_
- [reorderContainer(for:itemID:in:isEnabled:move:)](<../view/reordercontainer(for_itemid_in_isenabled_move_).md>) — Defines a container of reorderable views, with a type and keypath you use to identify items and a type you use to identify collections. _(beta)_
- [reorderDestination(for:itemID:in:)](<reorderdestination(for_itemid_in_).md>) — Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier. _(beta)_
- [ReorderDifference](../reorderdifference.md) — The difference that a reordering operation produces. _(beta)_
