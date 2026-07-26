---
title: remoteStorageBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.15+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlbuffer/remotestoragebuffer
source_url: 'https://developer.apple.com/documentation/metal/mtlbuffer/remotestoragebuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbuffer/remotestoragebuffer.json'
content_hash: 'sha256:a2d3c7871d36a1b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBuffer](../mtlbuffer.md)

# remoteStorageBuffer

<sub>Instance Property</sub>

The buffer on another GPU that the buffer was created from, if any.

> [!warning] Deprecated
> Not applicable on Apple Silicon

<sub>macOS</sub>

```swift
var remoteStorageBuffer: (any MTLBuffer)? { get }
```

## Discussion

If the value of this property is non-`nil`, it contains a reference to the [MTLBuffer](../mtlbuffer.md) instance that created this buffer. If the buffer isn’t a remote view, the value of this property is `nil`.

You can use remote views only as a source for copy commands encoded by an [MTLBlitCommandEncoder](../mtlblitcommandencoder.md).

## See Also

### Creating views of buffers on other GPUs

- [- newRemoteBufferViewForDevice:](<makeremotebufferview(__).md>) — Creates a remote view of the buffer for another GPU in the same peer group. _(deprecated)_
