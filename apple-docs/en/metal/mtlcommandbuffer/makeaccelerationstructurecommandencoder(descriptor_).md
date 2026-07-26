---
title: 'makeAccelerationStructureCommandEncoder(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandbuffer/makeaccelerationstructurecommandencoder(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/makeaccelerationstructurecommandencoder(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/makeaccelerationstructurecommandencoder%28descriptor%3A%29.json'
content_hash: 'sha256:cbffad6c8abbf4aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# makeAccelerationStructureCommandEncoder(descriptor:)

<sub>Instance Method</sub>

Creates a ray-tracing acceleration structure command encoder from a descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeAccelerationStructureCommandEncoder(descriptor: MTLAccelerationStructurePassDescriptor) -> any MTLAccelerationStructureCommandEncoder
```

## Parameters

- `descriptor` — An [MTLAccelerationStructurePassDescriptor](../mtlaccelerationstructurepassdescriptor.md) instance that configures the [MTLAccelerationStructureCommandEncoder](../mtlaccelerationstructurecommandencoder.md) the method returns.

## Discussion

Use an [MTLAccelerationStructureCommandEncoder](../mtlaccelerationstructurecommandencoder.md) instance’s methods to set up a single ray-tracing pass.

## See Also

### Creating acceleration structure encoders

- [- accelerationStructureCommandEncoder](<makeaccelerationstructurecommandencoder().md>) — Creates a ray-tracing acceleration structure command encoder that uses default settings.
