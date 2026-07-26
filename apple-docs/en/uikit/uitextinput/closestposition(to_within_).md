---
title: 'closestPosition(to:within:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/closestposition(to:within:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/closestposition(to:within:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/closestposition%28to%3Awithin%3A%29.json'
content_hash: 'sha256:57cf908b78e8bdda'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# closestPosition(to:within:)

<sub>Instance Method</sub>

Returns the position in a document that is closest to a specified point in a specified range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func closestPosition(to point: CGPoint, within range: UITextRange) -> UITextPosition?
```

## Parameters

- `point` — A point in the view that is drawing a document’s text.

- `range` — An object representing a range in a document’s text.

## Return Value

An object representing the character position in `range` that is closest to `point`.

## See Also

### Working with geometry and hit-testing

- [- firstRectForRange:](<firstrect(for_).md>) — Returns the first rectangle that encloses a range of text in a document.
- [- closestPositionToPoint:](<closestposition(to_).md>) — Returns the position in a document that is closest to a specified point.
- [- selectionRectsForRange:](<selectionrects(for_).md>) — Returns an array of selection rects corresponding to the range of text.
- [- characterRangeAtPoint:](<characterrange(at_).md>) — Returns the character or range of characters that is at a specified point in a document.
