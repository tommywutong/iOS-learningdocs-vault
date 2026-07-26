---
title: CIDistanceGradientFromRedMask
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cidistancegradientfromredmask
source_url: 'https://developer.apple.com/documentation/coreimage/cidistancegradientfromredmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cidistancegradientfromredmask.json'
content_hash: 'sha256:653200b2aba3d880'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIDistanceGradientFromRedMask

<sub>Protocol</sub>

The protocol for the Distance Gradient From Red Mask filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIDistanceGradientFromRedMask : CIFilterProtocol
```

## Overview

Produces an infinite image where the red channel contains the distance in pixels from each pixel to the mask.

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [inputImage](cidistancegradientfromredmask/inputimage.md) — The input image whose red channel defines a mask. If the red channel pixel value is greater than 0.5 then the point is considered in the mask and output pixel will be zero. Otherwise the output pixel will be a value between zero and one.
- [maximumDistance](cidistancegradientfromredmask/maximumdistance.md) — Determines the maximum distance to the mask that can be measured. Distances between zero and the maximum will be normalized to zero and one.
