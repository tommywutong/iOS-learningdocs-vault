---
title: 'inputDimensions(bufferIndex:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4machinelearningpipelinedescriptor/inputdimensions(bufferindex:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4machinelearningpipelinedescriptor/inputdimensions(bufferindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4machinelearningpipelinedescriptor/inputdimensions%28bufferindex%3A%29.json'
content_hash: 'sha256:d4f0a2c7392c0188'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4MachineLearningPipelineDescriptor](../mtl4machinelearningpipelinedescriptor.md)

# inputDimensions(bufferIndex:)

<sub>Instance Method</sub>

Obtains the dimensions of the input tensor at `bufferIndex` if set, `nil` otherwise.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func inputDimensions(bufferIndex: Int) -> MTLTensorExtents?
```
