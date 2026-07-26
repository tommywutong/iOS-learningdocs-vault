---
title: 'leftViewRect(forBounds:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextfield/leftviewrect(forbounds:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/leftviewrect(forbounds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/leftviewrect%28forbounds%3A%29.json'
content_hash: 'sha256:84d06cef0d784427'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# leftViewRect(forBounds:)

<sub>Instance Method</sub>

Returns the drawing rectangle of the text field’s left overlay view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func leftViewRect(forBounds bounds: CGRect) -> CGRect
```

## Parameters

- `bounds` — The bounding rectangle of the receiver.

## Return Value

The rectangle in which to draw the left overlay view.

## Discussion

You should not call this method directly. If you want to place the left overlay view in a different location, you can override this method and return the new rectangle. Note that the drawing rectangle remains unchanged in a right-to-left user interface.

## See Also

### Drawing and positioning overrides

- [- textRectForBounds:](<textrect(forbounds_).md>) — Returns the drawing rectangle for the text field’s text.
- [- drawTextInRect:](<drawtext(in_).md>) — Draws the text field’s text in the specified rectangle. _(deprecated)_
- [- placeholderRectForBounds:](<placeholderrect(forbounds_).md>) — Returns the drawing rectangle for the text field’s placeholder text.
- [- drawPlaceholderInRect:](<drawplaceholder(in_).md>) — Draws the text field’s placeholder text in the specified rectangle.
- [- borderRectForBounds:](<borderrect(forbounds_).md>) — Returns the text field’s border rectangle.
- [- editingRectForBounds:](<editingrect(forbounds_).md>) — Returns the rectangle for displaying editable text.
- [- clearButtonRectForBounds:](<clearbuttonrect(forbounds_).md>) — Returns the drawing rectangle for the built-in Clear button.
- [- rightViewRectForBounds:](<rightviewrect(forbounds_).md>) — Returns the drawing location of the text field’s right overlay view.
