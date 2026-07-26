---
title: textToSecondaryTextHorizontalPadding
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontentconfiguration-c.class/texttosecondarytexthorizontalpadding
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-c.class/texttosecondarytexthorizontalpadding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-c.class/texttosecondarytexthorizontalpadding.json'
content_hash: 'sha256:8621dd14b5eb9e63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIListContentConfiguration](../uilistcontentconfiguration-c.class.md)

# textToSecondaryTextHorizontalPadding

<sub>Instance Property</sub>

The minimum horizontal padding between the text and secondary text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) CGFloat textToSecondaryTextHorizontalPadding;
```

## Discussion

This value only applies when there’s both text and secondary text, and they’re in a side-by-side layout that [prefersSideBySideTextAndSecondaryText](../uilistcontentconfiguration-swift.struct/preferssidebysidetextandsecondarytext.md) specifies.

## See Also

### Customizing layout

- [axesPreservingSuperviewLayoutMargins](axespreservingsuperviewlayoutmargins.md) — A Boolean value that detemines whether the content view preserves the layout margins that it inherits from its superview on the horizontal or vertical axes.
- [directionalLayoutMargins](directionallayoutmargins.md) — The margins between the content and the edges of the content view.
- [prefersSideBySideTextAndSecondaryText](preferssidebysidetextandsecondarytext.md) — A Boolean value that determines whether the configuration positions the text and secondary text side by side.
- [imageToTextPadding](imagetotextpadding.md) — The padding between the image and text.
- [textToSecondaryTextVerticalPadding](texttosecondarytextverticalpadding.md) — The vertical padding between the text and secondary text.
