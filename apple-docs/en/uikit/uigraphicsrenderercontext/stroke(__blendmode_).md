---
title: 'stroke(_:blendMode:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicsrenderercontext/stroke(_:blendmode:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsrenderercontext/stroke(_:blendmode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsrenderercontext/stroke%28_%3Ablendmode%3A%29.json'
content_hash: 'sha256:9128b057af6ad95d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsRendererContext](../uigraphicsrenderercontext.md)

# stroke(_:blendMode:)

<sub>Instance Method</sub>

Paints a rectangular path using the currently selected stroke color and specified blend mode.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func stroke(_ rect: CGRect, blendMode: CGBlendMode)
```

## Parameters

- `rect` — A rectangle, specified in the Core Graphics coordinate space with values in points.

- `blendMode` — The blend mode applied to the stroke operation.

## Discussion

Before calling this method, select the stroke color with the [- setStroke](<../uicolor/setstroke().md>) method on an instance of [UIColor](../uicolor.md).

The blend mode specifies how the new value for a given pixel is calculated, given the existing pixel value and the currently selected fill color. For more information on the blend modes available, see [CGBlendMode](../../coregraphics/cgblendmode.md).

## See Also

### Drawing content

- [- strokeRect:](<stroke(__).md>) — Paints a rectangular path using the currently selected stroke color.
- [- fillRect:blendMode:](<fill(__blendmode_).md>) — Paints a rectangular area with the currently selected fill color using the supplied blend mode.
- [- fillRect:](<fill(__).md>) — Paints a rectangular area with the currently selected fill color.
