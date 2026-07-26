---
title: headIndex
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicoremlmodel/headindex
source_url: 'https://developer.apple.com/documentation/coreimage/cicoremlmodel/headindex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicoremlmodel/headindex.json'
content_hash: 'sha256:6949464e64034098'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CICoreMLModel](../cicoremlmodel.md)

# headIndex

<sub>Instance Property</sub>

A number that specifies which output of a multihead Core ML model applies the effect on the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var headIndex: Float { get set }
```

## See Also

### Instance Properties

- [inputImage](inputimage.md) — The image to use as an input image.
- [model](model.md) — The Core ML model used to apply the effect on the image.
- [softmaxNormalization](softmaxnormalization.md) — A Boolean value that specifies whether to apply Softmax normalization to the output of the model.
