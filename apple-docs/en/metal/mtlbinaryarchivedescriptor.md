---
title: MTLBinaryArchiveDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlbinaryarchivedescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlbinaryarchivedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbinaryarchivedescriptor.json'
content_hash: 'sha256:28a7eefef5e40238'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLBinaryArchiveDescriptor

<sub>Class</sub>

A description of a binary shader archive that you want to create.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLBinaryArchiveDescriptor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Choosing an archive file

- [url](mtlbinaryarchivedescriptor/url.md) — A URL to a Metal binary archive file.

## See Also

### Creating binary shader archives

- [- newBinaryArchiveWithDescriptor:error:](<mtldevice/makebinaryarchive(descriptor_).md>) — Creates a Metal binary archive instance.
- [Code](mtlbinaryarchiveerror-swift.struct/code.md) — Error codes when creating binary archives of compiled shader code.
- [MTLBinaryArchiveDomain](mtlbinaryarchivedomain.md) — The domain for Metal binary archive errors.
