---
title: directionalLayoutMargins
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontentconfiguration-c.class/directionallayoutmargins
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-c.class/directionallayoutmargins'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-c.class/directionallayoutmargins.json'
content_hash: 'sha256:128ecd06c21396b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIListContentConfiguration](../uilistcontentconfiguration-c.class.md)

# directionalLayoutMargins

<sub>Instance Property</sub>

The margins between the content and the edges of the content view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) NSDirectionalEdgeInsets directionalLayoutMargins;
```

## Discussion

When you preserve superview layout margins on one or both axes, this value specifies the minimum margins. The inherited margins may be larger.

By default, the content view preserves the layout margins of its superview on both axes. You can customize this behavior by changing [axesPreservingSuperviewLayoutMargins](../uilistcontentconfiguration-swift.struct/axespreservingsuperviewlayoutmargins.md).

## See Also

### Customizing layout

- [axesPreservingSuperviewLayoutMargins](axespreservingsuperviewlayoutmargins.md) — A Boolean value that detemines whether the content view preserves the layout margins that it inherits from its superview on the horizontal or vertical axes.
- [prefersSideBySideTextAndSecondaryText](preferssidebysidetextandsecondarytext.md) — A Boolean value that determines whether the configuration positions the text and secondary text side by side.
- [imageToTextPadding](imagetotextpadding.md) — The padding between the image and text.
- [textToSecondaryTextHorizontalPadding](texttosecondarytexthorizontalpadding.md) — The minimum horizontal padding between the text and secondary text.
- [textToSecondaryTextVerticalPadding](texttosecondarytextverticalpadding.md) — The vertical padding between the text and secondary text.
