---
title: storageModeShared
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresourceoptions/storagemodeshared
source_url: 'https://developer.apple.com/documentation/metal/mtlresourceoptions/storagemodeshared'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresourceoptions/storagemodeshared.json'
content_hash: 'sha256:2a1394ddb009d35f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResourceOptions](../mtlresourceoptions.md)

# storageModeShared

<sub>Type Property</sub>

The CPU and GPU share access to the resource, allocated in system memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var storageModeShared: MTLResourceOptions { get }
```

## Discussion

This is the default storage mode for [MTLBuffer](../mtlbuffer.md) instances on integrated GPUs and both [MTLBuffer](../mtlbuffer.md) and [MTLTexture](../mtltexture.md) instances on Apple silicon GPUs. On non-Apple family GPUs, the shared storage mode isn’t available for [MTLTexture](../mtltexture.md) instances.

When either the CPU or GPU changes the contents of the resource, you’re responsible for synchronizing access to the texture from the other participant. Ensure that all changes you schedule on either the CPU or GPU for a resource that uses shared memory complete before accessing that resource on the other processor.

For more guidance on how to choose storage modes, see [Setting resource storage modes](../setting-resource-storage-modes.md).

## See Also

### Specifying storage modes

- [MTLResourceStorageModeManaged](storagemodemanaged.md) — The CPU and GPU may maintain separate copies of the resource, and any changes need to be explicitly synchronized. _(deprecated)_
- [MTLResourceStorageModePrivate](storagemodeprivate.md) — The resource is only available to the GPU.
- [MTLResourceStorageModeMemoryless](storagemodememoryless.md) — The resource’s contents are only available to the GPU, and only exist temporarily during a render pass.
