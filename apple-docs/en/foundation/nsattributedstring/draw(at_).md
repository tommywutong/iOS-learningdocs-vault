---
title: 'draw(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/draw(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/draw(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/draw%28at%3A%29.json'
content_hash: 'sha256:83d8c8c801bda15d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# draw(at:)

<sub>Instance Method</sub>

Draws the attributed string starting at the specified point in the current graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func draw(at point: CGPoint)
```

## Parameters

- `point` — The point in the current graphics context where you want to start drawing the string. The coordinate system of the graphics context is usually defined by the view in which you are drawing.

## Discussion

This method draws the entire string starting at the specified point. This method draws the line using the attributes specified in the attributed string itself. If newline characters are present in the string, those characters are honored and cause subsequent text to be placed on the next line underneath the starting point.

There must be either a focused view or an active graphics context when you call this method.

## See Also

### Related Documentation

- [- size](<size().md>) — Returns the size necessary to draw the string.
- [lockFocus()](<../../appkit/nsview/lockfocus().md>) — Locks the focus on the view, so subsequent commands take effect in the view’s window and coordinate system. _(deprecated)_

### Drawing the attributed string

- [- drawInRect:](<draw(in_).md>) — Draws the attributed string inside the specified bounding rectangle in the current graphics context.
- [- drawWithRect:options:context:](<draw(with_options_context_).md>) — Draws the attributed string in the specified bounding rectangle using the provided options.
