---
title: restoreGState()
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontext/restoregstate()
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontext/restoregstate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontext/restoregstate%28%29.json'
content_hash: 'sha256:0f006a0a92998006'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGContext](../cgcontext.md)

# restoreGState()

<sub>Instance Method</sub>

Sets the current graphics state to the state most recently saved.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func restoreGState()
```

## Discussion

Core Graphics removes the graphics state at the top of the stack so that the most recently saved state becomes the current graphics state.

## See Also

### Saving and Restoring Graphics State

- [CGContextSaveGState](<savegstate().md>) — Pushes a copy of the current graphics state onto the graphics state stack for the context.
