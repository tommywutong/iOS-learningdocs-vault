---
title: 'addCompletedHandler(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtliocommandbuffer/addcompletedhandler(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandbuffer/addcompletedhandler(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandbuffer/addcompletedhandler%28_%3A%29.json'
content_hash: 'sha256:0bc5547da69b8da8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOCommandBuffer](../mtliocommandbuffer.md)

# addCompletedHandler(_:)

<sub>Instance Method</sub>

Adds a closure that Metal calls immediately after the GPU finishes executing the commands in the input/output command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addCompletedHandler(_ block: @escaping MTLIOCommandBufferHandler)
```

## Parameters

- `block` — A Swift closure or an Objective-C block with your code.

## See Also

### Adding final commands

- [- copyStatusToBuffer:offset:](<copystatus(buffer_offset_).md>) — Encodes a command that writes the input/output command buffer’s status to a buffer.
