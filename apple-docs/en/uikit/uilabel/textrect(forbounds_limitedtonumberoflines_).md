---
title: 'textRect(forBounds:limitedToNumberOfLines:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uilabel/textrect(forbounds:limitedtonumberoflines:)'
source_url: 'https://developer.apple.com/documentation/uikit/uilabel/textrect(forbounds:limitedtonumberoflines:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilabel/textrect%28forbounds%3Alimitedtonumberoflines%3A%29.json'
content_hash: 'sha256:345d28c242f9fe30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILabel](../uilabel.md)

# textRect(forBounds:limitedToNumberOfLines:)

<sub>Instance Method</sub>

Returns the drawing rectangle for the label’s text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func textRect(forBounds bounds: CGRect, limitedToNumberOfLines numberOfLines: Int) -> CGRect
```

## Parameters

- `bounds` — The bounding rectangle of the label.

- `numberOfLines` — The maximum number of lines to use for the label. The value `0` indicates the label has no maximum number of lines and the rectangle should encompass all of the text.

## Return Value

The computed drawing rectangle for the label’s text.

## Discussion

Override this method in subclasses that require changes in the label’s bounding rectangle to occur before the system performs other text layout calculations. Use the value in the `numberOfLines` parameter to limit the height of the returned rectangle to the specified number of lines of text.

The system may call this method if there was a prior call to the [- sizeToFit](<../uiview/sizetofit().md>) or [- sizeThatFits:](<../uiview/sizethatfits(__).md>) method. Note that labels in [UITableViewCell](../uitableviewcell.md) objects have sizes based on cell dimensions, and not on a requested size.

## See Also

### Drawing and positioning overrides

- [- drawTextInRect:](<drawtext(in_).md>) — Draws the label’s text, or its shadow, in the specified rectangle.
