---
title: 'ignoresSafeArea(_:edges:alignment:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/ignoressafearea(_:edges:alignment:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/ignoressafearea(_:edges:alignment:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/ignoressafearea%28_%3Aedges%3Aalignment%3A%29.json'
content_hash: 'sha256:544698b7bdbadb72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# ignoresSafeArea(_:edges:alignment:)

<sub>Instance Method</sub>

Expands the safe area of a view aligning content within the new bounds using the provided alignment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func ignoresSafeArea(_ regions: SafeAreaRegions = .all, edges: Edge.Set = .all, alignment: Alignment?) -> some View

```

## Parameters

- `regions` — The regions to expand the view’s safe area into. The modifier expands into all safe area region types by default.

- `edges` — The set of edges to expand. Any edges that you don’t include in this set remain unchanged. The set includes all edges by default.

- `alignment` — The alignment of this view inside the resulting frame. Note that most alignment values have no apparent effect when the size of the frame happens to match that of this view.

## Return Value

A view with an expanded safe area.

## Discussion

By default, the SwiftUI layout system sizes and positions views to avoid certain safe areas. This ensures that system content like the software keyboard or edges of the device don’t obstruct your views. To extend your content into these regions, you can ignore safe areas on specific edges by applying this modifier.

When expanding the safe area, the SwiftUI layout system proposes the expanded size to the view. If your view has a fixed size, you can use the alignment property to determine how the fixed size view should be aligned in the expanded bounds.

For examples of how to use this modifier, see [Adding a background to your view](../adding-a-background-to-your-view.md).

## See Also

### Staying in the safe areas

- [ignoresSafeArea(_:edges:)](<ignoressafearea(__edges_).md>) — Expands the safe area of a view.
- [safeAreaInset(edge:alignment:spacing:content:)](<safeareainset(edge_alignment_spacing_content_).md>) — Shows the specified content beside the modified view.
- [safeAreaPadding(_:)](<safeareapadding(__).md>) — Adds the provided insets into the safe area of this view.
- [safeAreaPadding(_:_:)](<safeareapadding(____).md>) — Adds the provided insets into the safe area of this view.
- [SafeAreaRegions](../safearearegions.md) — A set of symbolic safe area regions.
