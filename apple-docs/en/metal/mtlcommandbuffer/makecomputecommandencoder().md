---
title: makeComputeCommandEncoder()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffer/makecomputecommandencoder()
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/makecomputecommandencoder()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/makecomputecommandencoder%28%29.json'
content_hash: 'sha256:e8fd2630aa855286'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# makeComputeCommandEncoder()

<sub>Instance Method</sub>

Creates a compute command encoder that uses default settings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeComputeCommandEncoder() -> (any MTLComputeCommandEncoder)?
```

## Discussion

Use an [MTLComputeCommandEncoder](../mtlcomputecommandencoder.md) instance’s methods to set up a single compute pass. The encoder this method returns dispatches its compute commands serially (see [MTLDispatchTypeSerial](../mtldispatchtype/serial.md)). To create a compute command encoder that dispatches commands concurrently (see [MTLDispatchTypeConcurrent](../mtldispatchtype/concurrent.md)), use the [- computeCommandEncoderWithDispatchType:](<makecomputecommandencoder(dispatchtype_).md>) or [- computeCommandEncoderWithDescriptor:](<makecomputecommandencoder(descriptor_).md>) method.

## See Also

### Creating compute encoders

- [- computeCommandEncoderWithDescriptor:](<makecomputecommandencoder(descriptor_).md>) — Creates a compute command encoder from a descriptor.
- [- computeCommandEncoderWithDispatchType:](<makecomputecommandencoder(dispatchtype_).md>) — Creates a compute command encoder with a dispatch type.
- [MTLDispatchType](../mtldispatchtype.md) — The type of dispatch method to use when calling encoded functions.
