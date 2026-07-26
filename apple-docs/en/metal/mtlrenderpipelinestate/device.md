---
title: device
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinestate/device
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinestate/device.json'
content_hash: 'sha256:bf658dad10df1f1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineState](../mtlrenderpipelinestate.md)

# device

<sub>Instance Property</sub>

The device instance that creates the pipeline state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var device: any MTLDevice { get }
```

## Discussion

You can only use the pipeline state object with this device object.

## See Also

### Identifying a pipeline state

- [label](label.md) — A string that helps you identify the render pipeline state during debugging.
- [gpuResourceID](gpuresourceid.md) — An unique identifier that represents the pipeline state, which you can add to an argument buffer.
