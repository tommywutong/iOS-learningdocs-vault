---
title: adjustsFontSizeToFitWidth
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilabel/adjustsfontsizetofitwidth
source_url: 'https://developer.apple.com/documentation/uikit/uilabel/adjustsfontsizetofitwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilabel/adjustsfontsizetofitwidth.json'
content_hash: 'sha256:0d0247c626d6fb10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILabel](../uilabel.md)

# adjustsFontSizeToFitWidth

<sub>Instance Property</sub>

A Boolean value that determines whether the label reduces the text’s font size to fit the title string into the label’s bounding rectangle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var adjustsFontSizeToFitWidth: Bool { get set }
```

## Discussion

Normally, the label draws the text with the font you specify in the [font](font.md) property. If this property is [true](../../swift/true.md), and the text in the [text](text.md) property exceeds the label’s bounding rectangle, the label reduces the font size until the text fits or it has scaled the font down to the minimum font size. The default value for this property is [false](../../swift/false.md). If you change it to [true](../../swift/true.md), be sure that you also set an appropriate minimum font scale by modifying the [minimumScaleFactor](minimumscalefactor.md) property. This autoshrinking behavior is only intended for use with a single-line label.

To enable [adjustsFontSizeToFitWidth](adjustsfontsizetofitwidth.md) in Interface Builder, choose Minimum Font Scale from the Autoshrink pop-up menu in the label’s Attributes inspector.

## See Also

### Related Documentation

- [font](font.md) — The font of the text.
- [enablesMarqueeWhenAncestorFocused](enablesmarqueewhenancestorfocused.md) — A Boolean value that determines whether the label scrolls its text while one of its containing views has focus.

### Sizing the label’s text

- [allowsDefaultTighteningForTruncation](allowsdefaulttighteningfortruncation.md) — A Boolean value that determines whether the label tightens text before truncating.
- [baselineAdjustment](baselineadjustment.md) — An option that controls whether the text’s baseline remains fixed when text needs to shrink to fit in the label.
- [minimumScaleFactor](minimumscalefactor.md) — The minimum scale factor for the label’s text.
- [numberOfLines](numberoflines.md) — The maximum number of lines for rendering text.
- [sizingRule](../uiletterformawareadjusting/sizingrule.md) — The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.
