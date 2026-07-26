---
title: stroke()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibezierpath/stroke()
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/stroke()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/stroke%28%29.json'
content_hash: 'sha256:745f890e1d84b415'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# stroke()

<sub>Instance Method</sub>

Draws a line along the path using the current drawing properties.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func stroke()
```

## Discussion

The drawn line is centered on the path with its sides parallel to the path segment. This method applies the current drawing properties to the rendered path.

This method automatically saves the current graphics state prior to drawing and restores that state when it is done, so you do not have to save the graphics state yourself.

## See Also

### Drawing paths

- [- fill](<fill().md>) — Uses the current drawing properties to paint the region that the path encloses.
- [- fillWithBlendMode:alpha:](<fill(with_alpha_).md>) — Uses the specified blend mode and transparency values to paint the region that the path encloses.
- [- strokeWithBlendMode:alpha:](<stroke(with_alpha_).md>) — Draws a line along the path using the specified blend mode and transparency values.
