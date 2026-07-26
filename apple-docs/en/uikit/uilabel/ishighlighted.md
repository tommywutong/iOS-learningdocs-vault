---
title: isHighlighted
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilabel/ishighlighted
source_url: 'https://developer.apple.com/documentation/uikit/uilabel/ishighlighted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilabel/ishighlighted.json'
content_hash: 'sha256:c170543745e24808'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILabel](../uilabel.md)

# isHighlighted

<sub>Instance Property</sub>

A Boolean value that determines whether the label draws its text with a highlight.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isHighlighted: Bool { get set }
```

## Discussion

Setting this property causes the label to redraw with the appropriate highlight state. A subclass implementing a text button might set this property to [true](../../swift/true.md) when the user presses the button and set it to [false](../../swift/false.md) at other times. In order for the label to draw the highlight, the [highlightedTextColor](highlightedtextcolor.md) property must contain a non-`nil` value.

The default value of this property is [false](../../swift/false.md).

## See Also

### Managing highlight values

- [highlightedTextColor](highlightedtextcolor.md) — The highlight color for the label’s text.
