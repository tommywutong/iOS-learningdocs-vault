---
title: 'fill(with:alpha:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibezierpath/fill(with:alpha:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/fill(with:alpha:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/fill%28with%3Aalpha%3A%29.json'
content_hash: 'sha256:dc70563104a008d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# fill(with:alpha:)

<sub>Instance Method</sub>

Uses the specified blend mode and transparency values to paint the region that the path encloses.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func fill(with blendMode: CGBlendMode, alpha: CGFloat)
```

## Parameters

- `blendMode` — The blend mode determines how the filled path is composited with any existing rendered content.

- `alpha` — The amount of transparency to apply to the filled path. Values can range between `0.0` (transparent) and `1.0` (opaque). Values outside this range are clamped to `0.0` or `1.0`.

## Discussion

This method fills the path using the current fill color and drawing properties (plus the specified blend mode and transparency value). If the path contains any open subpaths, this method implicitly closes them before painting the fill region.

The painted region includes the pixels right up to, but not including, the path line itself. For paths with large line widths, this can result in overlap between the fill region and the stroked path (which is itself centered on the path line).

This method automatically saves the current graphics state prior to drawing and restores that state when it is done, so you do not have to save the graphics state yourself.

## See Also

### Drawing paths

- [- fill](<fill().md>) — Uses the current drawing properties to paint the region that the path encloses.
- [- stroke](<stroke().md>) — Draws a line along the path using the current drawing properties.
- [- strokeWithBlendMode:alpha:](<stroke(with_alpha_).md>) — Draws a line along the path using the specified blend mode and transparency values.
