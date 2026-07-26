---
title: 'sizeThatFits(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/shape/sizethatfits(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/shape/sizethatfits(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shape/sizethatfits%28_%3A%29.json'
content_hash: 'sha256:6ea558465fe63873'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shape](../shape.md)

# sizeThatFits(_:)

<sub>Instance Method</sub>

Returns the size of the view that will render the shape, given a proposed size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func sizeThatFits(_ proposal: ProposedViewSize) -> CGSize
```

## Parameters

- `proposal` — A size proposal for the container.

## Return Value

A size that indicates how much space the shape needs.

## Discussion

Implement this method to tell the container of the shape how much space the shape needs to render itself, given a size proposal.

See [sizeThatFits(proposal:subviews:cache:)](<../layout/sizethatfits(proposal_subviews_cache_).md>) for more details about how the layout system chooses the size of views.

## Default Implementations

### Shape Implementations

- [sizeThatFits(_:)](<sizethatfits(__)-2vtnh.md>) — Returns the original proposal, with nil components replaced by a small positive value.

## See Also

### Defining a shape’s size and path

- [path(in:)](<path(in_).md>) — Describes this shape as a path within a rectangular frame of reference.
