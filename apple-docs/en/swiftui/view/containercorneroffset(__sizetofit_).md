---
title: 'containerCornerOffset(_:sizeToFit:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/containercorneroffset(_:sizetofit:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/containercorneroffset(_:sizetofit:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/containercorneroffset%28_%3Asizetofit%3A%29.json'
content_hash: 'sha256:e6a8b60d592e5d5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# containerCornerOffset(_:sizeToFit:)

<sub>Instance Method</sub>

Adjusts the view’s layout to avoid the container view’s corner insets for the specified edges.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func containerCornerOffset(_ edges: Edge.Set, sizeToFit: Bool = false) -> some View

```

## Parameters

- `edges` — The set of edges which the container view should add corner insets from.

- `sizeToFit` — A flag indicating when this view is offset off a corner inset whether its size should attempt to fit into its remaining space of the view or fill its original size.

## Discussion

Use this modifier when you would like the view’s layout to adapt to avoid the container view’s corner insets for a set of edges. Corner insets may include pieces of system UI as well as the corner radii for windows and presentations. When a specific edge is provided the view is positioned to avoid insets from only the corners of that edge. When multiple corner edges overlap in the same axis the view will be positioned off the larger overlapping inset.

```swift
DrawingCanvasView(canvas: $canvas)
    .ignoresSafeArea()
    .overlay(alignment: .topLeading) {
        DrawingToolPaletteView(tool: $selectedTool)
            .containerCornerOffset(.horizontal)
    }
```

The modifier provides a `sizeToFit` parameter to indicate how the view should be sized when it has been offset from a corner inset. By default, `false` is provided, and the content’s size will be unchanged, only the position of the view’s content will be offset. When `true`, the content will attempt to size itself with a proposal using the remaining size of the original view subtracted from the overlapping corner insets.

## See Also

### Size

- [frame(width:height:alignment:)](<frame(width_height_alignment_).md>) — Positions this view within an invisible frame with the specified size.
- [frame(depth:alignment:)](<frame(depth_alignment_).md>) — Positions this view within an invisible frame with the specified depth.
- [frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)](<frame(minwidth_idealwidth_maxwidth_minheight_idealheight_maxheight_alignment_).md>) — Positions this view within an invisible frame having the specified size constraints.
- [frame(minDepth:idealDepth:maxDepth:alignment:)](<frame(mindepth_idealdepth_maxdepth_alignment_).md>) — Positions this view within an invisible frame having the specified depth constraints.
- [containerRelativeFrame(_:alignment:)](<containerrelativeframe(__alignment_).md>) — Positions this view within an invisible frame with a size relative to the nearest container.
- [containerRelativeFrame(_:alignment:_:)](<containerrelativeframe(__alignment___).md>) — Positions this view within an invisible frame with a size relative to the nearest container.
- [containerRelativeFrame(_:count:span:spacing:alignment:)](<containerrelativeframe(__count_span_spacing_alignment_).md>) — Positions this view within an invisible frame with a size relative to the nearest container.
- [fixedSize()](<fixedsize().md>) — Fixes this view at its ideal size.
- [fixedSize(horizontal:vertical:)](<fixedsize(horizontal_vertical_).md>) — Fixes this view at its ideal size in the specified dimensions.
- [layoutPriority(_:)](<layoutpriority(__).md>) — Sets the priority by which a parent layout should apportion space to this child.
