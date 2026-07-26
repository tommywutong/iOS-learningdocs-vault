---
title: CIColor
framework: Core Image
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicolor
source_url: 'https://developer.apple.com/documentation/coreimage/cicolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolor.json'
content_hash: 'sha256:5c450bc05c5dd037'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIColor

<sub>Class</sub>

The Core Image class that defines a color object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CIColor
```

## Overview

Use `CIColor` instances in conjunction with other Core Image classes, such as [CIFilter](cifilter-swift.class.md) and [CIKernel](cikernel.md). Many of the built-in Core Image filters have one or more `CIColor` inputs that you can set to affect the filter’s behavior.

### Color Model

A color is defined as a N-dimensional model where each dimension’s color component is represented by intensity values. A color component may also be referred to as a color channel. An RGB color model, for example, is three-dimensional and the red, green, and blue component intensities define each unique color.

### Color Space

A color is also defined by a color space that locates the axes of N-dimensional model within the greater volume of human perceivable colors.  Core Image uses `CGColorSpace` instances to specify a variety of different color spaces such as sRGB, P3, BT.2020, etc. The `CGColorSpace` also defines if the color space is coded linearly or in a non-linear perceptual curve. (For more information on `CGColorSpace` see [CGColorSpace](../coregraphics/cgcolorspace.md))

### Color Range

Standard dynamic range (SDR) color color component values range from `0.0` to `1.0`, with `0.0` representing an 0% of that component and `1.0` representing 100%. In contrast, high dynamic range (HDR) color values can be less than `0.0` (for more saturation) or greater than `1.0` (for more brightness).

### Color Opacity

`CIColor` instances also have an alpha component, which represents the opacity of the color, with 0.0 meaning completely transparent and 1.0 meaning completely opaque. If a color does not have an explicit alpha component, Core Image assumes that the alpha component equals 1.0. With `CIColor` that color components values are not premultiplied. So for example, a semi-transparent pure red `CIColor` is represented by RGB `1.0,0.0,0.0` and A `0.5`.  In contrast color components values in [CIImage](ciimage.md) buffers or read in [CIKernel](cikernel.md) samplers are premultiplied by default.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing Color Objects

- [- initWithCGColor:](<cicolor/init(cgcolor_)-1hzk4.md>) — Create a Core Image color object with a Core Graphics color object.
- [- initWithColor:](<cicolor/init(color_).md>)
- [- initWithRed:green:blue:alpha:](<cicolor/init(red_green_blue_alpha_).md>) — Initialize a Core Image color object in the sRGB color space with the specified red, green, blue, and alpha component values.

### Creating Color Objects

- [+ colorWithRed:green:blue:](<cicolor/init(red_green_blue_).md>) — Create a Core Image color object in the sRGB color space with the specified red, green, and blue component values.
- [+ colorWithString:](<cicolor/init(string_).md>) — Create a Core Image color object in the sRGB color space using a string containing the RGBA color component values.
- [+ colorWithRed:green:blue:colorSpace:](<cicolor/init(red_green_blue_colorspace_)-2og6y.md>) — Create a Core Image color object with the specified red, green, and blue component values as measured in the specified color space.
- [+ colorWithRed:green:blue:alpha:colorSpace:](<cicolor/init(red_green_blue_alpha_colorspace_)-5mvff.md>) — Create a Core Image color object with the specified red, green, blue, and alpha component values as measured in the specified color space.

### Getting Color Components

- [colorSpace](cicolor/colorspace.md) — Returns the `CGColorSpace` associated with the color
- [components](cicolor/components.md) — Return a pointer to an array of `CGFloat` values including alpha.
- [numberOfComponents](cicolor/numberofcomponents.md) — Returns the color components of the color including alpha.
- [red](cicolor/red-swift.property.md) — Returns the unpremultiplied red component of the color.
- [green](cicolor/green-swift.property.md) — Returns the unpremultiplied green component of the color.
- [blue](cicolor/blue-swift.property.md) — Returns the unpremultiplied blue component of the color.
- [alpha](cicolor/alpha.md) — Returns the alpha value of the color.
- [stringRepresentation](cicolor/stringrepresentation.md) — Returns a formatted string with the unpremultiplied color and alpha components of the color.

### Creating a CIColor Object with Preset Components

- [blackColor](cicolor/black.md) — Returns a singleton Core Image color instance in the sRGB color space with RGB values `0,0,0` and alpha value `1`.
- [blueColor](cicolor/blue-swift.type.property.md) — Returns a singleton Core Image color instance in the sRGB color space with RGB values `0,0,1` and alpha value `1`.
- [clearColor](cicolor/clear.md) — Returns a singleton Core Image color instance in the sRGB color space with RGB values `0,0,0` and alpha value `0`.
- [cyanColor](cicolor/cyan.md) — Returns a singleton Core Image color instance in the sRGB color space with RGB values `0,1,1` and alpha value `1`.
- [grayColor](cicolor/gray.md) — Returns a singleton Core Image color instance in the sRGB color space with RGB values `0.5,0.5,0.5` and alpha value `1`.
- [greenColor](cicolor/green-swift.type.property.md) — Returns a singleton Core Image color instance in the sRGB color space with RGB values `0,1,0` and alpha value `1`.
- [magentaColor](cicolor/magenta.md) — Returns a singleton Core Image color instance in the sRGB color space with RGB values `1,0,1` and alpha value `1`.
- [redColor](cicolor/red-swift.type.property.md) — Returns a singleton Core Image color instance in the sRGB color space with RGB values `1,0,0` and alpha value `1`.
- [whiteColor](cicolor/white.md) — Returns a singleton Core Image color instance in the sRGB color space with RGB values `1,1,1` and alpha value `1`.
- [yellowColor](cicolor/yellow.md) — Returns a singleton Core Image color instance in the sRGB color space with RGB values `1,1,0` and alpha value `1`.

### Initializers

- [init(CGColor:)](<cicolor/init(cgcolor_)-2n26w.md>)
- [init(CGColor:)](<cicolor/init(cgcolor_)-2nx98.md>)
- [init(coder:)](<cicolor/init(coder_).md>)
- [- initWithRed:green:blue:alpha:colorSpace:](<cicolor/init(red_green_blue_alpha_colorspace_)-8yg0z.md>) — Initialize a Core Image color object with the specified red, green, and blue component values as measured in the specified color space.
- [- initWithRed:green:blue:colorSpace:](<cicolor/init(red_green_blue_colorspace_)-6d8o.md>) — Initialize a Core Image color object with the specified red, green, and blue component values as measured in the specified color space.

## See Also

### Filters

- [CIFilter](cifilter-swift.class.md) — An image processor that produces an image by manipulating one or more input images or by generating new image data.
- [CIRAWFilter](cirawfilter.md) — A filter subclass that produces an image by manipulating RAW image sensor data from a digital camera or scanner.
- [CIVector](civector.md) — The Core Image class that defines a vector object.
