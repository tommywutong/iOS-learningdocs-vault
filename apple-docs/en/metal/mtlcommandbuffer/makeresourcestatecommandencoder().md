---
title: makeResourceStateCommandEncoder()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffer/makeresourcestatecommandencoder()
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/makeresourcestatecommandencoder()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/makeresourcestatecommandencoder%28%29.json'
content_hash: 'sha256:bb88e76fd49aff9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# makeResourceStateCommandEncoder()

<sub>Instance Method</sub>

Creates a resource state command encoder that uses default settings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeResourceStateCommandEncoder() -> (any MTLResourceStateCommandEncoder)?
```

## Discussion

Use an [MTLResourceStateCommandEncoder](../mtlresourcestatecommandencoder.md) instance’s methods to create a pass that updates the state of one or more sparse textures.

## See Also

### Creating resource state encoders

- [- resourceStateCommandEncoderWithDescriptor:](<resourcestatecommandencoder(with_).md>) — Creates a resource state command encoder from a descriptor.
