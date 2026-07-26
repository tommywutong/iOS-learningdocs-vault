---
title: model
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicoremlmodel/model
source_url: 'https://developer.apple.com/documentation/coreimage/cicoremlmodel/model'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicoremlmodel/model.json'
content_hash: 'sha256:07dff205830514e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CICoreMLModel](../cicoremlmodel.md)

# model

<sub>Instance Property</sub>

The Core ML model used to apply the effect on the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var model: MLModel { get set }
```

## See Also

### Instance Properties

- [headIndex](headindex.md) — A number that specifies which output of a multihead Core ML model applies the effect on the image.
- [inputImage](inputimage.md) — The image to use as an input image.
- [softmaxNormalization](softmaxnormalization.md) — A Boolean value that specifies whether to apply Softmax normalization to the output of the model.
