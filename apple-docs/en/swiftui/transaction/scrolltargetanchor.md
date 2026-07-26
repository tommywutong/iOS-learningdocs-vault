---
title: scrollTargetAnchor
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/transaction/scrolltargetanchor
source_url: 'https://developer.apple.com/documentation/swiftui/transaction/scrolltargetanchor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/transaction/scrolltargetanchor.json'
content_hash: 'sha256:89c208629ac9ed1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Transaction](../transaction.md)

# scrollTargetAnchor

<sub>Instance Property</sub>

The preferred alignment of the view within a scroll view’s visible region when scrolling to a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var scrollTargetAnchor: UnitPoint? { get set }
```

## Discussion

Use this API in conjunction with a `ScrollViewProxy/scrollTo(_:anchor)` or when updating the binding provided to a [scrollPosition(id:anchor:)](<../view/scrollposition(id_anchor_).md>).

```swift
@Binding var position: Item.ID?

var body: some View {
    ScrollView {
        LazyVStack {
            ForEach(items) { item in
                ItemView(item)
            }
        }
        .scrollTargetLayout()
    }
    .scrollPosition(id: $position)
    .safeAreaInset(edge: .bottom) {
        Button("Scroll To Bottom") {
            withAnimation {
                withTransaction(\.scrollTargetAnchor, .bottom) {
                    position = items.last?.id
                }
            }
        }
    }
}
```

When used with the [scrollPosition(id:anchor:)](<../view/scrollposition(id_anchor_).md>) modifier, this value will be preferred over the anchor specified in the modifier for the current transaction.

## See Also

### Getting information about a transaction

- [isContinuous](iscontinuous.md) — A Boolean value that indicates whether the transaction originated from an action that produces a sequence of values.
- [tracksVelocity](tracksvelocity.md) — Whether this transaction will track the velocity of any animatable properties that change.
- [subscript(_:)](<subscript(__).md>) — Accesses the transaction value associated with a custom key.
