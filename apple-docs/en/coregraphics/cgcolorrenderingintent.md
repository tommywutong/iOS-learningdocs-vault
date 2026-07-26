---
title: CGColorRenderingIntent
framework: Core Graphics
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorrenderingintent
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorrenderingintent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorrenderingintent.json'
content_hash: 'sha256:48ba1617e5f69c4a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGColorRenderingIntent

<sub>Enumeration</sub>

Handling options for colors that are not located within the destination color space of a graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CGColorRenderingIntent
```

## Overview

The rendering intent specifies how Quartz should handle colors that are not located within the gamut of the destination color space of a graphics context. It determines the exact method used to map colors from one color space to another. If you do not explicitly set the rendering intent by calling the function [CGContextSetRenderingIntent](<cgcontext/setrenderingintent(__).md>), the graphics context uses the relative colorimetric rendering intent, except when drawing sampled images.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCGRenderingIntentDefault](cgcolorrenderingintent/defaultintent.md) — The default rendering intent for the graphics context.
- [kCGRenderingIntentAbsoluteColorimetric](cgcolorrenderingintent/absolutecolorimetric.md)
- [kCGRenderingIntentRelativeColorimetric](cgcolorrenderingintent/relativecolorimetric.md)
- [kCGRenderingIntentPerceptual](cgcolorrenderingintent/perceptual.md) — Preserve the visual relationship between colors by compressing the gamut of the graphics context to fit inside the gamut of the output device. Perceptual intent is good for photographs and other complex, detailed images.
- [kCGRenderingIntentSaturation](cgcolorrenderingintent/saturation.md)

### Initializers

- [init(rawValue:)](<cgcolorrenderingintent/init(rawvalue_).md>)
