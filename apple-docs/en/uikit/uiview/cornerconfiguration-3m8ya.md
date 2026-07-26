---
title: cornerConfiguration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/cornerconfiguration-3m8ya
source_url: 'https://developer.apple.com/documentation/uikit/uiview/cornerconfiguration-3m8ya'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/cornerconfiguration-3m8ya.json'
content_hash: 'sha256:19e1995d1802bde3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# cornerConfiguration

<sub>Instance Property</sub>

A configuration that defines the corners of the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy, nonnull) UICornerConfiguration * cornerConfiguration;
```

## Discussion

For more information on how to configure view corners, see [UICornerConfiguration](../uicornerconfiguration-c.class.md).

## See Also

### Configuring a view’s corners

- [UICornerConfiguration](../uicornerconfiguration-c.class.md) — A configuration that defines how corner radii are mapped to the corners of a rectangle.
- [UICornerRadius](../uicornerradius-c.class.md) — A type that represents the radius the system uses to round a corner.
- [- effectiveRadiusForCorner:](<effectiveradius(corner_).md>) — Returns the effective radius for the corner you provide, calculated using the view’s current corner configuration.
