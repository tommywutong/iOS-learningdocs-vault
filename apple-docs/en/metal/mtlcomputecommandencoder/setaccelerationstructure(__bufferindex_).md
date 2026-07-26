---
title: 'setAccelerationStructure(_:bufferIndex:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/setaccelerationstructure(_:bufferindex:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setaccelerationstructure(_:bufferindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/setaccelerationstructure%28_%3Abufferindex%3A%29.json'
content_hash: 'sha256:47497808d45bdef8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setAccelerationStructure(_:bufferIndex:)

<sub>Instance Method</sub>

Binds an acceleration structure to the buffer argument table, allowing functions to access it on the GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setAccelerationStructure(_ accelerationStructure: (any MTLAccelerationStructure)?, bufferIndex: Int)
```

## Parameters

- `accelerationStructure` — An [MTLAccelerationStructure](../mtlaccelerationstructure.md) instance to bind to the argument table.

- `bufferIndex` — The index the structure binds to in the argument table.

## See Also

### Binding arguments for acceleration structures

- [- setIntersectionFunctionTable:atBufferIndex:](<setintersectionfunctiontable(__bufferindex_).md>) — Binds an intersection function table to the buffer argument table, making it callable in your Metal shaders.
