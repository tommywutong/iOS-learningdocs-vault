---
title: 'makeComputeCommandEncoder(dispatchType:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandbuffer/makecomputecommandencoder(dispatchtype:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/makecomputecommandencoder(dispatchtype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/makecomputecommandencoder%28dispatchtype%3A%29.json'
content_hash: 'sha256:c4a22564f8c99b44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# makeComputeCommandEncoder(dispatchType:)

<sub>Instance Method</sub>

Creates a compute command encoder with a dispatch type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeComputeCommandEncoder(dispatchType: MTLDispatchType) -> (any MTLComputeCommandEncoder)?
```

## Parameters

- `dispatchType` — An [MTLDispatchType](../mtldispatchtype.md) instance that indicates whether the compute pass the encoder creates runs commands serially or concurrently.

## Discussion

Use an [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md) instance’s methods to set up a single compute pass.

## See Also

### Creating compute encoders

- [- computeCommandEncoderWithDescriptor:](<makecomputecommandencoder(descriptor_).md>) — Creates a compute command encoder from a descriptor.
- [- computeCommandEncoder](<makecomputecommandencoder().md>) — Creates a compute command encoder that uses default settings.
- [MTLDispatchType](../mtldispatchtype.md) — The type of dispatch method to use when calling encoded functions.
