---
title: 'setPipelineState(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4machinelearningcommandencoder/setpipelinestate(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4machinelearningcommandencoder/setpipelinestate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4machinelearningcommandencoder/setpipelinestate%28_%3A%29.json'
content_hash: 'sha256:75214b3e9635d74e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4MachineLearningCommandEncoder](../mtl4machinelearningcommandencoder.md)

# setPipelineState(_:)

<sub>Instance Method</sub>

Configures the encoder with a machine learning pipeline state instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setPipelineState(_ pipelineState: any MTL4MachineLearningPipelineState)
```

## Parameters

- `pipelineState` — A Machine Learning pipeline state instance.

## Discussion

The pipeline state instance affects all subsequent Machine Learning commands.

## See Also

### Configuring the pass

- [- setArgumentTable:](<setargumenttable(__).md>) — Sets an argument table for the command encoder’s machine learning shader stage.
