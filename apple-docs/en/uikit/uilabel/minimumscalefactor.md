---
title: minimumScaleFactor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilabel/minimumscalefactor
source_url: 'https://developer.apple.com/documentation/uikit/uilabel/minimumscalefactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilabel/minimumscalefactor.json'
content_hash: 'sha256:13a95b39d66e7859'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILabel](../uilabel.md)

# minimumScaleFactor

<sub>Instance Property</sub>

The minimum scale factor for the label’s text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var minimumScaleFactor: CGFloat { get set }
```

## Discussion

If the [adjustsFontSizeToFitWidth](adjustsfontsizetofitwidth.md) is [true](../../swift/true.md), use this property to specify the smallest multiplier for the current font size that yields an acceptable font size for the label’s text. If you specify a value of `0` for this property, the label doesn’t scale the text down. The default value of this property is `0`.

To reveal the text field for editing minimum scale factor in Interface Builder, choose Minimum Font Scale from the Autoshrink pop-up menu in the label’s Attributes inspector.

## See Also

### Sizing the label’s text

- [adjustsFontSizeToFitWidth](adjustsfontsizetofitwidth.md) — A Boolean value that determines whether the label reduces the text’s font size to fit the title string into the label’s bounding rectangle.
- [allowsDefaultTighteningForTruncation](allowsdefaulttighteningfortruncation.md) — A Boolean value that determines whether the label tightens text before truncating.
- [baselineAdjustment](baselineadjustment.md) — An option that controls whether the text’s baseline remains fixed when text needs to shrink to fit in the label.
- [numberOfLines](numberoflines.md) — The maximum number of lines for rendering text.
- [sizingRule](../uiletterformawareadjusting/sizingrule.md) — The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.
