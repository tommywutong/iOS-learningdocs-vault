---
title: modificationDate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfileversion/modificationdate
source_url: 'https://developer.apple.com/documentation/foundation/nsfileversion/modificationdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileversion/modificationdate.json'
content_hash: 'sha256:2298e82d7f2b58ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileVersion](../nsfileversion.md)

# modificationDate

<sub>Instance Property</sub>

The modification date of the version.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var modificationDate: Date? { get }
```

## Discussion

If the version has been deleted, this value is `nil`.

## See Also

### Accessing the Version Information

- [URL](url.md) — The URL identifying the location of the file associated with the file version object.
- [localizedName](localizedname.md) — The string containing the user-presentable name of the file version.
- [localizedNameOfSavingComputer](localizednameofsavingcomputer.md) — The user-presentable name of the computer on which the revision was saved.
- [persistentIdentifier](persistentidentifier.md) — The identifier for this version of the file.
- [discardable](isdiscardable.md) — A Boolean value that specifies whether the system can delete the associated file at some future time.
