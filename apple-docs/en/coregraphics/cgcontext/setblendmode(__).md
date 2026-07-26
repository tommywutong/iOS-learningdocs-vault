---
title: 'setBlendMode(_:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgcontext/setblendmode(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/setblendmode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/setblendmode%28_%3A%29.json'
content_hash: 'sha256:754de3c9a0a34e5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# setBlendMode(_:)

<sub>Instance Method</sub>

Sets how sample values are composited by a graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setBlendMode(_ mode: CGBlendMode)
```

## Parameters

- `mode` — A blend mode. See [CGBlendMode](../cgblendmode.md) for a list of the constants you can supply.

## See Also

### Managing a Graphics Context

- [CGContextFlush](<flush().md>) — Forces all pending drawing operations in a window context to be rendered immediately to the destination device.
- [CGContextSynchronize](<synchronize().md>) — Marks a window context for update.
- [CGBlendMode](../cgblendmode.md) — Compositing operations for images.
- [CGContextSetRenderingIntent](<setrenderingintent(__).md>) — Sets the rendering intent in the current graphics state.
