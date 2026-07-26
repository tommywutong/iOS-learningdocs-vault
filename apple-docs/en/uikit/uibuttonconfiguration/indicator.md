---
title: indicator
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibuttonconfiguration/indicator
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonconfiguration/indicator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonconfiguration/indicator.json'
content_hash: 'sha256:f9ccb6d38c641fc9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButtonConfiguration](../uibuttonconfiguration.md)

# indicator

<sub>Instance Property</sub>

The style of the indicator that appears on the button.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, assign, readwrite) UIButtonConfigurationIndicator indicator;
```

## Discussion

Use this property to control the style of the indicator that appears on the trailing edge of the button. For example, the following code disables the indicator by setting this style to [UIButtonConfigurationIndicatorNone](../uibuttonconfigurationindicator/uibuttonconfigurationindicatornone.md).

```objc
UIButtonConfiguration *config = UIButtonConfiguration.filledButtonConfiguration;
config.indicator = UIButtonConfigurationIndicatorNone;
```

## See Also

### Configuring the indicator

- [UIButtonConfigurationIndicator](../uibuttonconfigurationindicator.md) — Constants that determine the style of the indicator that appears on a button.
- [indicatorColorTransformer](indicatorcolortransformer.md) — The color transformer for resolving the indicator color.
