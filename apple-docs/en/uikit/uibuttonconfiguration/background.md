---
title: background
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibuttonconfiguration/background
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonconfiguration/background'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonconfiguration/background.json'
content_hash: 'sha256:f5cbeb8aede81a52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButtonConfiguration](../uibuttonconfiguration.md)

# background

<sub>Instance Property</sub>

The configuration to customize the button background.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, strong, readwrite) UIBackgroundConfiguration * background;
```

## Discussion

The button lays out foreground configuration elements such as title, subtitle, and image on top of background elements. Use this property for detailed control over the background.

## See Also

### Configuring the button background

- [cornerStyle](cornerstyle.md) — The button style that controls the display behavior of the background corner radius.
- [UIButtonConfigurationCornerStyle](../uibuttonconfigurationcornerstyle.md) — Settings that determine the appearance of the background corner radius.
