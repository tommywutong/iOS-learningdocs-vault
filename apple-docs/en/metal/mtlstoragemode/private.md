---
title: MTLStorageMode.private
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstoragemode/private
source_url: 'https://developer.apple.com/documentation/metal/mtlstoragemode/private'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstoragemode/private.json'
content_hash: 'sha256:0e7c9a86d6d3af2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStorageMode](../mtlstoragemode.md)

# MTLStorageMode.private

<sub>Case</sub>

The resource is only available to the GPU.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case `private`
```

## Discussion

Metal may apply additional optimizations to private resources that aren’t allowed on shared or managed resources.

For more guidance on how to choose storage modes, see [Setting resource storage modes](../setting-resource-storage-modes.md).

## See Also

### Storage mode options

- [MTLStorageModeShared](shared.md) — The CPU and GPU share access to the resource, allocated in system memory.
- [MTLStorageModeManaged](managed.md) — The CPU and GPU may maintain separate copies of the resource, and any changes need to be explicitly synchronized. _(deprecated)_
- [MTLStorageModeMemoryless](memoryless.md) — The resource’s contents are only available to the GPU, and only exist temporarily during a render pass.
