---
title: 'clearButtonRect(forBounds:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextfield/clearbuttonrect(forbounds:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/clearbuttonrect(forbounds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/clearbuttonrect%28forbounds%3A%29.json'
content_hash: 'sha256:11cf803d360ade6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# clearButtonRect(forBounds:)

<sub>Instance Method</sub>

Returns the drawing rectangle for the built-in Clear button.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func clearButtonRect(forBounds bounds: CGRect) -> CGRect
```

## Parameters

- `bounds` — The bounding rectangle of the receiver.

## Return Value

The rectangle in which to draw the clear button.

## Discussion

You should not call this method directly. If you want to place the clear button in a different location, you can override this method and return the new rectangle. Your method should call the `super` implementation and modify the returned rectangle’s origin only. Changing the size of the clear button may cause unnecessary distortion of the button image.

## See Also

### Drawing and positioning overrides

- [- textRectForBounds:](<textrect(forbounds_).md>) — Returns the drawing rectangle for the text field’s text.
- [- drawTextInRect:](<drawtext(in_).md>) — Draws the text field’s text in the specified rectangle. _(deprecated)_
- [- placeholderRectForBounds:](<placeholderrect(forbounds_).md>) — Returns the drawing rectangle for the text field’s placeholder text.
- [- drawPlaceholderInRect:](<drawplaceholder(in_).md>) — Draws the text field’s placeholder text in the specified rectangle.
- [- borderRectForBounds:](<borderrect(forbounds_).md>) — Returns the text field’s border rectangle.
- [- editingRectForBounds:](<editingrect(forbounds_).md>) — Returns the rectangle for displaying editable text.
- [- leftViewRectForBounds:](<leftviewrect(forbounds_).md>) — Returns the drawing rectangle of the text field’s left overlay view.
- [- rightViewRectForBounds:](<rightviewrect(forbounds_).md>) — Returns the drawing location of the text field’s right overlay view.
