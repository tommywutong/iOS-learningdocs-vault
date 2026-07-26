---
title: alphaInfoMask
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+（27.0 起废弃）, iPadOS 7.0+（27.0 起废弃）, Mac Catalyst 7.0+（27.0 起废弃）, macOS 10.9+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/coregraphics/cgbitmapinfo/alphainfomask
source_url: 'https://developer.apple.com/documentation/coregraphics/cgbitmapinfo/alphainfomask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgbitmapinfo/alphainfomask.json'
content_hash: 'sha256:b519911bfa866fa8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGBitmapInfo](../cgbitmapinfo.md)

# alphaInfoMask

<sub>Type Property</sub>

The alpha information mask. Use this to extract alpha information that specifies whether a bitmap contains an alpha channel and how the alpha channel is generated.

> [!warning] Deprecated
> Use .alpha instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var alphaInfoMask: CGBitmapInfo { get }
```

## See Also

### Constants

- [kCGBitmapFloatComponents](floatcomponents.md) — The components of a bitmap are floating-point values. _(deprecated)_
- [byteOrderMask](byteordermask.md) — The byte ordering of pixel formats. _(deprecated)_
- [kCGBitmapByteOrderDefault](byteorderdefault.md) — The default byte order. _(deprecated)_
- [kCGBitmapByteOrder16Little](byteorder16little.md) — 16-bit, little endian format. _(deprecated)_
- [kCGBitmapByteOrder32Little](byteorder32little.md) — 32-bit, little endian format. _(deprecated)_
- [kCGBitmapByteOrder16Big](byteorder16big.md) — 16-bit, big endian format. _(deprecated)_
- [kCGBitmapByteOrder32Big](byteorder32big.md) — 32-bit, big endian format. _(deprecated)_
- [floatInfoMask](floatinfomask.md) _(deprecated)_
