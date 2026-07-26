---
title: axesPreservingSuperviewLayoutMargins
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontentconfiguration-c.class/axespreservingsuperviewlayoutmargins
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-c.class/axespreservingsuperviewlayoutmargins'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-c.class/axespreservingsuperviewlayoutmargins.json'
content_hash: 'sha256:6126dedf876a8d13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIListContentConfiguration](../uilistcontentconfiguration-c.class.md)

# axesPreservingSuperviewLayoutMargins

<sub>Instance Property</sub>

A Boolean value that detemines whether the content view preserves the layout margins that it inherits from its superview on the horizontal or vertical axes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) UIAxis axesPreservingSuperviewLayoutMargins;
```

## Discussion

By default, the content view preserves the layout margins of its superview on [UIAxisBoth](../uiaxis/both.md) axes.

## See Also

### Customizing layout

- [directionalLayoutMargins](directionallayoutmargins.md) — The margins between the content and the edges of the content view.
- [prefersSideBySideTextAndSecondaryText](preferssidebysidetextandsecondarytext.md) — A Boolean value that determines whether the configuration positions the text and secondary text side by side.
- [imageToTextPadding](imagetotextpadding.md) — The padding between the image and text.
- [textToSecondaryTextHorizontalPadding](texttosecondarytexthorizontalpadding.md) — The minimum horizontal padding between the text and secondary text.
- [textToSecondaryTextVerticalPadding](texttosecondarytextverticalpadding.md) — The vertical padding between the text and secondary text.
