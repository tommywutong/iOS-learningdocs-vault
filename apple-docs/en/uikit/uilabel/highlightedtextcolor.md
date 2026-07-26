---
title: highlightedTextColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilabel/highlightedtextcolor
source_url: 'https://developer.apple.com/documentation/uikit/uilabel/highlightedtextcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilabel/highlightedtextcolor.json'
content_hash: 'sha256:d07de5f6051bd91c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILabel](../uilabel.md)

# highlightedTextColor

<sub>Instance Property</sub>

The highlight color for the label’s text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var highlightedTextColor: UIColor? { get set }
```

## Discussion

Subclasses that use labels to implement a type of text button can use the value in this property when drawing the pressed state for the button. The label uses this value to display text whenever the [highlighted](ishighlighted.md) property is [true](../../swift/true.md).

The default value of this property is `nil`.

## See Also

### Managing highlight values

- [highlighted](ishighlighted.md) — A Boolean value that determines whether the label draws its text with a highlight.
