---
title: leftView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextfield/leftview
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/leftview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/leftview.json'
content_hash: 'sha256:c6688a1969a5abc7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# leftView

<sub>Instance Property</sub>

The overlay view that displays on the left (or leading) side of the text field.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var leftView: UIView? { get set }
```

## Discussion

You can use the left overlay view to indicate the intended behavior of the text field. For example, you might display a magnifying glass in this location to indicate that the text field is a search field. The left overlay view flips automatically in a right-to-left user interface.

The left overlay view is placed in the rectangle returned by the [- leftViewRectForBounds:](<leftviewrect(forbounds_).md>) method of the receiver. The image associated with this property should fit the given rectangle. If it does not fit, it is scaled to fit. If you specify a control for your view, the control tracks and sends actions as usual.

## See Also

### Related Documentation

- [- leftViewRectForBounds:](<leftviewrect(forbounds_).md>) — Returns the drawing rectangle of the text field’s left overlay view.

### Managing overlay views

- [clearButtonMode](clearbuttonmode.md) — A mode that controls when the standard Clear button appears in the text field.
- [leftViewMode](leftviewmode.md) — A mode that controls when the left overlay view appears in the text field.
- [rightView](rightview.md) — The overlay view that displays on the right (or trailing) side of the text field.
- [rightViewMode](rightviewmode.md) — A mode that controls when the right overlay view appears in the text field.
- [ViewMode](viewmode.md) — Constants that define when overlay views appear in a text field.
