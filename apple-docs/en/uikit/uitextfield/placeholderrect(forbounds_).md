---
title: 'placeholderRect(forBounds:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextfield/placeholderrect(forbounds:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/placeholderrect(forbounds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/placeholderrect%28forbounds%3A%29.json'
content_hash: 'sha256:8c6fcb7ee389dbff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# placeholderRect(forBounds:)

<sub>Instance Method</sub>

Returns the drawing rectangle for the text field’s placeholder text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func placeholderRect(forBounds bounds: CGRect) -> CGRect
```

## Parameters

- `bounds` — The bounding rectangle of the receiver.

## Return Value

The computed drawing rectangle for the placeholder text.

## Discussion

You should not call this method directly. If you want to customize the drawing rectangle for the placeholder text, you can override this method and return a different rectangle.

If the placeholder string is empty or `nil`, this method is not called.

## See Also

### Drawing and positioning overrides

- [- textRectForBounds:](<textrect(forbounds_).md>) — Returns the drawing rectangle for the text field’s text.
- [- drawTextInRect:](<drawtext(in_).md>) — Draws the text field’s text in the specified rectangle. _(deprecated)_
- [- drawPlaceholderInRect:](<drawplaceholder(in_).md>) — Draws the text field’s placeholder text in the specified rectangle.
- [- borderRectForBounds:](<borderrect(forbounds_).md>) — Returns the text field’s border rectangle.
- [- editingRectForBounds:](<editingrect(forbounds_).md>) — Returns the rectangle for displaying editable text.
- [- clearButtonRectForBounds:](<clearbuttonrect(forbounds_).md>) — Returns the drawing rectangle for the built-in Clear button.
- [- leftViewRectForBounds:](<leftviewrect(forbounds_).md>) — Returns the drawing rectangle of the text field’s left overlay view.
- [- rightViewRectForBounds:](<rightviewrect(forbounds_).md>) — Returns the drawing location of the text field’s right overlay view.
