---
title: 'clip(to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigraphicsrenderercontext/clip(to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsrenderercontext/clip(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsrenderercontext/clip%28to%3A%29.json'
content_hash: 'sha256:3ba6cc98f8ceeb08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGraphicsRendererContext](../uigraphicsrenderercontext.md)

# clip(to:)

<sub>Instance Method</sub>

Sets the clipping mask for the drawing context to the specified rectangle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func clip(to rect: CGRect)
```

## Parameters

- `rect` — The rectangle to which the drawing context is clipped, specified in the Core Graphics coordinate space with values in points.

## Discussion

To restrict the active drawing area to the specified rectangle, call this method before executing drawing commands.

To use a more complex shape as a clipping mask, use the [clip(to:mask:)](<../../coregraphics/cgcontext/clip(to_mask_).md>) method on the underlying Core Graphics context, accessed through the [CGContext](cgcontext.md) property.
