---
title: restorationBehavior
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uibarminimization-c.class/restorationbehavior
source_url: 'https://developer.apple.com/documentation/uikit/uibarminimization-c.class/restorationbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarminimization-c.class/restorationbehavior.json'
content_hash: 'sha256:8bb1c545d5153518'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarMinimization](../uibarminimization-c.class.md)

# restorationBehavior

<sub>Instance Property</sub>

The restoration behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, assign) UIBarMinimizationRestorationBehavior restorationBehavior;
```

## Discussion

Use this property alongside [minimizationBehavior](minimizationbehavior.md) to control when a minimized navigation bar restores. By default the bar restores when the user reverses scroll direction; with `UIBarMinimizationRestorationBehaviorAtScrollEdge`, the bar instead restores only when the scroll view’s content reaches the scroll edge. Currently only honored in combination with `UIBarMinimizationBehaviorOnScrollDown`.

The default value is `UIBarMinimizationRestorationBehaviorAutomatic`.
