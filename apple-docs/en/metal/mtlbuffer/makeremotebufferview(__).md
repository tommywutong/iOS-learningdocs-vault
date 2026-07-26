---
title: 'makeRemoteBufferView(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtlbuffer/makeremotebufferview(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlbuffer/makeremotebufferview(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbuffer/makeremotebufferview%28_%3A%29.json'
content_hash: 'sha256:4bfbf4bcce767374'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBuffer](../mtlbuffer.md)

# makeRemoteBufferView(_:)

<sub>Instance Method</sub>

Creates a remote view of the buffer for another GPU in the same peer group.

> [!warning] Deprecated
> Not applicable on Apple Silicon

<sub>macOS</sub>

```swift
func makeRemoteBufferView(_ device: any MTLDevice) -> (any MTLBuffer)?
```

## Discussion

The device instance that this buffer belongs to and the device you pass to the method both need to have the same nonzero peer group identifier ([peerGroupID](../mtldevice/peergroupid.md)). This buffer needs to use the private storage mode ([MTLStorageModePrivate](../mtlstoragemode/private.md)).

A remote view doesn’t allocate any storage for the new buffer; it references the memory allocated for the original buffer. You can use remote views only as a source for copy commands encoded by an [MTLBlitCommandEncoder](../mtlblitcommandencoder.md). For more information, see [Transferring data between connected GPUs](../transferring-data-between-connected-gpus.md).

## See Also

### Creating views of buffers on other GPUs

- [remoteStorageBuffer](remotestoragebuffer.md) — The buffer on another GPU that the buffer was created from, if any. _(deprecated)_
