---
title: MTLStorageMode.managed
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.11+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlstoragemode/managed
source_url: 'https://developer.apple.com/documentation/metal/mtlstoragemode/managed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstoragemode/managed.json'
content_hash: 'sha256:0ecf35c5fc723c6b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStorageMode](../mtlstoragemode.md)

# MTLStorageMode.managed

<sub>Case</sub>

The CPU and GPU may maintain separate copies of the resource, and any changes need to be explicitly synchronized.

> [!warning] Deprecated
> Managed storage has no effect on Apple Silicon, use Shared storage instead

<sub>Mac Catalyst, macOS</sub>

```swift
case managed
```

## Discussion

On Intel-based Mac computers, this is the default storage mode for [MTLTexture](../mtltexture.md) objects. In iOS and tvOS, the managed storage mode isn’t available. With managed storage, you synchronize changes between the CPU and GPU manually. For instructions and examples of resource synchronization, see [Synchronizing a managed resource in macOS](../synchronizing-a-managed-resource-in-macos.md).

For more guidance on how to choose storage modes, see [Setting resource storage modes](../setting-resource-storage-modes.md).

## See Also

### Storage mode options

- [MTLStorageModeShared](shared.md) — The CPU and GPU share access to the resource, allocated in system memory.
- [MTLStorageModePrivate](private.md) — The resource is only available to the GPU.
- [MTLStorageModeMemoryless](memoryless.md) — The resource’s contents are only available to the GPU, and only exist temporarily during a render pass.
