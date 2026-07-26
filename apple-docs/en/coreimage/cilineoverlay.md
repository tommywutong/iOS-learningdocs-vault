---
title: CILineOverlay
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cilineoverlay
source_url: 'https://developer.apple.com/documentation/coreimage/cilineoverlay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cilineoverlay.json'
content_hash: 'sha256:3e1db09e8783a68b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CILineOverlay

<sub>Protocol</sub>

The properties you use to configure a line overlay filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CILineOverlay : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [NRNoiseLevel](cilineoverlay/nrnoiselevel.md) — The noise level of the image, used with camera data, that’s removed before tracing the edges of the image.
- [NRSharpness](cilineoverlay/nrsharpness.md) — The amount of sharpening done when removing noise in the image before tracing the edges of the image.
- [contrast](cilineoverlay/contrast.md) — The amount of antialiasing to use on the edges produced by this filter.
- [edgeIntensity](cilineoverlay/edgeintensity.md) — The accentuation factor of the Sobel gradient information when tracing the edges of the image.
- [inputImage](cilineoverlay/inputimage.md) — The image to use as an input image.
- [threshold](cilineoverlay/threshold.md) — A value that determines edge visibility.

## See Also

### Related Documentation

- [+ lineOverlayFilter](<cifilter-swift.class/lineoverlay().md>) — Creates an image that resembles a sketch of the outlines of objects.

### Protocols

- [CIBlendWithMask](ciblendwithmask.md) — The properties you use to configure a blend with mask filter.
- [CIBloom](cibloom.md) — The properties you use to configure a bloom filter.
- [CICannyEdgeDetector](cicannyedgedetector.md)
- [CIComicEffect](cicomiceffect.md) — The properties you use to configure a comic effect filter.
- [CICoreMLModel](cicoremlmodel.md) — The properties you use to configure a Core ML model filter.
- [CICrystallize](cicrystallize.md) — The properties you use to configure a crystalize filter.
- [CIDepthOfField](cidepthoffield.md) — The properties you use to configure a depth-of-field filter.
- [CIEdgeWork](ciedgework.md) — The properties you use to configure an edge-work filter.
- [CIEdges](ciedges.md) — The properties you use to configure an edges filter.
- [CIGaborGradients](cigaborgradients.md) — The properties you use to configure a Gabor gradients filter.
- [CIGloom](cigloom.md) — The properties you use to configure a gloom filter.
- [CIHeightFieldFromMask](ciheightfieldfrommask.md) — The properties you use to configure a height-field-from-mask filter.
- [CIHexagonalPixellate](cihexagonalpixellate.md) — The properties you use to configure a hexagonal pixellate filter.
- [CIHighlightShadowAdjust](cihighlightshadowadjust.md) — The properties you use to configure a highlight-shadow adjust filter.
- [CIMix](cimix.md) — The properties you use to configure a mix filter.
