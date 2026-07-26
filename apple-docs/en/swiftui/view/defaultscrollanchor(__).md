---
title: 'defaultScrollAnchor(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/defaultscrollanchor(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/defaultscrollanchor(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/defaultscrollanchor%28_%3A%29.json'
content_hash: 'sha256:72202f16c231094f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# defaultScrollAnchor(_:)

<sub>Instance Method</sub>

Associates an anchor to control which part of the scroll view’s content should be rendered by default.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func defaultScrollAnchor(_ anchor: UnitPoint?) -> some View

```

## Discussion

Use this modifier to specify an anchor to control both which part of the scroll view’s content should be visible initially and how the scroll view handles content size changes.

Provide a value of [center](../unitpoint/center.md) to have the scroll view start in the center of its content when a scroll view is scrollable in both axes.

```swift
ScrollView([.horizontal, .vertical]) {
    // initially centered content
}
.defaultScrollAnchor(.center)
```

Provide a value of [bottom](../unitpoint/bottom.md) to have the scroll view start at the bottom of its content when scrollable in the vertical axis.

```swift
@Binding var items: [Item]
@Binding var scrolledID: Item.ID?

ScrollView {
    LazyVStack {
        ForEach(items) { item in
            ItemView(item)
        }
    }
}
.defaultScrollAnchor(.bottom)
```

The user may scroll away from the initial defined scroll position. When the content size of the scroll view changes, it may consult the anchor to know how to reposition the content.

## See Also

### Managing scroll position

- [scrollPosition(_:anchor:)](<scrollposition(__anchor_).md>) — Associates a binding to a scroll position with a scroll view within this view.
- [scrollPosition(id:anchor:)](<scrollposition(id_anchor_).md>) — Associates a binding to be updated when a scroll view within this view scrolls.
- [defaultScrollAnchor(_:for:)](<defaultscrollanchor(__for_).md>) — Associates an anchor to control the position of a scroll view in a particular circumstance.
- [ScrollAnchorRole](../scrollanchorrole.md) — A type defining the role of a scroll anchor.
- [ScrollPosition](../scrollposition.md) — A type that defines the semantic position of where a scroll view is scrolled within its content.
