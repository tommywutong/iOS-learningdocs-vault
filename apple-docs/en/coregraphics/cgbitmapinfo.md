---
title: CGBitmapInfo
framework: Core Graphics
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgbitmapinfo
source_url: 'https://developer.apple.com/documentation/coregraphics/cgbitmapinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgbitmapinfo.json'
content_hash: 'sha256:c4c5c58f44eb30ac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGBitmapInfo

<sub>Structure</sub>

Component information for a bitmap image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CGBitmapInfo
```

## Overview

Applications that store pixel data in memory using ARGB format must take care in how they read data. If the code is not written correctly, it’s possible to misread the data which leads to colors or alpha that appear wrong. The byte order constants specify the byte ordering of pixel formats. To specify byte ordering, use a bitwise OR operator to combine the appropriate constant with the `bitmapInfo` parameter.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [alphaInfoMask](cgbitmapinfo/alphainfomask.md) — The alpha information mask. Use this to extract alpha information that specifies whether a bitmap contains an alpha channel and how the alpha channel is generated. _(deprecated)_
- [kCGBitmapFloatComponents](cgbitmapinfo/floatcomponents.md) — The components of a bitmap are floating-point values. _(deprecated)_
- [byteOrderMask](cgbitmapinfo/byteordermask.md) — The byte ordering of pixel formats. _(deprecated)_
- [kCGBitmapByteOrderDefault](cgbitmapinfo/byteorderdefault.md) — The default byte order. _(deprecated)_
- [kCGBitmapByteOrder16Little](cgbitmapinfo/byteorder16little.md) — 16-bit, little endian format. _(deprecated)_
- [kCGBitmapByteOrder32Little](cgbitmapinfo/byteorder32little.md) — 32-bit, little endian format. _(deprecated)_
- [kCGBitmapByteOrder16Big](cgbitmapinfo/byteorder16big.md) — 16-bit, big endian format. _(deprecated)_
- [kCGBitmapByteOrder32Big](cgbitmapinfo/byteorder32big.md) — 32-bit, big endian format. _(deprecated)_
- [floatInfoMask](cgbitmapinfo/floatinfomask.md) _(deprecated)_

### Initializers

- [init(rawValue:)](<cgbitmapinfo/init(rawvalue_).md>)
- [init(_:)](<cgbitmapinfo/init(__).md>) _(deprecated)_
- [init(alpha:component:byteOrder:)](<cgbitmapinfo/init(alpha_component_byteorder_).md>)
- [init(alpha:component:byteOrder:pixelFormat:)](<cgbitmapinfo/init(alpha_component_byteorder_pixelformat_).md>)
- [init(arrayLiteral:)](<cgbitmapinfo/init(arrayliteral_).md>) _(deprecated)_

### Instance Properties

- [alpha](cgbitmapinfo/alpha.md)
- [byteOrder](cgbitmapinfo/byteorder.md)
- [component](cgbitmapinfo/component.md)
- [isEmpty](cgbitmapinfo/isempty.md) _(deprecated)_
- [pixelFormat](cgbitmapinfo/pixelformat.md)

### Instance Methods

- [contains(_:)](<cgbitmapinfo/contains(__).md>) _(deprecated)_
- [formIntersection(_:)](<cgbitmapinfo/formintersection(__).md>) _(deprecated)_
- [formSymmetricDifference(_:)](<cgbitmapinfo/formsymmetricdifference(__).md>) _(deprecated)_
- [formUnion(_:)](<cgbitmapinfo/formunion(__).md>) _(deprecated)_
- [insert(_:)](<cgbitmapinfo/insert(__).md>) _(deprecated)_
- [intersection(_:)](<cgbitmapinfo/intersection(__).md>) _(deprecated)_
- [isDisjoint(with:)](<cgbitmapinfo/isdisjoint(with_).md>) _(deprecated)_
- [isSubset(of:)](<cgbitmapinfo/issubset(of_).md>) _(deprecated)_
- [isSuperset(of:)](<cgbitmapinfo/issuperset(of_).md>) _(deprecated)_
- [remove(_:)](<cgbitmapinfo/remove(__).md>) _(deprecated)_
- [subtract(_:)](<cgbitmapinfo/subtract(__).md>) _(deprecated)_
- [subtracting(_:)](<cgbitmapinfo/subtracting(__).md>) _(deprecated)_
- [symmetricDifference(_:)](<cgbitmapinfo/symmetricdifference(__).md>) _(deprecated)_
- [union(_:)](<cgbitmapinfo/union(__).md>) _(deprecated)_
- [update(with:)](<cgbitmapinfo/update(with_).md>) _(deprecated)_

## See Also

### Examining an image

- [CGImageIsMask](cgimage/ismask.md) — Returns whether a bitmap image is an image mask.
- [CGImageGetWidth](cgimage/width.md) — Returns the width of a bitmap image, in pixels.
- [CGImageGetHeight](cgimage/height.md) — Returns the height of a bitmap image.
- [CGImageGetBitsPerComponent](cgimage/bitspercomponent.md) — Returns the number of bits allocated for a single color component of a bitmap image.
- [CGImageGetBitsPerPixel](cgimage/bitsperpixel.md) — Returns the number of bits allocated for a single pixel in a bitmap image.
- [CGImageGetBytesPerRow](cgimage/bytesperrow.md) — Returns the number of bytes allocated for a single row of a bitmap image.
- [CGImageGetColorSpace](cgimage/colorspace.md) — Return the color space for a bitmap image.
- [CGImageGetAlphaInfo](cgimage/alphainfo.md) — Returns the alpha channel information for a bitmap image.
- [CGImageAlphaInfo](cgimagealphainfo.md) — Storage options for alpha component data.
- [CGImageGetDataProvider](cgimage/dataprovider.md) — Returns the data provider for a bitmap image or image mask.
- [CGImageGetDecode](cgimage/decode.md) — Returns the decode array for a bitmap image.
- [CGImageGetShouldInterpolate](cgimage/shouldinterpolate.md) — Returns the interpolation setting for a bitmap image.
- [CGImageGetRenderingIntent](cgimage/renderingintent.md) — Returns the rendering intent setting for a bitmap image.
- [CGImageGetBitmapInfo](cgimage/bitmapinfo.md) — Returns the bitmap information for a bitmap image.
- [CGImageGetUTType](cgimage/uttype.md) — The Universal Type Identifier for the image.
