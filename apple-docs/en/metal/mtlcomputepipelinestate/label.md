---
title: label
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcomputepipelinestate/label
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputepipelinestate/label.json'
content_hash: 'sha256:f70e323ebf0ad757'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputePipelineState](../mtlcomputepipelinestate.md)

# label

<sub>Instance Property</sub>

A string that helps you identify the compute pipeline state during debugging.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String? { get }
```

## Discussion

Labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See [Naming resources and commands](../../xcode/naming-resources-and-commands.md).

## See Also

### Identifying a pipeline state

- [device](device.md) — The device instance that created the pipeline state.
- [gpuResourceID](gpuresourceid.md) — An unique identifier that represents the pipeline state, which you can add to an argument buffer.
