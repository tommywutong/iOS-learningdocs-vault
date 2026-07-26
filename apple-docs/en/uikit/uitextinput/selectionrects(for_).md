---
title: 'selectionRects(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/selectionrects(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/selectionrects(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/selectionrects%28for%3A%29.json'
content_hash: 'sha256:5505ae66418e24ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# selectionRects(for:)

<sub>Instance Method</sub>

Returns an array of selection rects corresponding to the range of text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func selectionRects(for range: UITextRange) -> [UITextSelectionRect]
```

## Parameters

- `range` — An object representing a range in a document’s text.

## Return Value

An array of [UITextSelectionRect](../uitextselectionrect.md) objects that encompass the selection.

## See Also

### Working with geometry and hit-testing

- [- firstRectForRange:](<firstrect(for_).md>) — Returns the first rectangle that encloses a range of text in a document.
- [- closestPositionToPoint:](<closestposition(to_).md>) — Returns the position in a document that is closest to a specified point.
- [- closestPositionToPoint:withinRange:](<closestposition(to_within_).md>) — Returns the position in a document that is closest to a specified point in a specified range.
- [- characterRangeAtPoint:](<characterrange(at_).md>) — Returns the character or range of characters that is at a specified point in a document.
