---
title: 'frame(minDepth:idealDepth:maxDepth:alignment:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/frame(mindepth:idealdepth:maxdepth:alignment:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/frame(mindepth:idealdepth:maxdepth:alignment:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/frame%28mindepth%3Aidealdepth%3Amaxdepth%3Aalignment%3A%29.json'
content_hash: 'sha256:ef925049bf6b2a17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# frame(minDepth:idealDepth:maxDepth:alignment:)

<sub>Instance Method</sub>

Positions this view within an invisible frame having the specified depth constraints.

<sub>visionOS</sub>

```swift
@export(implementation) nonisolated func frame(minDepth: CGFloat? = nil, idealDepth: CGFloat? = nil, maxDepth: CGFloat? = nil, alignment: DepthAlignment = .center) -> some View

```

## Parameters

- `minDepth` — The minimum depth of the resulting frame.

- `idealDepth` — The ideal depth of the resulting frame.

- `maxDepth` — The maximum depth of the resulting frame.

- `alignment` — The alignment of this view inside the resulting frame. Note that most alignment values have no apparent effect when the size of the frame happens to match that of this view.

## Return Value

A view with flexible dimensions given by the call’s non-`nil` parameters.

## Discussion

Always specify at least one size characteristic when calling this method. Pass `nil` or leave out a characteristic to indicate that the frame should adopt this view’s sizing behavior, constrained by the other non-`nil` arguments.

The size proposed to this view is the size proposed to the frame, limited by any constraints specified, and with an ideal dimension specified replacing any corresponding unspecified dimensions in the proposal.

If no minimum or maximum constraint is specified in a given dimension, the frame adopts the sizing behavior of its child in that dimension. If both constraints are specified in a dimension, the frame unconditionally adopts the size proposed for it, clamped to the constraints. Otherwise, the size of the frame in either dimension is:

- If a minimum constraint is specified and the size proposed for the frame by the parent is less than the size of this view, the proposed size, clamped to that minimum.
- If a maximum constraint is specified and the size proposed for the frame by the parent is greater than the size of this view, the proposed size, clamped to that maximum.
- Otherwise, the size of this view.

## See Also

### Influencing a view’s size

- [frame(width:height:alignment:)](<frame(width_height_alignment_).md>) — Positions this view within an invisible frame with the specified size.
- [frame(depth:alignment:)](<frame(depth_alignment_).md>) — Positions this view within an invisible frame with the specified depth.
- [frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)](<frame(minwidth_idealwidth_maxwidth_minheight_idealheight_maxheight_alignment_).md>) — Positions this view within an invisible frame having the specified size constraints.
- [containerRelativeFrame(_:alignment:)](<containerrelativeframe(__alignment_).md>) — Positions this view within an invisible frame with a size relative to the nearest container.
- [containerRelativeFrame(_:alignment:_:)](<containerrelativeframe(__alignment___).md>) — Positions this view within an invisible frame with a size relative to the nearest container.
- [containerRelativeFrame(_:count:span:spacing:alignment:)](<containerrelativeframe(__count_span_spacing_alignment_).md>) — Positions this view within an invisible frame with a size relative to the nearest container.
- [fixedSize()](<fixedsize().md>) — Fixes this view at its ideal size.
- [fixedSize(horizontal:vertical:)](<fixedsize(horizontal_vertical_).md>) — Fixes this view at its ideal size in the specified dimensions.
- [layoutPriority(_:)](<layoutpriority(__).md>) — Sets the priority by which a parent layout should apportion space to this child.
