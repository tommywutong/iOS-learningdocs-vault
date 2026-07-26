---
title: 'caretRect(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextinput/caretrect(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/caretrect(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/caretrect%28for%3A%29.json'
content_hash: 'sha256:280a77c80b58bc94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# caretRect(for:)

<sub>Instance Method</sub>

Returns a rectangle to draw the caret at a specified insertion point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func caretRect(for position: UITextPosition) -> CGRect
```

## Parameters

- `position` — An object that identifies a location in a text input area.

## Return Value

A rectangle that defines the area for drawing the caret.

## Discussion

The system uses this value to calculate the length of the beam—the vertical line representing the pointer—when using a trackpad to interact with a text input area. You must implement this method even if text never becomes editable, and an insertion point caret never appears.

## See Also

### Related Documentation

- [- firstRectForRange:](<firstrect(for_).md>) — Returns the first rectangle that encloses a range of text in a document.
- [UIPointerShape.verticalBeam(length:)](<../uipointershape-swift.enum/verticalbeam(length_).md>) — The pointer morphs into a vertical beam using the specified length.

### Providing the caret layout information

- [- caretTransformForPosition:](<carettransform(for_).md>) — Returns the transform to apply to the caret prior to drawing.
