---
title: baseForegroundColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibuttonconfiguration/baseforegroundcolor
source_url: 'https://developer.apple.com/documentation/uikit/uibuttonconfiguration/baseforegroundcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibuttonconfiguration/baseforegroundcolor.json'
content_hash: 'sha256:a5576dd2a2f3c7fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButtonConfiguration](../uibuttonconfiguration.md)

# baseForegroundColor

<sub>Instance Property</sub>

The untransformed color for foreground views.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, strong, readwrite, nullable) UIColor * baseForegroundColor;
```

## Discussion

The button configuration may transform the base color before applying it to foreground views.

## See Also

### Configuring button colors

- [baseBackgroundColor](basebackgroundcolor.md) — The untransformed color for background views.
