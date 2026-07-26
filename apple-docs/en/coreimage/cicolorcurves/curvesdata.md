---
title: curvesData
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicolorcurves/curvesdata
source_url: 'https://developer.apple.com/documentation/coreimage/cicolorcurves/curvesdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicolorcurves/curvesdata.json'
content_hash: 'sha256:1ef4299262fa5245'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIColorCurves](../cicolorcurves.md)

# curvesData

<sub>Instance Property</sub>

Color values that determine the color curves transform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var curvesData: Data { get set }
```

## Discussion

Create the curves data as an [NSData](../../foundation/nsdata.md) object containing a sequence of single-precision RGB values. These values represent a lookup table that’s applied to the input image.

Core Image unpremultiplies the image before applying the effect, and premultiplies the result after applying the effect.

## See Also

### Instance Properties

- [colorSpace](colorspace.md) — The working color space.
- [curvesDomain](curvesdomain.md) — A two-element vector that defines the minimum and maximum values of the curve data.
- [inputImage](inputimage.md) — The image to use as an input image.
