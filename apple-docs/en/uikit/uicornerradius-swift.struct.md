---
title: UICornerRadius
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicornerradius-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uicornerradius-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicornerradius-swift.struct.json'
content_hash: 'sha256:baafd57eef586e31'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICornerRadius

<sub>Structure</sub>

A type that represents the radius the system uses to round a corner.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UICornerRadius
```

## Relationships

- **Conforms To**: [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [ExpressibleByFloatLiteral](../swift/expressiblebyfloatliteral.md), [ExpressibleByIntegerLiteral](../swift/expressiblebyintegerliteral.md), [Hashable](../swift/hashable.md)

## Topics

### Defining a radius

- [containerConcentric(minimum:)](<uicornerradius-swift.struct/containerconcentric(minimum_).md>) — A dynamic corner radius calculated using the geometry of the view and its container limited to a minimum radius.
- [fixed(_:)](<uicornerradius-swift.struct/fixed(__).md>) — Creates a radius that represents a fixed corner radius in points.

## See Also

### Configuring a view’s corners

- [cornerConfiguration](uiview/cornerconfiguration-7l0ja.md) — A configuration that defines the corners of the view.
- [UICornerConfiguration](uicornerconfiguration-swift.struct.md) — A configuration that defines how corner radii are mapped to the corners of a rectangle.
- [- effectiveRadiusForCorner:](<uiview/effectiveradius(corner_).md>) — Returns the effective radius for the corner you provide, calculated using the view’s current corner configuration.
