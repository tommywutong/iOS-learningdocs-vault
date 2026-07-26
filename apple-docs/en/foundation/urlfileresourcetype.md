---
title: URLFileResourceType
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlfileresourcetype
source_url: 'https://developer.apple.com/documentation/foundation/urlfileresourcetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlfileresourcetype.json'
content_hash: 'sha256:2cd88d2b6fb2d871'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLFileResourceType

<sub>Structure</sub>

Possible values for the type of file resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct URLFileResourceType
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a File Resource Type Instance

- [init(rawValue:)](<urlfileresourcetype/init(rawvalue_).md>) — Creates a file resource type from the provided constant string.

### Constants

- [NSURLFileResourceTypeNamedPipe](urlfileresourcetype/namedpipe.md) — The resource is a named pipe.
- [NSURLFileResourceTypeCharacterSpecial](urlfileresourcetype/characterspecial.md) — The resource is a character special file.
- [NSURLFileResourceTypeDirectory](urlfileresourcetype/directory.md) — The resource is a directory.
- [NSURLFileResourceTypeBlockSpecial](urlfileresourcetype/blockspecial.md) — The resource is a block special file.
- [NSURLFileResourceTypeRegular](urlfileresourcetype/regular.md) — The resource is a regular file.
- [NSURLFileResourceTypeSymbolicLink](urlfileresourcetype/symboliclink.md) — The resource is a symbolic link.
- [NSURLFileResourceTypeSocket](urlfileresourcetype/socket.md) — The resource is a socket.
- [NSURLFileResourceTypeUnknown](urlfileresourcetype/unknown.md) — The resource’s type is unknown.

## See Also

### File keys

- [NSURLFileAllocatedSizeKey](urlresourcekey/fileallocatedsizekey.md) — The key for the total allocated size on-disk for the file.
- [NSURLFileProtectionKey](urlresourcekey/fileprotectionkey.md) — The key for the protection level of the file.
- [URLFileProtection](urlfileprotection.md) — Protection-level values for a URL resource key.
- [NSURLFileContentIdentifierKey](urlresourcekey/filecontentidentifierkey.md) — The key for a value that APFS assigns to identify a file’s content data stream.
- [NSURLFileResourceIdentifierKey](urlresourcekey/fileresourceidentifierkey.md) — The key for the resource’s unique identifier.
- [NSURLFileResourceTypeKey](urlresourcekey/fileresourcetypekey.md) — The key for the resource’s object type.
- [NSURLFileSecurityKey](urlresourcekey/filesecuritykey.md) — The key for the resource’s security information.
- [NSURLFileSizeKey](urlresourcekey/filesizekey.md) — The key for the file’s size, in bytes.
- [NSURLIsAliasFileKey](urlresourcekey/isaliasfilekey.md) — The key for determining whether the file is an alias.
- [NSURLIsPackageKey](urlresourcekey/ispackagekey.md) — The key for determining whether the resource is a file package.
- [NSURLIsRegularFileKey](urlresourcekey/isregularfilekey.md) — The key for determining whether the resource is a regular file rather than a directory or a symbolic link.
- [NSURLIsPurgeableKey](urlresourcekey/ispurgeablekey.md) — The key for a Boolean value that indicates whether the file system can delete a file when the system needs to free space.
- [NSURLIsSparseKey](urlresourcekey/issparsekey.md) — The key for a Boolean value that indicates whether the file has sparse regions.
- [NSURLMayHaveExtendedAttributesKey](urlresourcekey/mayhaveextendedattributeskey.md) — The key for a Boolean value that indicates whether the file has extended attributes.
- [NSURLMayShareFileContentKey](urlresourcekey/maysharefilecontentkey.md) — The key for a Boolean value that indicates whether cloned files and their original files may share data blocks.
