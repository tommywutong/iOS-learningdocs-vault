---
title: sizingRule
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiletterformawareadjusting/sizingrule
source_url: 'https://developer.apple.com/documentation/uikit/uiletterformawareadjusting/sizingrule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiletterformawareadjusting/sizingrule.json'
content_hash: 'sha256:6cbec04afeed2ba8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILetterformAwareAdjusting](../uiletterformawareadjusting.md)

# sizingRule

<sub>Instance Property</sub>

The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var sizingRule: UILetterformAwareSizingRule { get set }
```

## Discussion

For more information on sizing behaviors, see [UILetterformAwareAdjusting](../uiletterformawareadjusting.md).

## See Also

### Sizing the label’s text

- [adjustsFontSizeToFitWidth](../uilabel/adjustsfontsizetofitwidth.md) — A Boolean value that determines whether the label reduces the text’s font size to fit the title string into the label’s bounding rectangle.
- [allowsDefaultTighteningForTruncation](../uilabel/allowsdefaulttighteningfortruncation.md) — A Boolean value that determines whether the label tightens text before truncating.
- [baselineAdjustment](../uilabel/baselineadjustment.md) — An option that controls whether the text’s baseline remains fixed when text needs to shrink to fit in the label.
- [minimumScaleFactor](../uilabel/minimumscalefactor.md) — The minimum scale factor for the label’s text.
- [numberOfLines](../uilabel/numberoflines.md) — The maximum number of lines for rendering text.
