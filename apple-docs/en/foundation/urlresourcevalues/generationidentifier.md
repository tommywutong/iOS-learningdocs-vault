---
title: generationIdentifier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresourcevalues/generationidentifier
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcevalues/generationidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcevalues/generationidentifier.json'
content_hash: 'sha256:157504475778cd46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceValues](../urlresourcevalues.md)

# generationIdentifier

<sub>Instance Property</sub>

An opaque generation identifier which can be compared using `==` to determine if the data in a document has been modified.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var generationIdentifier: (any NSCopying & NSSecureCoding & NSObjectProtocol)? { get }
```

## Discussion

For URLs which refer to the same file inode, the generation identifier will change when the data in the file’s data fork is changed (changes to extended attributes or other file system metadata do not change the generation identifier). For URLs which refer to the same directory inode, the generation identifier will change when direct children of that directory are added, removed or renamed (changes to the data of the direct children of that directory will not change the generation identifier). The generation identifier is persistent across system restarts. The generation identifier is tied to a specific document on a specific volume and is not transferred when the document is copied to another volume. This property is not supported by all volumes.

## See Also

### Universal resource values

- [addedToDirectoryDate](addedtodirectorydate.md) — The date the resource was created, or renamed into or within its parent directory.
- [allValues](allvalues.md) — A loosely-typed dictionary containing all keys and values.
- [attributeModificationDate](attributemodificationdate.md) — The time the resource’s attributes were last modified.
- [canonicalPath](canonicalpath.md) — The URL’s path as a canonical absolute file system path.
- [contentAccessDate](contentaccessdate.md) — The date the resource was last accessed.
- [contentModificationDate](contentmodificationdate.md) — The time the resource content was last modified.
- [creationDate](creationdate.md) — The date the resource was created.
- [customIcon](customicon.md)
- [effectiveIcon](effectiveicon.md)
- [hasHiddenExtension](hashiddenextension.md) — True for resources whose filename extension is removed from the localized name property.
- [isAliasFile](isaliasfile.md) — true if the resource is a Finder alias file or a symlink, false otherwise
- [isExcludedFromBackup](isexcludedfrombackup.md) — True if resource should be excluded from backups, false otherwise.
- [isHidden](ishidden.md) — True for resources normally not displayed to users.
- [isPackage](ispackage.md) — True for packaged directories.
- [isReadable](isreadable.md) — True if this process (as determined by EUID) can read the resource.
