---
title: dispatchType
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcomputecommandencoder/dispatchtype
source_url: 'https://developer.apple.com/documentation/metal/mtlcomputecommandencoder/dispatchtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcomputecommandencoder/dispatchtype.json'
content_hash: 'sha256:f3af2641afb99d6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md)

# dispatchType

<sub>Instance Property</sub>

The dispatch type to use when submitting compute work to the GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var dispatchType: MTLDispatchType { get }
```

## Discussion

You set this property when you create the command encoder, and it doesn’t change for the remainder of the encoding.

See [- computeCommandEncoderWithDispatchType:](<../mtlcommandbuffer/makecomputecommandencoder(dispatchtype_).md>) for more information.

## See Also

### Configuring the pipeline state

- [- setComputePipelineState:](<setcomputepipelinestate(__).md>) — Configures the compute encoder with a pipeline state for subsequent kernel calls.
