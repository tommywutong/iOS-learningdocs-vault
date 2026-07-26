---
title: 'drawText(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uilabel/drawtext(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uilabel/drawtext(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilabel/drawtext%28in%3A%29.json'
content_hash: 'sha256:6dc0340c0adbe162'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILabel](../uilabel.md)

# drawText(in:)

<sub>Instance Method</sub>

Draws the label’s text, or its shadow, in the specified rectangle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func drawText(in rect: CGRect)
```

## Parameters

- `rect` — The rectangle in which to draw the text.

## Discussion

Don’t call this method directly. Override this method if you want to modify the default drawing behavior for the label’s text.

By the time the system calls this method, the current graphics context is already configured with the default environment and text color for drawing. In your overridden method, you can configure the current context further and then invoke `super` to do the actual drawing, or you can do the drawing yourself. If you do render the text yourself, don’t invoke `super`.

## See Also

### Drawing and positioning overrides

- [- textRectForBounds:limitedToNumberOfLines:](<textrect(forbounds_limitedtonumberoflines_).md>) — Returns the drawing rectangle for the label’s text.
