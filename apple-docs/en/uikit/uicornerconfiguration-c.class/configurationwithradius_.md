---
title: 'configurationWithRadius:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicornerconfiguration-c.class/configurationwithradius:'
source_url: 'https://developer.apple.com/documentation/uikit/uicornerconfiguration-c.class/configurationwithradius:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicornerconfiguration-c.class/configurationwithradius%3A.json'
content_hash: 'sha256:075441ff13c5dd12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICornerConfiguration](../uicornerconfiguration-c.class.md)

# configurationWithRadius:

<sub>Type Method</sub>

A configuration that applies the given radius independently to all corners.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) configurationWithRadius:(UICornerRadius *) radius;
```

## Discussion

When used with a container concentric radius, this allows each individual corner to resolve to different radii.

## See Also

### Configuring independent corners

- [configurationWithTopLeftRadius:topRightRadius:bottomLeftRadius:bottomRightRadius:](configurationwithtopleftradius_toprightradius_bottomleftradius_bottomrightradius_.md) — A configuration with independent radii for each corner.
