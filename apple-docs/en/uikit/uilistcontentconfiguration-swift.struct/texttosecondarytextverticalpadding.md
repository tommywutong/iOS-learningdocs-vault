---
title: textToSecondaryTextVerticalPadding
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilistcontentconfiguration-swift.struct/texttosecondarytextverticalpadding
source_url: 'https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/texttosecondarytextverticalpadding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilistcontentconfiguration-swift.struct/texttosecondarytextverticalpadding.json'
content_hash: 'sha256:20ec9b681ed1880a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIListContentConfiguration](../uilistcontentconfiguration-swift.struct.md)

# textToSecondaryTextVerticalPadding

<sub>Instance Property</sub>

The vertical padding between the text and secondary text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var textToSecondaryTextVerticalPadding: CGFloat { get set }
```

## Discussion

This value only applies when there’s both text and secondary text, and they’re in a stacked vertical layout.

## See Also

### Customizing layout

- [axesPreservingSuperviewLayoutMargins](axespreservingsuperviewlayoutmargins.md) — A Boolean value that determines whether the content view preserves the layout margins that it inherits from its superview on the horizontal or vertical axes.
- [directionalLayoutMargins](directionallayoutmargins.md) — The margins between the content and the edges of the content view.
- [prefersSideBySideTextAndSecondaryText](preferssidebysidetextandsecondarytext.md) — A Boolean value that determines whether the configuration positions the text and secondary text side by side.
- [imageToTextPadding](imagetotextpadding.md) — The padding between the image and text.
- [textToSecondaryTextHorizontalPadding](texttosecondarytexthorizontalpadding.md) — The minimum horizontal padding between the text and secondary text.
