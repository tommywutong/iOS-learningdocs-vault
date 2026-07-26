---
title: CISpotColor
framework: Core Image
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cispotcolor
source_url: 'https://developer.apple.com/documentation/coreimage/cispotcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cispotcolor.json'
content_hash: 'sha256:572b918408a21188'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Image](../coreimage.md)

# CISpotColor

<sub>Protocol</sub>

The properties you use to configure a spot color filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol CISpotColor : CIFilterProtocol
```

## Relationships

- **Inherits From**: [CIFilterProtocol](cifilterprotocol.md)

## Topics

### Instance Properties

- [centerColor1](cispotcolor/centercolor1.md) — The center value of the first color range to replace.
- [centerColor2](cispotcolor/centercolor2.md) — The center value of the second color range to replace.
- [centerColor3](cispotcolor/centercolor3.md) — The center value of the third color range to replace.
- [closeness1](cispotcolor/closeness1.md) — A value that indicates how closely the first color must match before it’s replaced.
- [closeness2](cispotcolor/closeness2.md) — A value that indicates how closely the second color must match before it’s replaced.
- [closeness3](cispotcolor/closeness3.md) — A value that indicates how closely the third color must match before it’s replaced.
- [contrast1](cispotcolor/contrast1.md) — The contrast of the first replacement color.
- [contrast2](cispotcolor/contrast2.md) — The contrast of the second replacement color.
- [contrast3](cispotcolor/contrast3.md) — The contrast of the third replacement color.
- [inputImage](cispotcolor/inputimage.md) — The image to use as an input image.
- [replacementColor1](cispotcolor/replacementcolor1.md) — A replacement color for the first color range.
- [replacementColor2](cispotcolor/replacementcolor2.md) — A replacement color for the second color range.
- [replacementColor3](cispotcolor/replacementcolor3.md) — A replacement color for the third color range.

## See Also

### Related Documentation

- [+ spotColorFilter](<cifilter-swift.class/spotcolor().md>) — Replaces colors of an image with specifed colors.

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
- [CILineOverlay](cilineoverlay.md) — The properties you use to configure a line overlay filter.
