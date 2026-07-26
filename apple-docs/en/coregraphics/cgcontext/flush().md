---
title: flush()
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontext/flush()
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/flush()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/flush%28%29.json'
content_hash: 'sha256:dc391247712eab8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# flush()

<sub>Instance Method</sub>

Forces all pending drawing operations in a window context to be rendered immediately to the destination device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flush()
```

## Discussion

When you call this function, Core Graphics immediately flushes the current drawing to the destination device (for example, a screen). Because the system software flushes a context automatically at the appropriate times, calling this function could have an adverse effect on performance. Under normal conditions, you do not need to call this function.

## See Also

### Managing a Graphics Context

- [CGContextSynchronize](<synchronize().md>) — Marks a window context for update.
- [CGContextSetBlendMode](<setblendmode(__).md>) — Sets how sample values are composited by a graphics context.
- [CGBlendMode](../cgblendmode.md) — Compositing operations for images.
- [CGContextSetRenderingIntent](<setrenderingintent(__).md>) — Sets the rendering intent in the current graphics state.
