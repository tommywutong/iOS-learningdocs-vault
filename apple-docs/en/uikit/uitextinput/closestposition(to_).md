---
title: 'closestPosition(to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/closestposition(to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/closestposition(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/closestposition%28to%3A%29.json'
content_hash: 'sha256:a307d01d629d70d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# closestPosition(to:)

<sub>Instance Method</sub>

Returns the position in a document that is closest to a specified point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func closestPosition(to point: CGPoint) -> UITextPosition?
```

## Parameters

- `point` — A point in the view that is drawing a document’s text.

## Return Value

An object locating a position in a document that is closest to `point`.

## See Also

### Working with geometry and hit-testing

- [- firstRectForRange:](<firstrect(for_).md>) — Returns the first rectangle that encloses a range of text in a document.
- [- selectionRectsForRange:](<selectionrects(for_).md>) — Returns an array of selection rects corresponding to the range of text.
- [- closestPositionToPoint:withinRange:](<closestposition(to_within_).md>) — Returns the position in a document that is closest to a specified point in a specified range.
- [- characterRangeAtPoint:](<characterrange(at_).md>) — Returns the character or range of characters that is at a specified point in a document.
