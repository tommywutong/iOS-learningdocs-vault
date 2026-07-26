---
title: 'fill(using:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.9+, Swift 4.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/sequence/fill(using:)-45en6'
source_url: 'https://developer.apple.com/documentation/swift/sequence/fill(using:)-45en6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence/fill%28using%3A%29-45en6.json'
content_hash: 'sha256:dbeefd2bb86012ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Sequence](../sequence.md)

# fill(using:)

<sub>Instance Method</sub>

Fills this list of rects in the current NSGraphicsContext with that rect’s associated color The compositing operation of the fill defaults to the context’s compositing operation, not necessarily using `.copy` like `NSRectFill()`.

<sub>macOS</sub>

```swift
func fill(using operation: NSCompositingOperation = NSGraphicsContext.current?.compositingOperation ?? .sourceOver)
```

## Discussion

> [!info] Precondition
> There must be a set current NSGraphicsContext.

## See Also

### Applying AppKit Graphic Operations

- [fill(using:)](<fill(using_)-l1te.md>) — Fills this list of rects in the current NSGraphicsContext in the context’s fill color. The compositing operation of the fill defaults to the context’s compositing operation, not necessarily using `.copy` like `NSRectFill()`.
- [clip()](<clip().md>) — Modifies the current graphics context clipping path by intersecting it with the graphical union of this list of rects This permanently modifies the graphics state, so the current state should be saved beforehand and restored afterwards.
