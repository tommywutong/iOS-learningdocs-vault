---
title: clip()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.9+, Swift 4.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/sequence/clip()
source_url: 'https://developer.apple.com/documentation/swift/sequence/clip()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence/clip%28%29.json'
content_hash: 'sha256:fc9ceed0e4dbc762'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Sequence](../sequence.md)

# clip()

<sub>Instance Method</sub>

Modifies the current graphics context clipping path by intersecting it with the graphical union of this list of rects This permanently modifies the graphics state, so the current state should be saved beforehand and restored afterwards.

<sub>macOS</sub>

```swift
func clip()
```

## Discussion

> [!info] Precondition
> There must be a set current NSGraphicsContext.

## See Also

### Applying AppKit Graphic Operations

- [fill(using:)](<fill(using_)-l1te.md>) — Fills this list of rects in the current NSGraphicsContext in the context’s fill color. The compositing operation of the fill defaults to the context’s compositing operation, not necessarily using `.copy` like `NSRectFill()`.
- [fill(using:)](<fill(using_)-45en6.md>) — Fills this list of rects in the current NSGraphicsContext with that rect’s associated color The compositing operation of the fill defaults to the context’s compositing operation, not necessarily using `.copy` like `NSRectFill()`.
