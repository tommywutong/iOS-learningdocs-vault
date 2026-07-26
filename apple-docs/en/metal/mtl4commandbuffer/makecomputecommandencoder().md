---
title: makeComputeCommandEncoder()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4commandbuffer/makecomputecommandencoder()
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandbuffer/makecomputecommandencoder()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandbuffer/makecomputecommandencoder%28%29.json'
content_hash: 'sha256:59d8fd62236849b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandBuffer](../mtl4commandbuffer.md)

# makeComputeCommandEncoder()

<sub>Instance Method</sub>

Creates a compute command encoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeComputeCommandEncoder() -> (any MTL4ComputeCommandEncoder)?
```

## Return Value

The created [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md) instance, or `nil` if the function fails.
