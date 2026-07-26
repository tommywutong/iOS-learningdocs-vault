---
title: 'draw(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/draw(in:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/draw(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/draw%28in%3A%29.json'
content_hash: 'sha256:1df51fd10f740718'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# draw(in:)

<sub>Instance Method</sub>

Draws the attributed string inside the specified bounding rectangle in the current graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func draw(in rect: CGRect)
```

## Parameters

- `rect` — The bounding rectangle in which to draw the string. In AppKit, the origin is normally in the lower-left corner of the drawing area, but the origin is in the upper-left corner if the focused view is flipped.

## Discussion

This method draws as much of the string as it can inside the specified rectangle, wrapping the string text as needed to make it fit. If the string is too long to fit inside the rectangle, the method renders as much as possible and clips the rest. It is possible for a portion of a glyph to appear outside the area of `rect` if the image bounding box of the particular glyph exceeds its typographic bounding box. Text is drawn according to its line sweep direction; for example, Arabic text begins at the right edge and is potentially clipped on the left.

Layout always occurs from top to bottom. AppKit automatically adjusts the initial drawing point whether or not the view is flipped. For example, if the `rect` argument is `{0.0, 0.0, 100.0, 100.0}`, the text origin is {0.0, 0.0} when the view coordinates are flipped and {0.0, 100.0} when the view is not flipped.

This method draws the line using the attributes specified in the attributed string itself. If newline characters are present in the string, those characters are honored and cause subsequent text to be placed on the next line underneath the starting point.

There must be either a focused view or an active graphics context when you call this method.

## See Also

### Related Documentation

- [lockFocus()](<../../appkit/nsview/lockfocus().md>) — Locks the focus on the view, so subsequent commands take effect in the view’s window and coordinate system. _(deprecated)_

### Drawing the attributed string

- [- drawAtPoint:](<draw(at_).md>) — Draws the attributed string starting at the specified point in the current graphics context.
- [- drawWithRect:options:context:](<draw(with_options_context_).md>) — Draws the attributed string in the specified bounding rectangle using the provided options.
