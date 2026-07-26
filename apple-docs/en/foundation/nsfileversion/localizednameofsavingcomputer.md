---
title: localizedNameOfSavingComputer
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfileversion/localizednameofsavingcomputer
source_url: 'https://developer.apple.com/documentation/foundation/nsfileversion/localizednameofsavingcomputer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileversion/localizednameofsavingcomputer.json'
content_hash: 'sha256:a9dc1d42e67ac4f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileVersion](../nsfileversion.md)

# localizedNameOfSavingComputer

<sub>Instance Property</sub>

The user-presentable name of the computer on which the revision was saved.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var localizedNameOfSavingComputer: String? { get }
```

## Discussion

If the current revision has been deleted from disk, or if no computer name was recorded, the value in this property is `nil`. The computer name is guaranteed to be recorded only when the current version is in conflict with another version. The version object does not track changes to the computer name itself. Thus, if the computer name changed, the value in this string might be an old value.

## See Also

### Accessing the Version Information

- [URL](url.md) — The URL identifying the location of the file associated with the file version object.
- [localizedName](localizedname.md) — The string containing the user-presentable name of the file version.
- [modificationDate](modificationdate.md) — The modification date of the version.
- [persistentIdentifier](persistentidentifier.md) — The identifier for this version of the file.
- [discardable](isdiscardable.md) — A Boolean value that specifies whether the system can delete the associated file at some future time.
