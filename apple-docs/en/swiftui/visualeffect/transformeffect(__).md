---
title: 'transformEffect(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/visualeffect/transformeffect(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/visualeffect/transformeffect(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/visualeffect/transformeffect%28_%3A%29.json'
content_hash: 'sha256:42ac611ce35d9147'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [VisualEffect](../visualeffect.md)

# transformEffect(_:)

<sub>Instance Method</sub>

Applies an affine transformation to the view’s rendered output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func transformEffect(_ transform: CGAffineTransform) -> some VisualEffect

```

## Parameters

- `transform` — A [CGAffineTransform](../../corefoundation/cgaffinetransform.md) to apply to the view.

## Return Value

An effect that applies an affine transformation to the view’s rendered output.

## Discussion

Use `transformEffect(_:)` to rotate, scale, translate, or skew the output of the view according to the provided [CGAffineTransform](../../corefoundation/cgaffinetransform.md).

## See Also

### Applying a transform

- [transform3DEffect(_:)](<transform3deffect(__).md>) — Applies a 3D transformation to this view’s rendered output.
