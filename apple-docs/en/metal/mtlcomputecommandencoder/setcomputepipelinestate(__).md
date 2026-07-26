---
title: 'setComputePipelineState(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/setcomputepipelinestate(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setcomputepipelinestate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/setcomputepipelinestate%28_%3A%29.json'
content_hash: 'sha256:7398dfa2afbbe499'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setComputePipelineState(_:)

<sub>Instance Method</sub>

Configures the compute encoder with a pipeline state for subsequent kernel calls.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setComputePipelineState(_ state: any MTLComputePipelineState)
```

## Parameters

- `state` — An [MTLComputePipelineState](../mtlcomputepipelinestate.md) instance.

## Discussion

> [!important] Important
> Set a compute encoder’s pipeline state before encoding any commands. Encoding commands without an available pipeline state causes an error.

Create your pipeline state through one of the [MTLDevice](../mtldevice.md) methods in Creating Compute Pipeline States.

A compute pipeline state provides information Metal uses to compile and run encoded commands. You can change the pipeline state at any time, allowing you to encode multiple kernel calls in a single command buffer. Changing the pipeline state doesn’t affect any previously encoded commands.

## See Also

### Configuring the pipeline state

- [dispatchType](dispatchtype.md) — The dispatch type to use when submitting compute work to the GPU.
