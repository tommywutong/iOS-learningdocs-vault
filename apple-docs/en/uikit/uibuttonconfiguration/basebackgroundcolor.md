---
title: baseBackgroundColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibuttonconfiguration/basebackgroundcolor
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonconfiguration/basebackgroundcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonconfiguration/basebackgroundcolor.json'
content_hash: 'sha256:b91e08d3c88c32f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButtonConfiguration](../uibuttonconfiguration.md)

# baseBackgroundColor

<sub>Instance Property</sub>

The untransformed color for background views.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, strong, readwrite, nullable) UIColor * baseBackgroundColor;
```

## Discussion

The button configuration may transform the base color before applying it to background elements.

## See Also

### Configuring button colors

- [baseForegroundColor](baseforegroundcolor.md) — The untransformed color for foreground views.
