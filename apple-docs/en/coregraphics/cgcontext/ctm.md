---
title: ctm
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontext/ctm
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/ctm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/ctm.json'
content_hash: 'sha256:7aa0195d9c542c4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# ctm

<sub>Instance Property</sub>

Returns the current transformation matrix.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var ctm: CGAffineTransform { get }
```

## See Also

### Working with the Current Transformation Matrix

- [CGContextRotateCTM](<rotate(by_).md>) — Rotates the user coordinate system in a context.
- [CGContextScaleCTM](<scaleby(x_y_).md>) — Changes the scale of the user coordinate system in a context.
- [CGContextTranslateCTM](<translateby(x_y_).md>) — Changes the origin of the user coordinate system in a context.
- [CGContextConcatCTM](<concatenate(__).md>) — Transforms the user coordinate system in a context using a specified matrix.
