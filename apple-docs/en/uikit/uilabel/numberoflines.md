---
title: numberOfLines
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilabel/numberoflines
source_url: 'https://developer.apple.com/documentation/uikit/uilabel/numberoflines'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilabel/numberoflines.json'
content_hash: 'sha256:17bfbdf8df4e06dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UILabel](../uilabel.md)

# numberOfLines

<sub>Instance Property</sub>

The maximum number of lines for rendering text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var numberOfLines: Int { get set }
```

## Discussion

This property controls the maximum number of lines to use in order to fit the label’s text into its bounding rectangle. The default value for this property is `1`. To remove any maximum limit, and use as many lines as needed, set the value of this property to `0`.

If you constrain your text using this property, the label truncates any text that doesn’t fit within the maximum number of lines and inside the bounding rectangle. To specify which part of the text the label should truncate, set the [lineBreakMode](linebreakmode.md) property.

When the [- sizeToFit](<../uiview/sizetofit().md>) method resizes a label, resizing takes into account the value stored in this property. For example, if the number of lines is `3`, the [- sizeToFit](<../uiview/sizetofit().md>) method resizes the label so that it’s big enough to display three lines of text in the current font.

## See Also

### Related Documentation

- [- sizeToFit](<../uiview/sizetofit().md>) — Resizes and moves the receiver view so it just encloses its subviews.
- [enabled](isenabled.md) — A Boolean value that determines whether the label draws its text in an enabled state.

### Sizing the label’s text

- [adjustsFontSizeToFitWidth](adjustsfontsizetofitwidth.md) — A Boolean value that determines whether the label reduces the text’s font size to fit the title string into the label’s bounding rectangle.
- [allowsDefaultTighteningForTruncation](allowsdefaulttighteningfortruncation.md) — A Boolean value that determines whether the label tightens text before truncating.
- [baselineAdjustment](baselineadjustment.md) — An option that controls whether the text’s baseline remains fixed when text needs to shrink to fit in the label.
- [minimumScaleFactor](minimumscalefactor.md) — The minimum scale factor for the label’s text.
- [sizingRule](../uiletterformawareadjusting/sizingrule.md) — The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.
