---
title: CIHighlightShadowAdjust
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cihighlightshadowadjust
source_url: 'https://developer.apple.com/documentation/coreimage/cihighlightshadowadjust'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cihighlightshadowadjust.json'
content_hash: 'sha256:3f12604b00389862'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CIHighlightShadowAdjust

<sub>Protocol</sub>

The properties you use to configure a highlight-shadow adjust filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CIHighlightShadowAdjust : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [highlightAmount](cihighlightshadowadjust/highlightamount.md) — The amount of adjustment to the highlights in the image.
- [inputImage](cihighlightshadowadjust/inputimage.md) — The image to use as an input image.
- [radius](cihighlightshadowadjust/radius.md) — The shadow highlight radius.
- [shadowAmount](cihighlightshadowadjust/shadowamount.md) — The amount of adjustment to the shadows in the image.

## See Also

### Related Documentation

- [+ highlightShadowAdjustFilter](<cifilter-swift.class/highlightshadowadjust().md>) — Adjusts the highlights of colors to reduce shadows.

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
- [CILineOverlay](cilineoverlay.md) — The properties you use to configure a line overlay filter.
- [CIMix](cimix.md) — The properties you use to configure a mix filter.
