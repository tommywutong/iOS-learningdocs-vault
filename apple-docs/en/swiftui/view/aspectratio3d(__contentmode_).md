---
title: 'aspectRatio3D(_:contentMode:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/aspectratio3d(_:contentmode:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/aspectratio3d(_:contentmode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/aspectratio3d%28_%3Acontentmode%3A%29.json'
content_hash: 'sha256:246e555d20d8d422'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# aspectRatio3D(_:contentMode:)

<sub>Instance Method</sub>

Constrains this view’s dimensions to the specified 3D aspect ratio.

<sub>visionOS</sub>

```swift
@export(implementation) nonisolated func aspectRatio3D(_ aspectRatio: Size3D? = nil, contentMode: ContentMode) -> some View

```

## Parameters

- `aspectRatio` — The ratio of width to height to depth to use for the resulting view. If `aspectRatio` is `nil`, the resulting view maintains this view’s aspect ratio.

- `contentMode` — A flag indicating whether this view should fit or fill the parent context.

## Return Value

A view that constrains this view’s dimensions to `aspectRatio`, using `contentMode` as its scaling algorithm.

## Discussion

If this view is resizable, the resulting view will have `aspectRatio` as its aspect ratio. In this example, the Model3D has a 2 : 3 : 1 width to height to depth ratio, and scales to fit its frame:

```swift
Model3D(named: "Sphere") { resolved in
    let ratio3D = Size3D(width: 2, height: 3, depth: 1)
    resolved
        .resizable()
        .aspectRatio3D(ratio3D, contentMode: .fit)
} placeholder: {
    ProgressView()
}
.frame(width: 200, height: 200)
.frame(depth: 200)
.border(Color(white: 0.75))
```

## See Also

### Scale

- [scaledToFill()](<scaledtofill().md>) — Scales this view to fill its parent.
- [scaledToFill3D()](<scaledtofill3d().md>) — Scales this view to fill its parent.
- [scaledToFit()](<scaledtofit().md>) — Scales this view to fit its parent.
- [scaledToFit3D()](<scaledtofit3d().md>) — Scales this view to fit its parent.
- [scaleEffect(_:anchor:)](<scaleeffect(__anchor_).md>) — Scales this view uniformly by the specified factor, relative to an anchor point.
- [scaleEffect(x:y:anchor:)](<scaleeffect(x_y_anchor_).md>) — Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [scaleEffect(x:y:z:anchor:)](<scaleeffect(x_y_z_anchor_).md>) — Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.
- [imageScale(_:)](<imagescale(__).md>) — Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.
- [aspectRatio(_:contentMode:)](<aspectratio(__contentmode_).md>) — Constrains this view’s dimensions to the specified aspect ratio.
