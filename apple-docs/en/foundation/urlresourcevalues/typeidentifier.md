---
title: typeIdentifier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 8.0+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/urlresourcevalues/typeidentifier
source_url: 'https://developer.apple.com/documentation/foundation/urlresourcevalues/typeidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresourcevalues/typeidentifier.json'
content_hash: 'sha256:ad76f0d92d17b26e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResourceValues](../urlresourcevalues.md)

# typeIdentifier

<sub>Instance Property</sub>

A string that represents the identifier for the type of the resource.

> [!warning] Deprecated
> Use .contentType instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var typeIdentifier: String? { get }
```

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
- [generationIdentifier](generationidentifier.md) — An opaque generation identifier which can be compared using `==` to determine if the data in a document has been modified.
- [hasHiddenExtension](hashiddenextension.md) — True for resources whose filename extension is removed from the localized name property.
- [isAliasFile](isaliasfile.md) — true if the resource is a Finder alias file or a symlink, false otherwise
- [isExcludedFromBackup](isexcludedfrombackup.md) — True if resource should be excluded from backups, false otherwise.
- [isHidden](ishidden.md) — True for resources normally not displayed to users.
- [isPackage](ispackage.md) — True for packaged directories.
