---
title: MTLStorageMode.memoryless
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstoragemode/memoryless
source_url: 'https://developer.apple.com/documentation/metal/mtlstoragemode/memoryless'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstoragemode/memoryless.json'
content_hash: 'sha256:58831709712902ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStorageMode](../mtlstoragemode.md)

# MTLStorageMode.memoryless

<sub>Case</sub>

The resource’s contents are only available to the GPU, and only exist temporarily during a render pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case memoryless
```

## Discussion

The memoryless storage mode uses tile memory, and is only available on Apple family GPUs. Memoryless resources are temporary targets used in a pass and you can’t access their contents with [MTLLoadActionLoad](../mtlloadaction/load.md) or [MTLStoreActionStore](../mtlstoreaction/store.md).

Use memoryless resources for temporary elements used only within a single pass. For example, most render passes don’t store depth attachments and multisample attachments to memory. You can significantly reduce your memory usage by creating these attachments as memoryless resources.

On Metal devices that support tile rendering, you can use imageblocks to manage transient rendering data more flexibly. For more information about imageblock memory and using it with your shader functions, see the [Metal Shading Language Specification (PDF)](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf) sections 2.11, 4.5, and 5.6.

For more guidance on how to choose storage modes, see [Setting resource storage modes](../setting-resource-storage-modes.md).

## See Also

### Storage mode options

- [MTLStorageModeShared](shared.md) — The CPU and GPU share access to the resource, allocated in system memory.
- [MTLStorageModeManaged](managed.md) — The CPU and GPU may maintain separate copies of the resource, and any changes need to be explicitly synchronized. _(deprecated)_
- [MTLStorageModePrivate](private.md) — The resource is only available to the GPU.
