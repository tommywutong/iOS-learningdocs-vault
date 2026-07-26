---
title: UICornerRadius
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicornerradius-c.class
source_url: 'https://developer.apple.com/documentation/uikit/uicornerradius-c.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicornerradius-c.class.json'
content_hash: 'sha256:babc7852096372f3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICornerRadius

<sub>Class</sub>

A type that represents the radius the system uses to round a corner.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UICornerRadius : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSCopying](../foundation/nscopying.md)

## Topics

### Defining a radius

- [containerConcentricRadius](uicornerradius-c.class/containerconcentricradius.md) — A dynamic corner radius calculated using the geometry of the view and its container.
- [containerConcentricRadiusWithMinimum:](uicornerradius-c.class/containerconcentricradiuswithminimum_.md) — A dynamic corner radius calculated using the geometry of the view and its container limited to a minimum radius.
- [fixedRadius:](uicornerradius-c.class/fixedradius_.md) — A fixed corner radius in points.

## See Also

### Configuring a view’s corners

- [cornerConfiguration](uiview/cornerconfiguration-3m8ya.md) — A configuration that defines the corners of the view.
- [UICornerConfiguration](uicornerconfiguration-c.class.md) — A configuration that defines how corner radii are mapped to the corners of a rectangle.
- [- effectiveRadiusForCorner:](<uiview/effectiveradius(corner_).md>) — Returns the effective radius for the corner you provide, calculated using the view’s current corner configuration.
