---
title: 'beginTransparencyLayer(in:auxiliaryInfo:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/begintransparencylayer(in:auxiliaryinfo:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/begintransparencylayer(in:auxiliaryinfo:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/begintransparencylayer%28in%3Aauxiliaryinfo%3A%29.json'
content_hash: 'sha256:a9dc91e34c832626'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# beginTransparencyLayer(in:auxiliaryInfo:)

<sub>Instance Method</sub>

Begins a transparency layer whose contents are bounded by the specified rectangle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func beginTransparencyLayer(in rect: CGRect, auxiliaryInfo auxInfo: CFDictionary?)
```

## Parameters

- `rect` — The rectangle, specified in user space, that bounds the transparency layer.

- `auxInfo` — A dictionary that specifies any additional information, or `nil`.

## Discussion

This function is identical to [CGContextBeginTransparencyLayer](<begintransparencylayer(auxiliaryinfo_).md>) except that the content of the transparency layer is within the bounds of the provided rectangle.

## See Also

### Working with Transparency Layers

- [CGContextBeginTransparencyLayer](<begintransparencylayer(auxiliaryinfo_).md>) — Begins a transparency layer.
- [CGContextEndTransparencyLayer](<endtransparencylayer().md>) — Ends a transparency layer.
