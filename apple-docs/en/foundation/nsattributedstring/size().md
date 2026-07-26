---
title: size()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsattributedstring/size()
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/size()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/size%28%29.json'
content_hash: 'sha256:f4ee313e6628281d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# size()

<sub>Instance Method</sub>

Returns the size necessary to draw the string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func size() -> CGSize
```

## Return Value

The minimum size required to draw the entire contents of the string.

## Discussion

You can use this method prior to drawing to compute how much space is required to draw the string.

This method may return fractional sizes. When setting the size of your view, use the [ceil](../../kernel/1557272-ceil.md) function to round fractional values up to the nearest whole number.

## See Also

### Related Documentation

- [- drawAtPoint:](<draw(at_).md>) — Draws the attributed string starting at the specified point in the current graphics context.
- [- drawInRect:](<draw(in_).md>) — Draws the attributed string inside the specified bounding rectangle in the current graphics context.

### Getting metrics for the string

- [- boundingRectWithSize:options:context:](<boundingrect(with_options_context_).md>) — Returns the bounding rectangle necessary to draw the string.
- [- containsAttachmentsInRange:](<containsattachments(in_).md>) — Returns a Boolean value that indicates if the attributed string contains an attachment in the specified range.
