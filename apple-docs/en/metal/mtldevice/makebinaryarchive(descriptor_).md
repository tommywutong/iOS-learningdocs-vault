---
title: 'makeBinaryArchive(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makebinaryarchive(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makebinaryarchive(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makebinaryarchive%28descriptor%3A%29.json'
content_hash: 'sha256:0400d0d8e594bff2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeBinaryArchive(descriptor:)

<sub>Instance Method</sub>

Creates a Metal binary archive instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeBinaryArchive(descriptor: MTLBinaryArchiveDescriptor) throws -> any MTLBinaryArchive
```

## Parameters

- `descriptor` — An [MTLBinaryArchiveDescriptor](../mtlbinaryarchivedescriptor.md) instance.

## See Also

### Creating binary shader archives

- [MTLBinaryArchiveDescriptor](../mtlbinaryarchivedescriptor.md) — A description of a binary shader archive that you want to create.
- [Code](../mtlbinaryarchiveerror-swift.struct/code.md) — Error codes when creating binary archives of compiled shader code.
- [MTLBinaryArchiveDomain](../mtlbinaryarchivedomain.md) — The domain for Metal binary archive errors.
