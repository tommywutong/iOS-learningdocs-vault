---
title: 'makeIndirectCommandBuffer(descriptor:maxCommandCount:options:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makeindirectcommandbuffer(descriptor:maxcommandcount:options:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makeindirectcommandbuffer(descriptor:maxcommandcount:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makeindirectcommandbuffer%28descriptor%3Amaxcommandcount%3Aoptions%3A%29.json'
content_hash: 'sha256:56d8fb2d4881d8c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeIndirectCommandBuffer(descriptor:maxCommandCount:options:)

<sub>Instance Method</sub>

Creates an indirect command buffer instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeIndirectCommandBuffer(descriptor: MTLIndirectCommandBufferDescriptor, maxCommandCount maxCount: Int, options: MTLResourceOptions = []) -> (any MTLIndirectCommandBuffer)?
```

## Parameters

- `descriptor` — An [MTLIndirectCommandBufferDescriptor](../mtlindirectcommandbufferdescriptor.md) instance.

- `maxCount` — The largest number of commands you can store in the buffer.

- `options` — An [MTLResourceOptions](../mtlresourceoptions.md) instance.

## Return Value

A new [MTLIndirectCommandBuffer](../mtlindirectcommandbuffer.md) instance if the method completed successfully; otherwise `nil`.
