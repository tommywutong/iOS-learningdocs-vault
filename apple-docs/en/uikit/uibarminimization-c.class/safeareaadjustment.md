---
title: safeAreaAdjustment
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uibarminimization-c.class/safeareaadjustment
source_url: 'https://developer.apple.com/documentation/uikit/uibarminimization-c.class/safeareaadjustment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarminimization-c.class/safeareaadjustment.json'
content_hash: 'sha256:2f317e544180cf9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarMinimization](../uibarminimization-c.class.md)

# safeAreaAdjustment

<sub>Instance Property</sub>

The safe area adjustment during minimization.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, assign) UIBarMinimizationSafeAreaAdjustment safeAreaAdjustment;
```

## Discussion

Currently, only the navigation bar supports customizing the safe area adjustment.

The default value is `UIBarMinimizationSafeAreaAdjustmentAutomatic`.
