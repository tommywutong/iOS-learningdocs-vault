---
title: CICoreMLModel
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicoremlmodel
source_url: 'https://developer.apple.com/documentation/coreimage/cicoremlmodel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicoremlmodel.json'
content_hash: 'sha256:44805f25560a6763'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CICoreMLModel

<sub>Protocol</sub>

The properties you use to configure a Core ML model filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CICoreMLModel : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [headIndex](cicoremlmodel/headindex.md) — A number that specifies which output of a multihead Core ML model applies the effect on the image.
- [inputImage](cicoremlmodel/inputimage.md) — The image to use as an input image.
- [model](cicoremlmodel/model.md) — The Core ML model used to apply the effect on the image.
- [softmaxNormalization](cicoremlmodel/softmaxnormalization.md) — A Boolean value that specifies whether to apply Softmax normalization to the output of the model.

## See Also

### Related Documentation

- [+ coreMLModelFilter](<cifilter-swift.class/coremlmodel().md>) — Filters an image with a Core ML model.

### Protocols

- [CIBlendWithMask](ciblendwithmask.md) — The properties you use to configure a blend with mask filter.
- [CIBloom](cibloom.md) — The properties you use to configure a bloom filter.
- [CICannyEdgeDetector](cicannyedgedetector.md)
- [CIComicEffect](cicomiceffect.md) — The properties you use to configure a comic effect filter.
- [CICrystallize](cicrystallize.md) — The properties you use to configure a crystalize filter.
- [CIDepthOfField](cidepthoffield.md) — The properties you use to configure a depth-of-field filter.
- [CIEdgeWork](ciedgework.md) — The properties you use to configure an edge-work filter.
- [CIEdges](ciedges.md) — The properties you use to configure an edges filter.
- [CIGaborGradients](cigaborgradients.md) — The properties you use to configure a Gabor gradients filter.
- [CIGloom](cigloom.md) — The properties you use to configure a gloom filter.
- [CIHeightFieldFromMask](ciheightfieldfrommask.md) — The properties you use to configure a height-field-from-mask filter.
- [CIHexagonalPixellate](cihexagonalpixellate.md) — The properties you use to configure a hexagonal pixellate filter.
- [CIHighlightShadowAdjust](cihighlightshadowadjust.md) — The properties you use to configure a highlight-shadow adjust filter.
- [CILineOverlay](cilineoverlay.md) — The properties you use to configure a line overlay filter.
- [CIMix](cimix.md) — The properties you use to configure a mix filter.
