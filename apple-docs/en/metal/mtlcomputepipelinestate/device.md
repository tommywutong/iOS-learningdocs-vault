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
doc_path: /documentation/metal/mtlcomputepipelinestate/device
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepipelinestate/device.json'
content_hash: 'sha256:acee6455b10c7679'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePipelineState](../mtlcomputepipelinestate.md)

# device

<sub>Instance Property</sub>

The device instance that created the pipeline state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var device: any MTLDevice { get }
```

## Discussion

This compute state instance is only usable on the device set in this property.

## See Also

### Identifying a pipeline state

- [gpuResourceID](gpuresourceid.md) — An unique identifier that represents the pipeline state, which you can add to an argument buffer.
- [label](label.md) — A string that helps you identify the compute pipeline state during debugging.
