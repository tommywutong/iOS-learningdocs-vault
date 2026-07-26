---
title: gpuResourceID
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinestate/gpuresourceid
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/gpuresourceid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinestate/gpuresourceid.json'
content_hash: 'sha256:647c6af37923b7d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineState](../mtlrenderpipelinestate.md)

# gpuResourceID

<sub>Instance Property</sub>

An unique identifier that represents the pipeline state, which you can add to an argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var gpuResourceID: MTLResourceID { get }
```

## See Also

### Identifying a pipeline state

- [device](device.md) — The device instance that creates the pipeline state.
- [label](label.md) — A string that helps you identify the render pipeline state during debugging.
