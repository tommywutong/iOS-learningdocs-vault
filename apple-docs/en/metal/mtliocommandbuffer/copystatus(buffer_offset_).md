---
title: 'copyStatus(buffer:offset:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtliocommandbuffer/copystatus(buffer:offset:)'
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandbuffer/copystatus(buffer:offset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandbuffer/copystatus%28buffer%3Aoffset%3A%29.json'
content_hash: 'sha256:d560c78d5f989206'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOCommandBuffer](../mtliocommandbuffer.md)

# copyStatus(buffer:offset:)

<sub>Instance Method</sub>

Encodes a command that writes the input/output command buffer’s status to a buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func copyStatus(buffer: any MTLBuffer, offset: Int)
```

## Parameters

- `buffer` — A buffer instance the method copies the status into.

- `offset` — A starting location relative to the beginning of the buffer, in bytes, the method copies data to.

## See Also

### Adding final commands

- [- addCompletedHandler:](<addcompletedhandler(__).md>) — Adds a closure that Metal calls immediately after the GPU finishes executing the commands in the input/output command buffer.
