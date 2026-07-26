---
title: 'setArgumentTable(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4machinelearningcommandencoder/setargumenttable(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4machinelearningcommandencoder/setargumenttable(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4machinelearningcommandencoder/setargumenttable%28_%3A%29.json'
content_hash: 'sha256:83549fd477b91ae5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4MachineLearningCommandEncoder](../mtl4machinelearningcommandencoder.md)

# setArgumentTable(_:)

<sub>Instance Method</sub>

Sets an argument table for the command encoder’s machine learning shader stage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setArgumentTable(_ argumentTable: (any MTL4ArgumentTable)?)
```

## Parameters

- `argumentTable` — An argument table to set on the command encoder’s Machine Learning stage.

## Discussion

The argument table provides inputs to all subsequent Machine Learning dispatches.

## See Also

### Configuring the pass

- [- setPipelineState:](<setpipelinestate(__).md>) — Configures the encoder with a machine learning pipeline state instance.
