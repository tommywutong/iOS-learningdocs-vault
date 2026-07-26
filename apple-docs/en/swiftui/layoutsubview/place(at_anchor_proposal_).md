---
title: 'place(at:anchor:proposal:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/layoutsubview/place(at:anchor:proposal:)'
source_url: 'https://developer.apple.com/documentation/swiftui/layoutsubview/place(at:anchor:proposal:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/layoutsubview/place%28at%3Aanchor%3Aproposal%3A%29.json'
content_hash: 'sha256:d3f612b87dc0d55e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LayoutSubview](../layoutsubview.md)

# place(at:anchor:proposal:)

<sub>Instance Method</sub>

Assigns a position and proposed size to the subview.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func place(at position: CGPoint, anchor: UnitPoint = .topLeading, proposal: ProposedViewSize)
```

## Parameters

- `position` — The place where the anchor of the subview should appear in its container view, relative to container’s bounds.

- `anchor` — The unit point on the subview that appears at `position`. You can use a built-in point, like [center](../unitpoint/center.md), or you can create a custom [UnitPoint](../unitpoint.md).

- `proposal` — A proposed size for the subview. In SwiftUI, views choose their own size, but can take a size proposal from their parent view into account when doing so.

## Discussion

Call this method from your implementation of the [Layout](../layout.md) protocol’s [placeSubviews(in:proposal:subviews:cache:)](<../layout/placesubviews(in_proposal_subviews_cache_).md>) method for each subview arranged by the layout. Provide a position within the container’s bounds where the subview should appear, and an anchor that indicates which part of the subview appears at that point.

Include a proposed size that the subview can take into account when sizing itself. To learn the subview’s size for a given proposal before calling this method, you can call the [dimensions(in:)](<dimensions(in_).md>) or [sizeThatFits(_:)](<sizethatfits(__).md>) method on the subview with the same proposal. That enables you to know subview sizes before committing to subview positions.

> [!important] Important
> Call this method only from within your [Layout](../layout.md) type’s implementation of the [placeSubviews(in:proposal:subviews:cache:)](<../layout/placesubviews(in_proposal_subviews_cache_).md>) method.

If you call this method more than once for a subview, the last call takes precedence. If you don’t call this method for a subview, the subview appears at the center of its layout container and uses the layout container’s size proposal.
