---
title: synchronize()
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontext/synchronize()
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/synchronize()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/synchronize%28%29.json'
content_hash: 'sha256:507f07010788c248'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# synchronize()

<sub>Instance Method</sub>

Marks a window context for update.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func synchronize()
```

## Discussion

When you call this function, all drawing operations since the last update are flushed at the next regular opportunity. Under normal conditions, you do not need to call this function.

## See Also

### Managing a Graphics Context

- [CGContextFlush](<flush().md>) — Forces all pending drawing operations in a window context to be rendered immediately to the destination device.
- [CGContextSetBlendMode](<setblendmode(__).md>) — Sets how sample values are composited by a graphics context.
- [CGBlendMode](../cgblendmode.md) — Compositing operations for images.
- [CGContextSetRenderingIntent](<setrenderingintent(__).md>) — Sets the rendering intent in the current graphics state.
