---
title: 'dispatchNetwork(intermediatesHeap:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4machinelearningcommandencoder/dispatchnetwork(intermediatesheap:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4machinelearningcommandencoder/dispatchnetwork(intermediatesheap:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4machinelearningcommandencoder/dispatchnetwork%28intermediatesheap%3A%29.json'
content_hash: 'sha256:6f14753493844598'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4MachineLearningCommandEncoder](../mtl4machinelearningcommandencoder.md)

# dispatchNetwork(intermediatesHeap:)

<sub>Instance Method</sub>

Dispatches a machine learning network using the current pipeline state and argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func dispatchNetwork(intermediatesHeap heap: any MTLHeap)
```

## Parameters

- `heap` — A heap that Metal can use to allocate intermediate tensors.

## Discussion

This method takes a parameter consisting of a `MTLHeap` that Metal can use to allocate intermediate tensors. You can query the minimum size Metal requires for this heap by calling [intermediatesHeapSize](../mtl4machinelearningpipelinestate/intermediatesheapsize.md).
