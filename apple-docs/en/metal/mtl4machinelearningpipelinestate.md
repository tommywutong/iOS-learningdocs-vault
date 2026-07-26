---
title: MTL4MachineLearningPipelineState
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4machinelearningpipelinestate
source_url: 'https://developer.apple.com/documentation/metal/mtl4machinelearningpipelinestate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4machinelearningpipelinestate.json'
content_hash: 'sha256:53f7a387184c2eb8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTL4MachineLearningPipelineState

<sub>Protocol</sub>

A pipeline state that you can use with machine-learning encoder instances.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTL4MachineLearningPipelineState : MTLAllocation, Sendable
```

## Overview

See [MTL4MachineLearningCommandEncoder](mtl4machinelearningcommandencoder.md) for more information.

## Relationships

- **Inherits From**: [MTLAllocation](mtlallocation.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [device](mtl4machinelearningpipelinestate/device.md) — Returns the device the pipeline state belongs to.
- [intermediatesHeapSize](mtl4machinelearningpipelinestate/intermediatesheapsize.md) — Obtain the size of the heap, in bytes, this pipeline requires during the execution.
- [label](mtl4machinelearningpipelinestate/label.md) — Queries the string that helps identify this object.
- [reflection](mtl4machinelearningpipelinestate/reflection.md) — Returns reflection information for this machine learning pipeline state.

## See Also

### Encoding a machine learning pass

- [Running a machine learning model on the GPU timeline](running-a-machine-learning-model-on-the-gpu-timeline.md) — Dispatch model inference commands with a machine learning pass in a Metal 4 command buffer.
- [MTL4MachineLearningCommandEncoder](mtl4machinelearningcommandencoder.md) — Encodes machine learning model inference commands for a single pass.
