---
title: CGInterpolationQuality
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cginterpolationquality
source_url: 'https://developer.apple.com/documentation/coregraphics/cginterpolationquality'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cginterpolationquality.json'
content_hash: 'sha256:f754c9601ab628e7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGInterpolationQuality

<sub>Enumeration</sub>

Levels of interpolation quality for rendering an image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CGInterpolationQuality
```

## Overview

You use the function [CGContextSetInterpolationQuality](cgcontextsetinterpolationquality.md) to set the interpolation quality in a graphics context.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGInterpolationDefault](cginterpolationquality/default.md) — The default level of quality.
- [kCGInterpolationNone](cginterpolationquality/none.md) — No interpolation.
- [kCGInterpolationLow](cginterpolationquality/low.md) — A low level of interpolation quality. This setting may speed up image rendering.
- [kCGInterpolationMedium](cginterpolationquality/medium.md) — A medium level of interpolation quality. This setting is slower than the low setting but faster than the high setting.
- [kCGInterpolationHigh](cginterpolationquality/high.md) — A high level of interpolation quality. This setting may slow down image rendering.

### Initializers

- [init(rawValue:)](<cginterpolationquality/init(rawvalue_).md>)

## See Also

### Drawing Images and PDF Content

- [draw(_:in:byTiling:)](<cgcontext/draw(__in_bytiling_).md>) — Draws an image in the specified area.
- [CGContextDrawPDFPage](<cgcontext/drawpdfpage(__).md>) — Draws the content of a PDF page into the current graphics context.
- [CGContextGetInterpolationQuality](cgcontext/interpolationquality.md) — Returns the current level of interpolation quality for a graphics context.
