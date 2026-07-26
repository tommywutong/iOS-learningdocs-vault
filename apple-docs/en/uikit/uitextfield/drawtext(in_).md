---
title: 'drawText(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（15.0 起废弃）, iPadOS 2.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, tvOS（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uitextfield/drawtext(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/drawtext(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/drawtext%28in%3A%29.json'
content_hash: 'sha256:e1632b5e0aef2c63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# drawText(in:)

<sub>Instance Method</sub>

Draws the text field’s text in the specified rectangle.

> [!warning] Deprecated
> The system no longer calls this method.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func drawText(in rect: CGRect)
```

## Parameters

- `rect` — The rectangle in which to draw the text.

## Discussion

You should not call this method directly. If you want to customize the drawing behavior for the text, you can override this method to do your drawing.

By the time this method is called, the current graphics context is already configured with the default environment and text color for drawing. In your overridden method, you can configure the current context further and then invoke `super` to do the actual drawing or you can do the drawing yourself. If you do render the text yourself, you should not invoke `super`.

## See Also

### Drawing and positioning overrides

- [- textRectForBounds:](<textrect(forbounds_).md>) — Returns the drawing rectangle for the text field’s text.
- [- placeholderRectForBounds:](<placeholderrect(forbounds_).md>) — Returns the drawing rectangle for the text field’s placeholder text.
- [- drawPlaceholderInRect:](<drawplaceholder(in_).md>) — Draws the text field’s placeholder text in the specified rectangle.
- [- borderRectForBounds:](<borderrect(forbounds_).md>) — Returns the text field’s border rectangle.
- [- editingRectForBounds:](<editingrect(forbounds_).md>) — Returns the rectangle for displaying editable text.
- [- clearButtonRectForBounds:](<clearbuttonrect(forbounds_).md>) — Returns the drawing rectangle for the built-in Clear button.
- [- leftViewRectForBounds:](<leftviewrect(forbounds_).md>) — Returns the drawing rectangle of the text field’s left overlay view.
- [- rightViewRectForBounds:](<rightviewrect(forbounds_).md>) — Returns the drawing location of the text field’s right overlay view.
