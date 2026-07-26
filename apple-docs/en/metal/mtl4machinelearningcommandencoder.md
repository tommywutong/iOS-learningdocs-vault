---
title: MTL4MachineLearningCommandEncoder
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4machinelearningcommandencoder
source_url: 'https://developer.apple.com/documentation/metal/mtl4machinelearningcommandencoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4machinelearningcommandencoder.json'
content_hash: 'sha256:eb188637a6d81006'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4MachineLearningCommandEncoder

<sub>Protocol</sub>

Encodes machine learning model inference commands for a single pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTL4MachineLearningCommandEncoder : MTL4CommandEncoder
```

## Overview

Create a machine learning encoder by calling a factory method of an [MTL4CommandBuffer](mtl4commandbuffer.md) instance, such as [- machineLearningCommandEncoder](<mtl4commandbuffer/makemachinelearningcommandencoder().md>).

The [- dispatchNetworkWithIntermediatesHeap:](<mtl4machinelearningcommandencoder/dispatchnetwork(intermediatesheap_).md>) method applies to the [MTLStageMachineLearning](mtlstages/machinelearning.md) stage of a machine learning pass. For more information about stages and synchronization, see [MTLStages](mtlstages.md) and [Resource synchronization](resource-synchronization.md).

## Relationships

- **Inherits From**: [MTL4CommandEncoder](mtl4commandencoder.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the pass

- [- setPipelineState:](<mtl4machinelearningcommandencoder/setpipelinestate(__).md>) — Configures the encoder with a machine learning pipeline state instance.
- [- setArgumentTable:](<mtl4machinelearningcommandencoder/setargumenttable(__).md>) — Sets an argument table for the command encoder’s machine learning shader stage.

### Running machine learning networks

- [- dispatchNetworkWithIntermediatesHeap:](<mtl4machinelearningcommandencoder/dispatchnetwork(intermediatesheap_).md>) — Dispatches a machine learning network using the current pipeline state and argument table.

## See Also

### Encoding a machine learning pass

- [Running a machine learning model on the GPU timeline](running-a-machine-learning-model-on-the-gpu-timeline.md) — Dispatch model inference commands with a machine learning pass in a Metal 4 command buffer.
- [MTL4MachineLearningPipelineState](mtl4machinelearningpipelinestate.md) — A pipeline state that you can use with machine-learning encoder instances.
