---
title: localizedName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfileversion/localizedname
source_url: 'https://developer.apple.com/documentation/foundation/nsfileversion/localizedname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileversion/localizedname.json'
content_hash: 'sha256:44228b4614dc7228'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileVersion](../nsfileversion.md)

# localizedName

<sub>Instance Property</sub>

The string containing the user-presentable name of the file version.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var localizedName: String? { get }
```

## Discussion

When displaying different versions of a file to the user, you should present this string to the user instead of the version’s URL.

## See Also

### Accessing the Version Information

- [URL](url.md) — The URL identifying the location of the file associated with the file version object.
- [localizedNameOfSavingComputer](localizednameofsavingcomputer.md) — The user-presentable name of the computer on which the revision was saved.
- [modificationDate](modificationdate.md) — The modification date of the version.
- [persistentIdentifier](persistentidentifier.md) — The identifier for this version of the file.
- [discardable](isdiscardable.md) — A Boolean value that specifies whether the system can delete the associated file at some future time.
