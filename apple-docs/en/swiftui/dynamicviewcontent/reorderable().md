---
title: reorderable()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/dynamicviewcontent/reorderable()
source_url: 'https://developer.apple.com/documentation/swiftui/dynamicviewcontent/reorderable()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dynamicviewcontent/reorderable%28%29.json'
content_hash: 'sha256:4407b70c94730927'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DynamicViewContent](../dynamicviewcontent.md)

# reorderable()

<sub>Instance Method</sub>

Enables reordering of views from this content inside the scope of a reorderable container modifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated func reorderable() -> some DynamicViewContent<Self.Data>

```

## Discussion

Declare this modifier on [DynamicViewContent](../dynamicviewcontent.md) within a reorderable container to allow people to reorder the items in the content using a system drag gesture. A reorderable container is a list, stack, grid, or custom layout that you define with the [reorderContainer(for:in:isEnabled:move:)](<../view/reordercontainer(for_in_isenabled_move_).md>) modifier.

Use this modifier when you have a single collection in the container. If your container has multiple collections, use `DynamicViewContent/reorderable(collectionid:)` instead.

The following example shows a list of landmark views that a person can move to reorder inside the [VStack](../vstack.md):

```swift
struct ContentView: View {
    @State private var landmarks: [Landmark] = []

    var body: some View {
        VStack {
            ForEach(landmarks) { landmark in
                LandmarkView(landmark)
            }
            .reorderable()
        }
        .reorderContainer(for: Landmark.self) { difference in
            apply(difference: difference)
        }
    }
}
```

## See Also

### Reordering items

- [Making a card game with drag, drop, and reordering in SwiftUI](../making-a-card-game-with-drag-drop-and-reordering-in-swiftui.md) — Move cards between positions in a card game using drag, drop, and reordering modifiers.
- [reorderable(collectionID:)](<reorderable(collectionid_).md>) — Enables reordering views from this content within and between sections in the scope of a reorderable container modifier. _(beta)_
- [ReorderableSingleCollectionIdentifier](../reorderablesinglecollectionidentifier.md) — An opaque, empty type used to identify reorderable containers and modifiers with only a single collection. _(beta)_
- [reorderContainer(for:isEnabled:move:)](<../view/reordercontainer(for_isenabled_move_).md>) — Defines a container of reorderable views. _(beta)_
- [reorderContainer(for:in:isEnabled:move:)](<../view/reordercontainer(for_in_isenabled_move_).md>) — Defines a container of reorderable views, with a type you specify to identify sections. _(beta)_
- [reorderContainer(for:itemID:isEnabled:move:)](<../view/reordercontainer(for_itemid_isenabled_move_).md>) — Defines a container of reorderable views, with a type and keypath you specify to identify items. _(beta)_
- [reorderContainer(for:itemID:in:isEnabled:move:)](<../view/reordercontainer(for_itemid_in_isenabled_move_).md>) — Defines a container of reorderable views, with a type and keypath you use to identify items and a type you use to identify collections. _(beta)_
- [reorderDestination(for:in:)](<../dropsession/reorderdestination(for_in_).md>) — Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier. _(beta)_
- [reorderDestination(for:itemID:in:)](<../dropsession/reorderdestination(for_itemid_in_).md>) — Provides the destination value of a reordering operation that occurred in the container associated with this drop destination modifier. _(beta)_
- [ReorderDifference](../reorderdifference.md) — The difference that a reordering operation produces. _(beta)_
