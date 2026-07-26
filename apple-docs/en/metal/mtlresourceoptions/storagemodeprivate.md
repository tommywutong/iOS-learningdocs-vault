---
title: storageModePrivate
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlresourceoptions/storagemodeprivate
source_url: 'https://developer.apple.com/documentation/metal/mtlresourceoptions/storagemodeprivate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlresourceoptions/storagemodeprivate.json'
content_hash: 'sha256:445dd0c6daf20fb0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLResourceOptions](../mtlresourceoptions.md)

# storageModePrivate

<sub>Type Property</sub>

The resource is only available to the GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var storageModePrivate: MTLResourceOptions { get }
```

## Discussion

Metal may apply additional optimizations to private resources that aren’t allowed on shared or managed resources.

For more guidance on how to choose storage modes, see [Setting resource storage modes](../setting-resource-storage-modes.md).

## See Also

### Specifying storage modes

- [MTLResourceStorageModeShared](storagemodeshared.md) — The CPU and GPU share access to the resource, allocated in system memory.
- [MTLResourceStorageModeManaged](storagemodemanaged.md) — The CPU and GPU may maintain separate copies of the resource, and any changes need to be explicitly synchronized. _(deprecated)_
- [MTLResourceStorageModeMemoryless](storagemodememoryless.md) — The resource’s contents are only available to the GPU, and only exist temporarily during a render pass.
