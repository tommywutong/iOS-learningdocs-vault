---
title: allowsDefaultTighteningForTruncation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilabel/allowsdefaulttighteningfortruncation
source_url: 'https://developer.apple.com/documentation/uikit/uilabel/allowsdefaulttighteningfortruncation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilabel/allowsdefaulttighteningfortruncation.json'
content_hash: 'sha256:84ef113c4a39e83a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILabel](../uilabel.md)

# allowsDefaultTighteningForTruncation

<sub>Instance Property</sub>

A Boolean value that determines whether the label tightens text before truncating.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var allowsDefaultTighteningForTruncation: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md), the label tightens intercharacter spacing of its text before allowing any truncation to occur. The label determines the maximum amount of tightening automatically based on the font, current line width, line break mode, and other relevant information. This autoshrinking behavior is only intended for use with a single-line label.

The default value of this property is [false](../../swift/false.md).

## See Also

### Related Documentation

- [enablesMarqueeWhenAncestorFocused](enablesmarqueewhenancestorfocused.md) — A Boolean value that determines whether the label scrolls its text while one of its containing views has focus.

### Sizing the label’s text

- [adjustsFontSizeToFitWidth](adjustsfontsizetofitwidth.md) — A Boolean value that determines whether the label reduces the text’s font size to fit the title string into the label’s bounding rectangle.
- [baselineAdjustment](baselineadjustment.md) — An option that controls whether the text’s baseline remains fixed when text needs to shrink to fit in the label.
- [minimumScaleFactor](minimumscalefactor.md) — The minimum scale factor for the label’s text.
- [numberOfLines](numberoflines.md) — The maximum number of lines for rendering text.
- [sizingRule](../uiletterformawareadjusting/sizingrule.md) — The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.
