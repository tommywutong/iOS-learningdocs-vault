---
title: fileSecurity
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresourcevalues/filesecurity
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcevalues/filesecurity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcevalues/filesecurity.json'
content_hash: 'sha256:386749c927a1bca1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceValues](../urlresourcevalues.md)

# fileSecurity

<sub>Instance Property</sub>

The file system object’s security information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fileSecurity: NSFileSecurity? { get set }
```

## See Also

### File values

- [documentIdentifier](documentidentifier.md) — A value that the kernel assigns to identify a document.
- [fileContentIdentifier](filecontentidentifier.md) — A value APFS assigns that identifies a file’s content data stream.
- [fileAllocatedSize](fileallocatedsize.md) — The total allocated size on-disk for the file, in bytes.
- [fileProtection](fileprotection.md) — The protection level for the file.
- [fileResourceIdentifier](fileresourceidentifier.md) — An identifier for comparing two file system objects for equality.
- [fileResourceType](fileresourcetype.md) — The type of the file system object.
- [fileSize](filesize.md) — The total file size, in bytes.
- [isPurgeable](ispurgeable.md) — A Boolean value that indicates whether the file system can delete a file when the system needs to free space.
- [isSparse](issparse.md) — A Boolean value that indicates whether the file has sparse regions.
- [mayHaveExtendedAttributes](mayhaveextendedattributes.md) — A Boolean value that indicates the file may have extended attributes.
- [isExecutable](isexecutable.md) — A Boolean value that indicates whether you can execute the file resource or search a directory resource.
- [isRegularFile](isregularfile.md) — A Boolean value that indicates whether the resource is a regular file.
- [mayShareFileContent](maysharefilecontent.md) — A Boolean value that indicates whether the cloned files and their original files may share data blocks.
- [totalFileAllocatedSize](totalfileallocatedsize.md) — The total allocated size of the file, in bytes.
- [totalFileSize](totalfilesize.md) — The total displayable size of the file, in bytes.
