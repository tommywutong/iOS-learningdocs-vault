---
title: UIColor
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicolor
source_url: 'https://developer.apple.com/documentation/uikit/uicolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor.json'
content_hash: 'sha256:7bca1a670a04e655'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIColor

<sub>Class</sub>

An object that stores color data and sometimes opacity.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class UIColor
```

## Overview

Use color to customize your app’s appearance, communicate status, and help people visualize data. To learn more about using color in your apps, see [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/foundations/color/).

[UIColor](uicolor.md) provides a list of class properties that create adaptable and fixed colors such as blue, green, purple, and more. [UIColor](uicolor.md) also offers properties to specify system-provided colors for UI elements such as labels, text, and buttons. You can create color objects by specifying color component values such as RGB, hue, and saturation. You can also create colors from other color objects and even create a pattern-based color from an image.

> [!important] Important
> Most developers have no need to subclass [UIColor](uicolor.md). The only time subclassing might be necessary is if you require support for additional color spaces or color models. If you do subclass, the properties and methods you add must be safe to use from multiple threads.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSItemProviderReading](../foundation/nsitemproviderreading.md), [NSItemProviderWriting](../foundation/nsitemproviderwriting.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting existing colors

- [UI element colors](ui-element-colors.md) — Choose colors for UI elements such as labels, text, backgrounds, and links.
- [Standard colors](standard-colors.md) — Define standard color objects for specific shades, such as red, blue, green, black, white, and more.
- [Color creation](color-creation.md) — Load colors from asset catalogs and create colors from raw component values.

### Applying the color to the drawing environment

- [Customizing drawings](customizing-drawings.md) — Create custom colors and patterns for drawing in your app.
- [- set](<uicolor/set().md>) — Sets the color of subsequent stroke and fill operations to the color that the receiver represents.
- [- setFill](<uicolor/setfill().md>) — Sets the color of subsequent fill operations to the color that the receiver represents.
- [- setStroke](<uicolor/setstroke().md>) — Sets the color of subsequent stroke operations to the color that the receiver represents.

### Getting the color information

- [Determining color values with color spaces](determining-color-values-with-color-spaces.md) — Change the system’s interpretation of a color value for display by selecting a color space.
- [CGColor](uicolor/cgcolor.md) — The Quartz color that corresponds to the color object.
- [CIColor](uicolor/cicolor.md) — The Core Image color that corresponds to the color object.
- [- getHue:saturation:brightness:alpha:](<uicolor/gethue(__saturation_brightness_alpha_).md>) — Returns the components that form the color in the HSB color space.
- [- getRed:green:blue:alpha:](<uicolor/getred(__green_blue_alpha_).md>) — Returns the components that form the color in the RGB color space.
- [- getWhite:alpha:](<uicolor/getwhite(__alpha_).md>) — Returns the grayscale components of the color.
- [linearExposure](uicolor/linearexposure.md) — The linear brightness multiplier that was applied when generating this color. Colors created with an exposure by UIColor create CGColors that are tagged with a contentHeadroom value. While CGColors created without a contentHeadroom tag will return 0 from CGColorGetHeadroom, UIColors generated in a similar fashion return a linearExposure of 1.0.
- [accessibilityName](uicolor/accessibilityname.md) — A localized description of the color for accessibility attributes.

### Resolving a dynamically generated color

- [- resolvedColorWithTraitCollection:](<uicolor/resolvedcolor(with_).md>) — Returns the version of the current color that results from the specified traits.

### Working with color prominence

- [prominence](uicolor/prominence-swift.property.md)
- [- colorWithProminence:](<uicolor/withprominence(__).md>) — Returns the version of the current color that results from applying the specified prominence.
- [Prominence](uicolor/prominence-swift.enum.md) — A type that indicates the prominence of a color in the interface.

### Working with high dynamic range (HDR) colors

- [- colorByApplyingContentHeadroom:](<uicolor/applyingcontentheadroom(__).md>) — Reinterpret the color by applying a new `contentHeadroom` without changing the color components. Changing the `contentHeadroom` redefines the color relative to a different peak white, changing its behavior under tone mapping and the result of calling `standardDynamicRangeColor`. The new color will have a `contentHeadroom` \>= 1.0.
- [standardDynamicRangeColor](uicolor/standarddynamicrange.md) — In some cases it is useful to recover the color that was base SDR color that was exposed to generate the given HDR color. If a color’s `linearExposure` is \>1, then this will return the base SDR color.

### Initializers

- [init(CGColor:)](<uicolor/init(cgcolor_)-58l83.md>)
- [init(CGColor:)](<uicolor/init(cgcolor_)-9d9vs.md>)
- [init(CIColor:)](<uicolor/init(cicolor_)-2b5ik.md>)
- [init(CIColor:)](<uicolor/init(cicolor_)-5fqhu.md>)
- [init(coder:)](<uicolor/init(coder_).md>)
- [+ colorNamed:inBundle:compatibleWithTraitCollection:](<uicolor/init(named_in_compatiblewith_).md>)

### Default Implementations

- [UIColor Implementations](uicolor/uicolor-implementations.md)
