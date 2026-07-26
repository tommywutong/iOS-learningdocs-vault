---
title: makeMachineLearningCommandEncoder()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4commandbuffer/makemachinelearningcommandencoder()
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandbuffer/makemachinelearningcommandencoder()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandbuffer/makemachinelearningcommandencoder%28%29.json'
content_hash: 'sha256:c04bd856162305f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandBuffer](../mtl4commandbuffer.md)

# makeMachineLearningCommandEncoder()

<sub>Instance Method</sub>

Creates a machine learning command encoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeMachineLearningCommandEncoder() -> (any MTL4MachineLearningCommandEncoder)?
```

## Return Value

The created [MTL4MachineLearningCommandEncoder](../mtl4machinelearningcommandencoder.md) instance , or `nil` if the function fails.
