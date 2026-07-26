---
title: intermediatesHeapSize
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4machinelearningpipelinestate/intermediatesheapsize
source_url: 'https://developer.apple.com/documentation/metal/mtl4machinelearningpipelinestate/intermediatesheapsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4machinelearningpipelinestate/intermediatesheapsize.json'
content_hash: 'sha256:0342c661c5c513cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4MachineLearningPipelineState](../mtl4machinelearningpipelinestate.md)

# intermediatesHeapSize

<sub>Instance Property</sub>

Obtain the size of the heap, in bytes, this pipeline requires during the execution.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var intermediatesHeapSize: Int { get }
```

## Discussion

Use this value to allocate a [MTLHeap](../mtlheap.md) instance of sufficient size that you can then provide to [- dispatchNetworkWithIntermediatesHeap:](<../mtl4machinelearningcommandencoder/dispatchnetwork(intermediatesheap_).md>).

Metal uses this heap to store intermediate data as it executes the pipeline. It is your responsibility to provide a heap at least as large as this property requests.
