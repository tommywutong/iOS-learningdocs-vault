---
title: 'setInputDimensions(_:bufferIndex:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4machinelearningpipelinedescriptor/setinputdimensions(_:bufferindex:)-8fnq7'
source_url: 'https://developer.apple.com/documentation/metal/mtl4machinelearningpipelinedescriptor/setinputdimensions(_:bufferindex:)-8fnq7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4machinelearningpipelinedescriptor/setinputdimensions%28_%3Abufferindex%3A%29-8fnq7.json'
content_hash: 'sha256:9029cacafdb3adb5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4MachineLearningPipelineDescriptor](../mtl4machinelearningpipelinedescriptor.md)

# setInputDimensions(_:bufferIndex:)

<sub>Instance Method</sub>

Sets the dimensions of multiple input tensors on a range of buffer bindings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setInputDimensions(_ dimensions: [MTLTensorExtents], bufferIndex: Int)
```

## Parameters

- `dimensions` — An array of tensor extents.

- `bufferIndex` — The index of the first input to modify. Subsequent array elements affect subsequent indices.
