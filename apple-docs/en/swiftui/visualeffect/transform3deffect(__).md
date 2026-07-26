---
title: 'transform3DEffect(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/visualeffect/transform3deffect(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/visualeffect/transform3deffect(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visualeffect/transform3deffect%28_%3A%29.json'
content_hash: 'sha256:0b78ffacfd96401f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VisualEffect](../visualeffect.md)

# transform3DEffect(_:)

<sub>Instance Method</sub>

Applies a 3D transformation to this view’s rendered output.

<sub>visionOS</sub>

```swift
@export(implementation) func transform3DEffect(_ transform: AffineTransform3D) -> some VisualEffect

```

## Parameters

- `transform` — The 3D transformation to apply to the view, interpreting it as a 3D plane in space.

## Return Value

An effect that renders transformed according to the provided `transform`

### Apply a transform about an anchor

This does not adjust the transform relative to an anchor point. Instead, apply the scale and rotation separately using [scaleEffect(_:anchor:)](<../view/scaleeffect(__anchor_).md>) together with [rotation3DEffect(_:anchor:)](<../view/rotation3deffect(__anchor_).md>).

```swift
Model3D(url: URL(string: "https://example.com/robot.usdz")!)
   .scaleEffect(transform.scale)
   .rotation3DEffect(transform.rotation ?? .identity)
   .transform3DEffect(AffineTransform3D(
       translation: transform.translation))
```

## See Also

### Applying a transform

- [transformEffect(_:)](<transformeffect(__).md>) — Applies an affine transformation to the view’s rendered output.
