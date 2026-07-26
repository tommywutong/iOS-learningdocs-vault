---
title: makeAccelerationStructureCommandEncoder()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffer/makeaccelerationstructurecommandencoder()
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/makeaccelerationstructurecommandencoder()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/makeaccelerationstructurecommandencoder%28%29.json'
content_hash: 'sha256:8b9c465e26cb0ae5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# makeAccelerationStructureCommandEncoder()

<sub>Instance Method</sub>

Creates a ray-tracing acceleration structure command encoder that uses default settings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeAccelerationStructureCommandEncoder() -> (any MTLAccelerationStructureCommandEncoder)?
```

## Discussion

Use an [MTLAccelerationStructureCommandEncoder](../mtlaccelerationstructurecommandencoder.md) instance’s methods to set up a single ray-tracing pass.

## See Also

### Creating acceleration structure encoders

- [- accelerationStructureCommandEncoderWithDescriptor:](<makeaccelerationstructurecommandencoder(descriptor_).md>) — Creates a ray-tracing acceleration structure command encoder from a descriptor.
