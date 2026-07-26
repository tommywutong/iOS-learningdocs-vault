---
title: CISignedDistanceGradientFromRedMask
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cisigneddistancegradientfromredmask
source_url: 'https://developer.apple.com/documentation/coreimage/cisigneddistancegradientfromredmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cisigneddistancegradientfromredmask.json'
content_hash: 'sha256:6e1bfe75c4728ae9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CISignedDistanceGradientFromRedMask

<sub>Protocol</sub>

The protocol for the Signed Distance Gradient From Red Mask filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CISignedDistanceGradientFromRedMask : CIFilterProtocol
```

## Overview

Produces an infinite image where the red channel contains the distance in pixels from each pixel to the mask.

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [inputImage](cisigneddistancegradientfromredmask/inputimage.md) — The input image whose red channel defines a mask. If the red channel pixel value is greater than 0.5 then the point is considered in the mask and output pixel will be a value between zero and negative one. Otherwise the output pixel will be a value between zero and one.
- [maximumDistance](cisigneddistancegradientfromredmask/maximumdistance.md) — Determines the maximum distance to the mask that can be measured. Distances between zero and the maximum will be normalized to negative one and one.
