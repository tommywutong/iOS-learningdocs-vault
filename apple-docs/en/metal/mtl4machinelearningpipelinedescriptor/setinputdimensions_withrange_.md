---
title: 'setInputDimensions:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4machinelearningpipelinedescriptor/setinputdimensions:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtl4machinelearningpipelinedescriptor/setinputdimensions:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4machinelearningpipelinedescriptor/setinputdimensions%3Awithrange%3A.json'
content_hash: 'sha256:dab2b4690779c8de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4MachineLearningPipelineDescriptor](../mtl4machinelearningpipelinedescriptor.md)

# setInputDimensions:withRange:

<sub>Instance Method</sub>

Sets the dimensions of multiple input tensors on a range of buffer bindings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setInputDimensions:(NSArray<MTLTensorExtents *> *) dimensions withRange:(NSRange) range;
```

## Parameters

- `dimensions` — An array of tensor extents.

- `range` — The range of inputs of the `dimensions` argument. The range’s `length` needs to match the dimensions’ `count` property.

## Discussion

Use this method to specify the dimensions of multiple input tensors at a range of indices in a single call.

You can indicate that any tensors in the range have unspecified dimensions by providing `NSNull` at the their corresponding index location in the array.

> [!important] Important
> The range’s length property needs to match the number of dimensions you provide. Specifically, `range.length` needs to match `dimensions.count`.
