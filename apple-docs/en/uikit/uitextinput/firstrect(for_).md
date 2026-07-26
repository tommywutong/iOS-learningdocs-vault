---
title: 'firstRect(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/firstrect(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/firstrect(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/firstrect%28for%3A%29.json'
content_hash: 'sha256:e1e911517a69205e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# firstRect(for:)

<sub>Instance Method</sub>

Returns the first rectangle that encloses a range of text in a document.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func firstRect(for range: UITextRange) -> CGRect
```

## Parameters

- `range` — An object that represents a range of text in a document.

## Return Value

The first rectangle in a `range` of text. You might use this rectangle to draw a correction rectangle. The “first” in the name refers the rectangle enclosing the first line when the range encompasses multiple lines of text.

## See Also

### Related Documentation

- [- caretRectForPosition:](<caretrect(for_).md>) — Returns a rectangle to draw the caret at a specified insertion point.

### Working with geometry and hit-testing

- [- closestPositionToPoint:](<closestposition(to_).md>) — Returns the position in a document that is closest to a specified point.
- [- selectionRectsForRange:](<selectionrects(for_).md>) — Returns an array of selection rects corresponding to the range of text.
- [- closestPositionToPoint:withinRange:](<closestposition(to_within_).md>) — Returns the position in a document that is closest to a specified point in a specified range.
- [- characterRangeAtPoint:](<characterrange(at_).md>) — Returns the character or range of characters that is at a specified point in a document.
