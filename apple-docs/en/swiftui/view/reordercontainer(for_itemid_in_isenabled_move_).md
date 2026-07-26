---
title: 'reorderContainer(for:itemID:in:isEnabled:move:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/reordercontainer(for:itemid:in:isenabled:move:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/reordercontainer(for:itemid:in:isenabled:move:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/reordercontainer%28for%3Aitemid%3Ain%3Aisenabled%3Amove%3A%29.json'
content_hash: 'sha256:b9b12d007760c629'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# reorderContainer(for:itemID:in:isEnabled:move:)

<sub>Instance Method</sub>

Defines a container of reorderable views, with a type and keypath you use to identify items and a type you use to identify collections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated func reorderContainer<Item, ItemID, CollectionID>(for item: Item.Type, itemID: KeyPath<Item, ItemID>, in collectionID: CollectionID.Type, isEnabled: Bool = true, move: @escaping (ReorderDifference<ItemID, CollectionID>) -> ()) -> some View where ItemID : Hashable, ItemID : Sendable, CollectionID : Hashable, CollectionID : Sendable

```

## Parameters

- `item` — The type of reorderable items in the container.

- `itemID` — A keypath to the identifier used to represent this item.

- `collectionID` — The type used to identify collections of reorderable items in the container.

- `isEnabled` — Whether the container allows reordering.

- `move` — A closure that provides the change at the end of a session.

## Discussion

Declare this modifier on your list, stack, grid, or custom layout to define a reorderable container. Then, apply [reorderable(collectionID:)](<../dynamicviewcontent/reorderable(collectionid_).md>) to the content of your container to make those views reorderable.

Use this overload if your container contains multiple collections and you need to provide the type and keypath you use to identify items. If your container only has a single collection, use the convenience [reorderContainer(for:itemID:isEnabled:move:)](<reordercontainer(for_itemid_isenabled_move_).md>) modifier.

A person can lift a reorderable view within the container using a drag gesture. As they lift the item, the system puts a placeholder view in its place to indicate where the view can drop. As they move the item through the container, the position of the placeholder updates to reflect which view the person drags over. When they drop the view, the system calls the `move` closure and provides the change.

The system provides the change as a difference to the closure. The difference contains the identifiers of items to move, in the order that the person selected them. It also contains a destination value, which indicates where to insert the item or items.

The following example shows a list of reminder views that a person can move to reorder inside and between each [Section](../section.md) in the [List](../list.md):

```swift
struct ContentView: View {
    @State private var model = ReminderModel()

    var body: some View {
        List {
            ForEach(model.sections) { section in
                Section(section.name) {
                    ForEach(
                        section.reminders, id: \.databaseID
                    ) { reminder in
                        ReminderView(reminder)
                    }
                    .reorderable(collectionID: section.id)
                }
            }
        }
        .reorderContainer(
            for: Reminder.self, itemID: \.databaseID,
            in: ReminderModel.Section.ID.self
        ) { difference in
            model.apply(difference: difference)
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
- [reorderContainer(for:isEnabled:move:)](<reordercontainer(for_isenabled_move_).md>) — Defines a container of reorderable views. _(beta)_
- [reorderContainer(for:in:isEnabled:move:)](<reordercontainer(for_in_isenabled_move_).md>) — Defines a container of reorderable views, with a type you specify to identify sections. _(beta)_
- [reorderContainer(for:itemID:isEnabled:move:)](<reordercontainer(for_itemid_isenabled_move_).md>) — Defines a container of reorderable views, with a type and keypath you specify to identify items. _(beta)_
- [reorderDestination(for:in:)](<../dropsession/reorderdestination(for_in_).md>) — Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier. _(beta)_
- [reorderDestination(for:itemID:in:)](<../dropsession/reorderdestination(for_itemid_in_).md>) — Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier. _(beta)_
- [ReorderDifference](../reorderdifference.md) — The difference that a reordering operation produces. _(beta)_
