---
title: cornerStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibuttonconfiguration/cornerstyle
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonconfiguration/cornerstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonconfiguration/cornerstyle.json'
content_hash: 'sha256:9884efa8937eefe5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButtonConfiguration](../uibuttonconfiguration.md)

# cornerStyle

<sub>Instance Property</sub>

The button style that controls the display behavior of the background corner radius.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, assign, readwrite) UIButtonConfigurationCornerStyle cornerStyle;
```

## Discussion

This property controls the behavior of the [cornerRadius](../uibackgroundconfiguration-c.class/cornerradius.md) you set on the configuration background. The default corner style is [UIButtonConfigurationCornerStyleDynamic](../uibuttonconfigurationcornerstyle/uibuttonconfigurationcornerstyledynamic.md).

## See Also

### Configuring the button background

- [background](background.md) — The configuration to customize the button background.
- [UIButtonConfigurationCornerStyle](../uibuttonconfigurationcornerstyle.md) — Settings that determine the appearance of the background corner radius.
