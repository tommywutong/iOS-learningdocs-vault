---
title: isRegularFileKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresourcekey/isregularfilekey
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcekey/isregularfilekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcekey/isregularfilekey.json'
content_hash: 'sha256:044f6cf0b4dbe5cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceKey](../urlresourcekey.md)

# isRegularFileKey

<sub>Type Property</sub>

The key for determining whether the resource is a regular file rather than a directory or a symbolic link.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let isRegularFileKey: URLResourceKey
```

## Discussion

The system returns the read-only value as a Boolean [NSNumber](../nsnumber.md) object.

## See Also

### File keys

- [NSURLFileAllocatedSizeKey](fileallocatedsizekey.md) — The key for the total allocated size on-disk for the file.
- [NSURLFileProtectionKey](fileprotectionkey.md) — The key for the protection level of the file.
- [URLFileProtection](../urlfileprotection.md) — Protection-level values for a URL resource key.
- [NSURLFileContentIdentifierKey](filecontentidentifierkey.md) — The key for a value that APFS assigns to identify a file’s content data stream.
- [NSURLFileResourceIdentifierKey](fileresourceidentifierkey.md) — The key for the resource’s unique identifier.
- [NSURLFileResourceTypeKey](fileresourcetypekey.md) — The key for the resource’s object type.
- [URLFileResourceType](../urlfileresourcetype.md) — Possible values for the type of file resource.
- [NSURLFileSecurityKey](filesecuritykey.md) — The key for the resource’s security information.
- [NSURLFileSizeKey](filesizekey.md) — The key for the file’s size, in bytes.
- [NSURLIsAliasFileKey](isaliasfilekey.md) — The key for determining whether the file is an alias.
- [NSURLIsPackageKey](ispackagekey.md) — The key for determining whether the resource is a file package.
- [NSURLIsPurgeableKey](ispurgeablekey.md) — The key for a Boolean value that indicates whether the file system can delete a file when the system needs to free space.
- [NSURLIsSparseKey](issparsekey.md) — The key for a Boolean value that indicates whether the file has sparse regions.
- [NSURLMayHaveExtendedAttributesKey](mayhaveextendedattributeskey.md) — The key for a Boolean value that indicates whether the file has extended attributes.
- [NSURLMayShareFileContentKey](maysharefilecontentkey.md) — The key for a Boolean value that indicates whether cloned files and their original files may share data blocks.
