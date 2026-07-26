---
title: scaledToFill3D()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view/scaledtofill3d()
source_url: 'https://developer.apple.com/documentation/swiftui/view/scaledtofill3d()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/scaledtofill3d%28%29.json'
content_hash: 'sha256:9a1e1aa6714a3b31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# scaledToFill3D()

<sub>Instance Method</sub>

Scales this view to fill its parent.

<sub>visionOS</sub>

```swift
@export(implementation) nonisolated func scaledToFill3D() -> some View

```

## Return Value

A view that scales this view to fit its parent, maintaining this view’s aspect ratio.

## Discussion

This view’s 3D aspect ratio is maintained as the view scales. This method is equivalent to calling `aspectRatio3D(nil, contentMode: .fill)`.

```swift
Model3D(named: "Sphere") { resolved in
    resolved
        .resizable()
        .scaledToFill3D()
} placeholder: {
    ProgressView()
}
.frame(width: 300, height: 100)
.frame(depth: 300)
.border(Color(white: 0.75))
```

## See Also

### Scale

- [scaledToFill()](<scaledtofill().md>) — Scales this view to fill its parent.
- [scaledToFit()](<scaledtofit().md>) — Scales this view to fit its parent.
- [scaledToFit3D()](<scaledtofit3d().md>) — Scales this view to fit its parent.
- [scaleEffect(_:anchor:)](<scaleeffect(__anchor_).md>) — Scales this view uniformly by the specified factor, relative to an anchor point.
- [scaleEffect(x:y:anchor:)](<scaleeffect(x_y_anchor_).md>) — Scales this view’s rendered output by the given horizontal and vertical amounts, relative to an anchor point.
- [scaleEffect(x:y:z:anchor:)](<scaleeffect(x_y_z_anchor_).md>) — Scales this view by the specified horizontal, vertical, and depth factors, relative to an anchor point.
- [imageScale(_:)](<imagescale(__).md>) — Scales images within the view according to one of the relative sizes available including small, medium, and large images sizes.
- [aspectRatio(_:contentMode:)](<aspectratio(__contentmode_).md>) — Constrains this view’s dimensions to the specified aspect ratio.
- [aspectRatio3D(_:contentMode:)](<aspectratio3d(__contentmode_).md>) — Constrains this view’s dimensions to the specified 3D aspect ratio.
