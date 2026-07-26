---
title: 'textRect(forBounds:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextfield/textrect(forbounds:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/textrect(forbounds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/textrect%28forbounds%3A%29.json'
content_hash: 'sha256:d0bbfce1762cbfef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# textRect(forBounds:)

<sub>Instance Method</sub>

Returns the drawing rectangle for the text field’s text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func textRect(forBounds bounds: CGRect) -> CGRect
```

## Parameters

- `bounds` — The bounding rectangle of the receiver.

## Return Value

The computed drawing rectangle for the label’s text.

## Discussion

You should not call this method directly. If you want to customize the drawing rectangle for the text, you can override this method and return a different rectangle.

The default implementation of this method returns a rectangle that is derived from the control’s original bounds, but which does not include the area occupied by the receiver’s border or overlay views.

## See Also

### Drawing and positioning overrides

- [- drawTextInRect:](<drawtext(in_).md>) — Draws the text field’s text in the specified rectangle. _(deprecated)_
- [- placeholderRectForBounds:](<placeholderrect(forbounds_).md>) — Returns the drawing rectangle for the text field’s placeholder text.
- [- drawPlaceholderInRect:](<drawplaceholder(in_).md>) — Draws the text field’s placeholder text in the specified rectangle.
- [- borderRectForBounds:](<borderrect(forbounds_).md>) — Returns the text field’s border rectangle.
- [- editingRectForBounds:](<editingrect(forbounds_).md>) — Returns the rectangle for displaying editable text.
- [- clearButtonRectForBounds:](<clearbuttonrect(forbounds_).md>) — Returns the drawing rectangle for the built-in Clear button.
- [- leftViewRectForBounds:](<leftviewrect(forbounds_).md>) — Returns the drawing rectangle of the text field’s left overlay view.
- [- rightViewRectForBounds:](<rightviewrect(forbounds_).md>) — Returns the drawing location of the text field’s right overlay view.
