---
title: isPurgeable
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresourcevalues/ispurgeable
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcevalues/ispurgeable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcevalues/ispurgeable.json'
content_hash: 'sha256:490148e6786907b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceValues](../urlresourcevalues.md)

# isPurgeable

<sub>Instance Property</sub>

A Boolean value that indicates whether the file system can delete a file when the system needs to free space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isPurgeable: Bool? { get }
```

## See Also

### File values

- [documentIdentifier](documentidentifier.md) — A value that the kernel assigns to identify a document.
- [fileContentIdentifier](filecontentidentifier.md) — A value APFS assigns that identifies a file’s content data stream.
- [fileAllocatedSize](fileallocatedsize.md) — The total allocated size on-disk for the file, in bytes.
- [fileProtection](fileprotection.md) — The protection level for the file.
- [fileResourceIdentifier](fileresourceidentifier.md) — An identifier for comparing two file system objects for equality.
- [fileResourceType](fileresourcetype.md) — The type of the file system object.
- [fileSecurity](filesecurity.md) — The file system object’s security information.
- [fileSize](filesize.md) — The total file size, in bytes.
- [isSparse](issparse.md) — A Boolean value that indicates whether the file has sparse regions.
- [mayHaveExtendedAttributes](mayhaveextendedattributes.md) — A Boolean value that indicates the file may have extended attributes.
- [isExecutable](isexecutable.md) — A Boolean value that indicates whether you can execute the file resource or search a directory resource.
- [isRegularFile](isregularfile.md) — A Boolean value that indicates whether the resource is a regular file.
- [mayShareFileContent](maysharefilecontent.md) — A Boolean value that indicates whether the cloned files and their original files may share data blocks.
- [totalFileAllocatedSize](totalfileallocatedsize.md) — The total allocated size of the file, in bytes.
- [totalFileSize](totalfilesize.md) — The total displayable size of the file, in bytes.
