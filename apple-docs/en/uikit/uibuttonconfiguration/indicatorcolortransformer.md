---
title: indicatorColorTransformer
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibuttonconfiguration/indicatorcolortransformer
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonconfiguration/indicatorcolortransformer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonconfiguration/indicatorcolortransformer.json'
content_hash: 'sha256:88479de15fdbb3df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButtonConfiguration](../uibuttonconfiguration.md)

# indicatorColorTransformer

<sub>Instance Property</sub>

The color transformer for resolving the indicator color.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, readwrite, nullable) UIConfigurationColorTransformer indicatorColorTransformer;
```

## Discussion

Use this color transformer to set a custom color for [indicator](indicator.md). For example, the following code uses a grayscale color for the indicator instead of the default color.

```objc
UIButtonConfiguration *config = UIButtonConfiguration.filledButtonConfiguration;
config.indicatorColorTransformer = UIConfigurationColorTransformerGrayscale;
```

## See Also

### Configuring the indicator

- [indicator](indicator.md) — The style of the indicator that appears on the button.
- [UIButtonConfigurationIndicator](../uibuttonconfigurationindicator.md) — Constants that determine the style of the indicator that appears on a button.
