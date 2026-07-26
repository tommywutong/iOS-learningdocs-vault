---
title: 'frame(depth:alignment:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/frame(depth:alignment:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/frame(depth:alignment:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/frame%28depth%3Aalignment%3A%29.json'
content_hash: 'sha256:85b26684f3b4adb8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# frame(depth:alignment:)

<sub>Instance Method</sub>

Positions this view within an invisible frame with the specified depth.

<sub>visionOS</sub>

```swift
@export(implementation) nonisolated func frame(depth: CGFloat?, alignment: DepthAlignment = .center) -> some View

```

## Parameters

- `depth` — A fixed depth for the resulting view. If `depth` is `nil`, the resulting view assumes this view’s sizing behavior.

- `alignment` — The alignment of this view inside the resulting view. `alignment` applies if this view is smaller than the size given by the resulting frame.

## Return Value

A view with a fixed dimension of `depth` if non-`nil`.

## Discussion

Use this method to specify a fixed size for a view’s depth. If you don’t specify a dimension, the resulting view assumes this view’s sizing behavior in depth.

## See Also

### Influencing a view’s size

- [frame(width:height:alignment:)](<frame(width_height_alignment_).md>) — Positions this view within an invisible frame with the specified size.
- [frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)](<frame(minwidth_idealwidth_maxwidth_minheight_idealheight_maxheight_alignment_).md>) — Positions this view within an invisible frame having the specified size constraints.
- [frame(minDepth:idealDepth:maxDepth:alignment:)](<frame(mindepth_idealdepth_maxdepth_alignment_).md>) — Positions this view within an invisible frame having the specified depth constraints.
- [containerRelativeFrame(_:alignment:)](<containerrelativeframe(__alignment_).md>) — Positions this view within an invisible frame with a size relative to the nearest container.
- [containerRelativeFrame(_:alignment:_:)](<containerrelativeframe(__alignment___).md>) — Positions this view within an invisible frame with a size relative to the nearest container.
- [containerRelativeFrame(_:count:span:spacing:alignment:)](<containerrelativeframe(__count_span_spacing_alignment_).md>) — Positions this view within an invisible frame with a size relative to the nearest container.
- [fixedSize()](<fixedsize().md>) — Fixes this view at its ideal size.
- [fixedSize(horizontal:vertical:)](<fixedsize(horizontal_vertical_).md>) — Fixes this view at its ideal size in the specified dimensions.
- [layoutPriority(_:)](<layoutpriority(__).md>) — Sets the priority by which a parent layout should apportion space to this child.
