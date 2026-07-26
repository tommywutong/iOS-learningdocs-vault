---
title: 'resourceStateCommandEncoder(with:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcommandbuffer/resourcestatecommandencoder(with:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/resourcestatecommandencoder(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/resourcestatecommandencoder%28with%3A%29.json'
content_hash: 'sha256:841bca6d3f4755bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# resourceStateCommandEncoder(with:)

<sub>Instance Method</sub>

Creates a resource state command encoder from a descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func resourceStateCommandEncoder(with resourceStatePassDescriptor: MTLResourceStatePassDescriptor) -> (any MTLResourceStateCommandEncoder)?
```

## Parameters

- `resourceStatePassDescriptor` — An [MTLResourceStatePassDescriptor](../mtlresourcestatepassdescriptor.md) instance that configures the [MTLResourceStateCommandEncoder](../mtlresourcestatecommandencoder.md) the method returns.

## Discussion

Use an [MTLResourceStateCommandEncoder](../mtlresourcestatecommandencoder.md) instance’s methods to create a pass that updates the state of one or more sparse textures.

## See Also

### Creating resource state encoders

- [- resourceStateCommandEncoder](<makeresourcestatecommandencoder().md>) — Creates a resource state command encoder that uses default settings.
