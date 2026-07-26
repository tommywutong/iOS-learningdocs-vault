---
title: 'fill(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicsrenderercontext/fill(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsrenderercontext/fill(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsrenderercontext/fill%28_%3A%29.json'
content_hash: 'sha256:7b47802537b7ebc4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsRendererContext](../uigraphicsrenderercontext.md)

# fill(_:)

<sub>Instance Method</sub>

Paints a rectangular area with the currently selected fill color.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func fill(_ rect: CGRect)
```

## Parameters

- `rect` — A rectangle, specified in the Core Graphics coordinate space with values in points.

## Discussion

Before calling this method, select the fill color with the [- setFill](<../uicolor/setfill().md>) method on an instance of [UIColor](../uicolor.md).

For an example of how to use this method, see [Creating an image with an image renderer](../uigraphicsimagerenderer.md#Creating-an-image-with-an-image-renderer) in [UIGraphicsImageRenderer](../uigraphicsimagerenderer.md).

## See Also

### Drawing content

- [- strokeRect:](<stroke(__).md>) — Paints a rectangular path using the currently selected stroke color.
- [- strokeRect:blendMode:](<stroke(__blendmode_).md>) — Paints a rectangular path using the currently selected stroke color and specified blend mode.
- [- fillRect:blendMode:](<fill(__blendmode_).md>) — Paints a rectangular area with the currently selected fill color using the supplied blend mode.
