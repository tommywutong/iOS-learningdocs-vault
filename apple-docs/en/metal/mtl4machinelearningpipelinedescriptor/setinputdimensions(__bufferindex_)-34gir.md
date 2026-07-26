---
title: 'setInputDimensions(_:bufferIndex:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4machinelearningpipelinedescriptor/setinputdimensions(_:bufferindex:)-34gir'
source_url: 'https://developer.apple.com/documentation/metal/mtl4machinelearningpipelinedescriptor/setinputdimensions(_:bufferindex:)-34gir'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4machinelearningpipelinedescriptor/setinputdimensions%28_%3Abufferindex%3A%29-34gir.json'
content_hash: 'sha256:f3d164b25233e597'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4MachineLearningPipelineDescriptor](../mtl4machinelearningpipelinedescriptor.md)

# setInputDimensions(_:bufferIndex:)

<sub>Instance Method</sub>

Sets the dimension of an input tensor at a buffer index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setInputDimensions(_ dimensions: MTLTensorExtents?, bufferIndex: Int)
```

## Parameters

- `dimensions` — The dimensions of the tensor.

- `bufferIndex` — Index of the tensor to modify.

## Discussion

When the compiled model declares the input as unranked (unknown rank), any concrete `dimensions` are accepted. Otherwise `dimensions.rank` must equal the model’s input rank, and each static (non `-1`) dimension must match.
