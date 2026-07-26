---
title: 'characterRange(at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/characterrange(at:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/characterrange(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/characterrange%28at%3A%29.json'
content_hash: 'sha256:edb67b65c6b04c13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# characterRange(at:)

<sub>Instance Method</sub>

Returns the character or range of characters that is at a specified point in a document.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func characterRange(at point: CGPoint) -> UITextRange?
```

## Parameters

- `point` — A point in the view that is drawing a document’s text.

## Return Value

An object representing a range that encloses a character (or characters) at `point`.

## See Also

### Working with geometry and hit-testing

- [- firstRectForRange:](<firstrect(for_).md>) — Returns the first rectangle that encloses a range of text in a document.
- [- closestPositionToPoint:](<closestposition(to_).md>) — Returns the position in a document that is closest to a specified point.
- [- selectionRectsForRange:](<selectionrects(for_).md>) — Returns an array of selection rects corresponding to the range of text.
- [- closestPositionToPoint:withinRange:](<closestposition(to_within_).md>) — Returns the position in a document that is closest to a specified point in a specified range.
