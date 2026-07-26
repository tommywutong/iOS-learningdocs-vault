---
title: 'makeComputeCommandEncoder(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandbuffer/makecomputecommandencoder(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/makecomputecommandencoder(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/makecomputecommandencoder%28descriptor%3A%29.json'
content_hash: 'sha256:12395375c48f600c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# makeComputeCommandEncoder(descriptor:)

<sub>Instance Method</sub>

Creates a compute command encoder from a descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeComputeCommandEncoder(descriptor computePassDescriptor: MTLComputePassDescriptor) -> (any MTLComputeCommandEncoder)?
```

## Parameters

- `computePassDescriptor` — An [MTLComputePassDescriptor](../mtlcomputepassdescriptor.md) instance that configures the [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md) the method returns.

## Discussion

Use an [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md) instance’s methods to set up a single compute pass.

## See Also

### Creating compute encoders

- [- computeCommandEncoder](<makecomputecommandencoder().md>) — Creates a compute command encoder that uses default settings.
- [- computeCommandEncoderWithDispatchType:](<makecomputecommandencoder(dispatchtype_).md>) — Creates a compute command encoder with a dispatch type.
- [MTLDispatchType](../mtldispatchtype.md) — The type of dispatch method to use when calling encoded functions.
