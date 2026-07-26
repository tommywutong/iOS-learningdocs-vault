---
title: 'defaultScrollAnchor(_:for:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/defaultscrollanchor(_:for:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/defaultscrollanchor(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/defaultscrollanchor%28_%3Afor%3A%29.json'
content_hash: 'sha256:227d29ae6f07b229'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# defaultScrollAnchor(_:for:)

<sub>Instance Method</sub>

Associates an anchor to control the position of a scroll view in a particular circumstance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func defaultScrollAnchor(_ anchor: UnitPoint?, for role: ScrollAnchorRole) -> some View

```

## Discussion

You can associate a [UnitPoint](../unitpoint.md) to a [ScrollView](../scrollview.md) using the [defaultScrollAnchor(_:)](<defaultscrollanchor(__).md>) modifier. By default, the system uses this point for different kinds of behaviors including:

- Where the scroll view should initially be scrolled
- How the scroll view should handle content size or container size changes
- How the scroll view should align content smaller than its container size

You can further customize this behavior by assigning different unit points for these different cases.

For example, you can use the [defaultScrollAnchor(_:)](<defaultscrollanchor(__).md>) modifier to provide a value of [bottom](../unitpoint/bottom.md) as the anchor for all cases and then opt out of certain cases by providing a different value for them.

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
.defaultScrollAnchor(.topLeading, for: .alignment)
```

## See Also

### Managing scroll position

- [scrollPosition(_:anchor:)](<scrollposition(__anchor_).md>) — Associates a binding to a scroll position with a scroll view within this view.
- [scrollPosition(id:anchor:)](<scrollposition(id_anchor_).md>) — Associates a binding to be updated when a scroll view within this view scrolls.
- [defaultScrollAnchor(_:)](<defaultscrollanchor(__).md>) — Associates an anchor to control which part of the scroll view’s content should be rendered by default.
- [ScrollAnchorRole](../scrollanchorrole.md) — A type defining the role of a scroll anchor.
- [ScrollPosition](../scrollposition.md) — A type that defines the semantic position of where a scroll view is scrolled within its content.
