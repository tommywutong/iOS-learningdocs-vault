---
title: 'setIntersectionFunctionTable(_:bufferIndex:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcomputecommandencoder/setintersectionfunctiontable(_:bufferindex:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/setintersectionfunctiontable(_:bufferindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/setintersectionfunctiontable%28_%3Abufferindex%3A%29.json'
content_hash: 'sha256:63a1acf11a8c96ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# setIntersectionFunctionTable(_:bufferIndex:)

<sub>Instance Method</sub>

Binds an intersection function table to the buffer argument table, making it callable in your Metal shaders.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setIntersectionFunctionTable(_ intersectionFunctionTable: (any MTLIntersectionFunctionTable)?, bufferIndex: Int)
```

## Parameters

- `intersectionFunctionTable` — The [MTLIntersectionFunctionTable](../mtlintersectionfunctiontable.md) to bind.

- `bufferIndex` — The index in the buffer argument table the intersection function table binds to.

## See Also

### Binding arguments for acceleration structures

- [- setAccelerationStructure:atBufferIndex:](<setaccelerationstructure(__bufferindex_).md>) — Binds an acceleration structure to the buffer argument table, allowing functions to access it on the GPU.
