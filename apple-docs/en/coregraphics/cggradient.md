---
title: CGGradient
framework: Core Graphics
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cggradient
source_url: 'https://developer.apple.com/documentation/coregraphics/cggradient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cggradient.json'
content_hash: 'sha256:c1bbfec478689a26'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGGradient

<sub>Class</sub>

A definition for a smooth transition between colors for drawing radial and axial gradient fills.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CGGradient
```

## Overview

A gradient defines a smooth transition between colors across an area. A `CGGradient` has a color space, two or more colors, and a location for each color. The color space cannot be a pattern or indexed color space, otherwise it can be any Core Graphics color space ([CGColorSpace](cgcolorspace.md)).

Colors can be provided as component values (such as red, green, blue) or as Core Graphics color objects ([CGColor](cgcolor.md)). Component values can vary from 0.0 to 1.0, designating the proportion of the component present in the color.

A location is a normalized value. When it comes time to paint the gradient, Core Graphics maps the normalized location values to the points in coordinate space that you provide.

For more precise control over gradients, see [CGShading](cgshading.md).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating Gradient Instances

- [CGGradientCreateWithColorComponents](<cggradient/init(colorspace_colorcomponents_locations_count_).md>) — Creates a CGGradient object from a color space and the provided color components and locations.
- [CGGradientCreateWithColors](<cggradient/init(colorsspace_colors_locations_).md>) — Creates a gradient object from a color space and the provided color objects and locations.

### Working with Core Foundation Types

- [CGGradientGetTypeID](cggradient/typeid.md) — Returns the Core Foundation type identifier for CGGradient objects.

### Initializers

- [CGGradientCreateWithContentHeadroom](<cggradient/init(headroom_colorspace_colorcomponents_locations_count_).md>)

### Instance Properties

- [CGGradientGetContentHeadroom](cggradient/contentheadroom.md)

## See Also

### Utility and Support Classes

- [CGDataConsumer](cgdataconsumer.md) — An abstraction for data-writing tasks that eliminates the need to manage a raw memory buffer.
- [CGDataProvider](cgdataprovider.md) — An abstraction for data-reading tasks that eliminates the need to manage a raw memory buffer.
- [CGShading](cgshading.md) — A definition for a smooth transition between colors, controlled by a custom function you provide, for drawing radial and axial gradient fills.
- [CGFunction](cgfunction.md) — A general facility for defining and using callback functions.
- [CGPattern](cgpattern.md) — A 2D pattern to be used for drawing graphics paths.
