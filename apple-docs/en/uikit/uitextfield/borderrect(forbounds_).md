---
title: 'borderRect(forBounds:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextfield/borderrect(forbounds:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/borderrect(forbounds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/borderrect%28forbounds%3A%29.json'
content_hash: 'sha256:f36e38e7e48049db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# borderRect(forBounds:)

<sub>Instance Method</sub>

Returns the text field’s border rectangle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func borderRect(forBounds bounds: CGRect) -> CGRect
```

## Parameters

- `bounds` — The bounding rectangle of the receiver.

## Return Value

The border rectangle for the receiver.

## Discussion

You should not call this method directly. If you want to provide a different border rectangle for drawing, you can override this method and return that rectangle.

The default implementation of this method returns the original `bounds` rectangle.

## See Also

### Drawing and positioning overrides

- [- textRectForBounds:](<textrect(forbounds_).md>) — Returns the drawing rectangle for the text field’s text.
- [- drawTextInRect:](<drawtext(in_).md>) — Draws the text field’s text in the specified rectangle. _(deprecated)_
- [- placeholderRectForBounds:](<placeholderrect(forbounds_).md>) — Returns the drawing rectangle for the text field’s placeholder text.
- [- drawPlaceholderInRect:](<drawplaceholder(in_).md>) — Draws the text field’s placeholder text in the specified rectangle.
- [- editingRectForBounds:](<editingrect(forbounds_).md>) — Returns the rectangle for displaying editable text.
- [- clearButtonRectForBounds:](<clearbuttonrect(forbounds_).md>) — Returns the drawing rectangle for the built-in Clear button.
- [- leftViewRectForBounds:](<leftviewrect(forbounds_).md>) — Returns the drawing rectangle of the text field’s left overlay view.
- [- rightViewRectForBounds:](<rightviewrect(forbounds_).md>) — Returns the drawing location of the text field’s right overlay view.
