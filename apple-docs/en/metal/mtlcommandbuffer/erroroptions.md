---
title: errorOptions
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffer/erroroptions
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/erroroptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/erroroptions.json'
content_hash: 'sha256:72837d18f30be864'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# errorOptions

<sub>Instance Property</sub>

Settings that determine which information the command buffer records about execution errors, and how it does it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var errorOptions: MTLCommandBufferErrorOption { get }
```

## Discussion

The property reflects the [errorOptions](../mtlcommandbufferdescriptor/erroroptions.md) property of the [MTLCommandBufferDescriptor](../mtlcommandbufferdescriptor.md) instance at the time you create the command buffer.

## See Also

### Getting error details

- [error](error.md) — A description of an error when the GPU encounters an issue as it runs the command buffer.
- [MTLCommandBufferEncoderInfo](../mtlcommandbufferencoderinfo.md) — A container that provides additional information about a runtime failure a GPU encounters as it runs the commands in a command buffer.
- [MTLCommandBufferEncoderInfoErrorKey](../mtlcommandbufferencoderinfoerrorkey.md) — A key to a command buffer error’s user information dictionary that retrieves additional information about a GPU’s runtime error.
