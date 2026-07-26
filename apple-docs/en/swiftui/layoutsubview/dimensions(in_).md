---
title: 'dimensions(in:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/layoutsubview/dimensions(in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/layoutsubview/dimensions(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layoutsubview/dimensions%28in%3A%29.json'
content_hash: 'sha256:9d66b44e65a13e7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LayoutSubview](../layoutsubview.md)

# dimensions(in:)

<sub>Instance Method</sub>

Asks the subview for its dimensions and alignment guides.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dimensions(in proposal: ProposedViewSize) -> ViewDimensions
```

## Parameters

- `proposal` — A proposed size for the subview. In SwiftUI, views choose their own size, but can take a size proposal from their parent view into account when doing so.

## Return Value

A [ViewDimensions](../viewdimensions.md) instance that includes a height and width, as well as a set of alignment guides.

## Discussion

Call this method to ask a subview of a custom [Layout](../layout.md) type about its size and alignment properties. You can call it from your implementation of any of that protocol’s methods, like [placeSubviews(in:proposal:subviews:cache:)](<../layout/placesubviews(in_proposal_subviews_cache_).md>) or [sizeThatFits(proposal:subviews:cache:)](<../layout/sizethatfits(proposal_subviews_cache_).md>), to get information for your layout calculations.

When you call this method, you propose a size using the `proposal` parameter. The subview can choose its own size, but might take the proposal into account. You can call this method more than once with different proposals to find out if the view is flexible. For example, you can propose:

- [zero](../proposedviewsize/zero.md) to get the subview’s minimum size.
- [infinity](../proposedviewsize/infinity.md) to get the subview’s maximum size.
- [unspecified](../proposedviewsize/unspecified.md) to get the subview’s ideal size.

If you need only the view’s height and width, you can use the [sizeThatFits(_:)](<sizethatfits(__).md>) method instead.

## See Also

### Getting subview characteristics

- [sizeThatFits(_:)](<sizethatfits(__).md>) — Asks the subview for its size.
- [spacing](spacing.md) — The subviews’s preferred spacing values.
- [priority](priority.md) — The layout priority of the subview.
