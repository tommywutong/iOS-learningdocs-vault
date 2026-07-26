---
title: 'fixedSize(horizontal:vertical:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/fixedsize(horizontal:vertical:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/fixedsize(horizontal:vertical:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/fixedsize%28horizontal%3Avertical%3A%29.json'
content_hash: 'sha256:b414ef4c9945fdfa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# fixedSize(horizontal:vertical:)

<sub>Instance Method</sub>

Fixes this view at its ideal size in the specified dimensions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func fixedSize(horizontal: Bool, vertical: Bool) -> some View

```

## Parameters

- `horizontal` — A Boolean value that indicates whether to fix the width of the view.

- `vertical` — A Boolean value that indicates whether to fix the height of the view.

## Return Value

A view that fixes this view at its ideal size in the dimensions specified by `horizontal` and `vertical`.

## Discussion

This function behaves like [fixedSize()](<fixedsize().md>), except with `fixedSize(horizontal:vertical:)` the fixing of the axes can be optionally specified in one or both dimensions. For example, if you horizontally fix a text view before wrapping it in the frame view, you’re telling the text view to maintain its ideal _width_. The view calculates this to be the space needed to represent the entire string.

```swift
Text("A single line of text, too long to fit in a box.")
    .fixedSize(horizontal: true, vertical: false)
    .frame(width: 200, height: 200)
    .border(Color.gray)
```

This can result in the view exceeding the parent’s bounds, which may or may not be the effect you want.

![A screenshot showing a text view exceeding the bounds of its](../../../../attachments/39fd04b5cd61b452f33e4b492d96759c/SwiftUI-View-fixedSize-3@2x.png)

## See Also

### Influencing a view’s size

- [frame(width:height:alignment:)](<frame(width_height_alignment_).md>) — Positions this view within an invisible frame with the specified size.
- [frame(depth:alignment:)](<frame(depth_alignment_).md>) — Positions this view within an invisible frame with the specified depth.
- [frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)](<frame(minwidth_idealwidth_maxwidth_minheight_idealheight_maxheight_alignment_).md>) — Positions this view within an invisible frame having the specified size constraints.
- [frame(minDepth:idealDepth:maxDepth:alignment:)](<frame(mindepth_idealdepth_maxdepth_alignment_).md>) — Positions this view within an invisible frame having the specified depth constraints.
- [containerRelativeFrame(_:alignment:)](<containerrelativeframe(__alignment_).md>) — Positions this view within an invisible frame with a size relative to the nearest container.
- [containerRelativeFrame(_:alignment:_:)](<containerrelativeframe(__alignment___).md>) — Positions this view within an invisible frame with a size relative to the nearest container.
- [containerRelativeFrame(_:count:span:spacing:alignment:)](<containerrelativeframe(__count_span_spacing_alignment_).md>) — Positions this view within an invisible frame with a size relative to the nearest container.
- [fixedSize()](<fixedsize().md>) — Fixes this view at its ideal size.
- [layoutPriority(_:)](<layoutpriority(__).md>) — Sets the priority by which a parent layout should apportion space to this child.
