---
title: 'scrollPosition(_:anchor:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/scrollposition(_:anchor:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/scrollposition(_:anchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/scrollposition%28_%3Aanchor%3A%29.json'
content_hash: 'sha256:cd9f7187339db289'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# scrollPosition(_:anchor:)

<sub>Instance Method</sub>

Associates a binding to a scroll position with a scroll view within this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func scrollPosition(_ position: Binding<ScrollPosition>, anchor: UnitPoint? = nil) -> some View

```

## Discussion

Use this modifier to control where a scroll view is positioned. You can use the [ScrollPosition](../scrollposition.md) type to scroll in a variety of ways:

- scroll to a view with a provided identity
- scroll to a concrete offset
- scroll to an edge

You can create a scroll position with a specified view identity type

```swift
@State private var position
    = ScrollPosition(idType: MyItem.ID.self)
```

SwiftUI will use that along with the views in the scroll view’s scroll target layout to programmatically scroll to those views and to update the [viewID](../scrollposition/viewid.md) property as the user scrolls. Use the [scrollTargetLayout(isEnabled:)](<scrolltargetlayout(isenabled_).md>) modifier to configure which the layout that contains your scroll targets.

When scrolling to a view with an identifier, SwiftUI will update the position with the value of the top-most view scrolled within the visible region of the scroll view.

In the following example, the position binding will update to reflect the top-most ItemView as the scroll view scrolls.

```swift
@Binding var items: [MyItem]
@State private var position: ScrollPosition
    = .init(idType: MyItem.ID.self)

ScrollView {
    LazyVStack {
        ForEach(items) { item in
            ItemView(item)
        }
    }
    .scrollTargetLayout()
}
.scrollPosition($position)
```

You can then query the currently scrolled id by using the [viewID(type:)](<../scrollposition/viewid(type_).md>).

```swift
let viewID: MyItem.ID = position.viewID(type: MyItem.ID.self)
```

While most use cases will use view identity based scrolling, you can also use the scroll position type to scroll to offsets or edges. For example, you can create a button that scrolls to the bottom of the scroll view by specifying an edge.

```swift
Button("Scroll to bottom") {
    position.scrollTo(edge: .bottom)
}
```

When configuring a scroll position, SwiftUI will attempt to keep that position stable. For an edge, that means keeping a top aligned scroll view scrolled to the top if the content size changes. For a point, SwiftUI won’t attempt to keep that exact offset scrolled when the content size changes nor will it update to a new offset when that changes.

For view identity positions, SwiftUI will attempt to keep the view with the identity specified in the provided binding visible when events occur that might cause it to be scrolled out of view by the system. Some examples of these include:

- The data backing the content of a scroll view is re-ordered.
- The size of the scroll view changes, like when a window is resized on macOS or during a rotation on iOS.
- The scroll view initially lays out it content defaulting to the top most view, but the binding has a different view’s identity.

You can provide an anchor to a view identity based position to:

- Influence which view the system chooses as the view whose identity value will update the providing binding as the scroll view scrolls.
- Control the alignment of the view when scrolling to a view when writing a new binding value.

In the example below, the bottom most view will be chosen to update the position binding with.

```swift
ScrollView {
    LazyVStack {
        ForEach(items) { item in
            ItemView(item)
        }
    }
    .scrollTargetLayout()
}
.scrollPosition($position, anchor: .bottom)
```

For example, providing a value of [bottom](../unitpoint/bottom.md) will prefer to have the bottom-most view chosen and prefer to scroll to views aligned to the bottom.

## See Also

### Managing scroll position

- [scrollPosition(id:anchor:)](<scrollposition(id_anchor_).md>) — Associates a binding to be updated when a scroll view within this view scrolls.
- [defaultScrollAnchor(_:)](<defaultscrollanchor(__).md>) — Associates an anchor to control which part of the scroll view’s content should be rendered by default.
- [defaultScrollAnchor(_:for:)](<defaultscrollanchor(__for_).md>) — Associates an anchor to control the position of a scroll view in a particular circumstance.
- [ScrollAnchorRole](../scrollanchorrole.md) — A type defining the role of a scroll anchor.
- [ScrollPosition](../scrollposition.md) — A type that defines the semantic position of where a scroll view is scrolled within its content.
