---
title: CIBlurredRoundedRectangleGenerator
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciblurredroundedrectanglegenerator
source_url: 'https://developer.apple.com/documentation/coreimage/ciblurredroundedrectanglegenerator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciblurredroundedrectanglegenerator.json'
content_hash: 'sha256:c50eec86cc8c7588'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIBlurredRoundedRectangleGenerator

<sub>Protocol</sub>

The protocol for the Blurred Rounded Rectangle Generator filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIBlurredRoundedRectangleGenerator : CIFilterProtocol
```

## Overview

Generates a blurred rounded rectangle image with the specified extent, corner radius, blur sigma, and color.

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [color](ciblurredroundedrectanglegenerator/color.md) — A color.
- [extent](ciblurredroundedrectanglegenerator/extent.md) — A rectangle that defines the extent of the effect.
- [radius](ciblurredroundedrectanglegenerator/radius.md) — The distance from the center of the effect.
- [sigma](ciblurredroundedrectanglegenerator/sigma.md) — The sigma for a gaussian blur.
- [smoothness](ciblurredroundedrectanglegenerator/smoothness.md) — A value to control the smoothness of the transition between the curved and linear edges of the shape.
