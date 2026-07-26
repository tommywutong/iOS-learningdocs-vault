---
title: persistentIdentifier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfileversion/persistentidentifier
source_url: 'https://developer.apple.com/documentation/foundation/nsfileversion/persistentidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileversion/persistentidentifier.json'
content_hash: 'sha256:094472e8f0a38ec6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileVersion](../nsfileversion.md)

# persistentIdentifier

<sub>Instance Property</sub>

The identifier for this version of the file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var persistentIdentifier: any NSCoding { get }
```

## Discussion

You can save the value of this property persistently and use it to recreate the version object later. When recreating the version object using the [+ versionOfItemAtURL:forPersistentIdentifier:](<version(itemat_forpersistentidentifier_).md>) method, the version object returned is equivalent to the current object.

## See Also

### Accessing the Version Information

- [URL](url.md) — The URL identifying the location of the file associated with the file version object.
- [localizedName](localizedname.md) — The string containing the user-presentable name of the file version.
- [localizedNameOfSavingComputer](localizednameofsavingcomputer.md) — The user-presentable name of the computer on which the revision was saved.
- [modificationDate](modificationdate.md) — The modification date of the version.
- [discardable](isdiscardable.md) — A Boolean value that specifies whether the system can delete the associated file at some future time.
