---
title: baselineAdjustment
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilabel/baselineadjustment
source_url: 'https://developer.apple.com/documentation/uikit/uilabel/baselineadjustment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilabel/baselineadjustment.json'
content_hash: 'sha256:0ff0e6e4f122e9df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILabel](../uilabel.md)

# baselineAdjustment

<sub>Instance Property</sub>

An option that controls whether the text’s baseline remains fixed when text needs to shrink to fit in the label.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var baselineAdjustment: UIBaselineAdjustment { get set }
```

## Discussion

If [adjustsFontSizeToFitWidth](adjustsfontsizetofitwidth.md) is [true](../../swift/true.md), this property controls the behavior of the text baselines in situations where the text needs the font size adjusted in order to fit. The default value of this property is [UIBaselineAdjustmentAlignBaselines](../uibaselineadjustment/alignbaselines.md). This property is effective only when the [numberOfLines](numberoflines.md) is `1`.

## See Also

### Sizing the label’s text

- [adjustsFontSizeToFitWidth](adjustsfontsizetofitwidth.md) — A Boolean value that determines whether the label reduces the text’s font size to fit the title string into the label’s bounding rectangle.
- [allowsDefaultTighteningForTruncation](allowsdefaulttighteningfortruncation.md) — A Boolean value that determines whether the label tightens text before truncating.
- [minimumScaleFactor](minimumscalefactor.md) — The minimum scale factor for the label’s text.
- [numberOfLines](numberoflines.md) — The maximum number of lines for rendering text.
- [sizingRule](../uiletterformawareadjusting/sizingrule.md) — The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.
