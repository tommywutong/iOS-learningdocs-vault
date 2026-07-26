---
title: macIdiomStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibuttonconfiguration/macidiomstyle
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonconfiguration/macidiomstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonconfiguration/macidiomstyle.json'
content_hash: 'sha256:b627fc7d37e80845'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButtonConfiguration](../uibuttonconfiguration.md)

# macIdiomStyle

<sub>Instance Property</sub>

The style to use when this button appears in macOS.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, assign, readwrite) UIButtonConfigurationMacIdiomStyle macIdiomStyle;
```

## Discussion

Use this property when building your app with Mac Catalyst. The value [UIButtonConfigurationMacIdiomStyleAutomatic](../uibuttonconfigurationmacidiomstyle/uibuttonconfigurationmacidiomstyleautomatic.md) lets the system choose the appropriate style. Select a specific style to force the button to always use that style.

## See Also

### Configuring the appearance on macOS

- [UIButtonConfigurationMacIdiomStyle](../uibuttonconfigurationmacidiomstyle.md) — The button style your app uses when running in macOS.
