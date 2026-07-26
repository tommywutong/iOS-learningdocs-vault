---
title: navigationBarMinimization
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/navigationbarminimization-15u99
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/navigationbarminimization-15u99'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/navigationbarminimization-15u99.json'
content_hash: 'sha256:36bb89b4e92545ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# navigationBarMinimization

<sub>Instance Property</sub>

The minimization configuration for the navigation bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, readwrite) UIBarMinimization * navigationBarMinimization;
```

## Discussion

Set the properties of this configuration to control how the navigation bar minimizes in response to scrolling. When the navigation bar minimizes, an integrated top tab bar will also minimize.
