---
title: isDiscardable
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfileversion/isdiscardable
source_url: 'https://developer.apple.com/documentation/foundation/nsfileversion/isdiscardable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileversion/isdiscardable.json'
content_hash: 'sha256:40855b91eb7f35c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileVersion](../nsfileversion.md)

# isDiscardable

<sub>Instance Property</sub>

A Boolean value that specifies whether the system can delete the associated file at some future time.

<sub>macOS</sub>

```swift
var isDiscardable: Bool { get set }
```

## Discussion

Marking a file version as discardable gives the system the flexibility to reclaim the space, occupied by the associated file, at some future time. Do not, however, depend on the file being discarded.

After setting this property to [true](../../swift/true.md), do not set this property to [false](../../swift/false.md) again. Doing so causes the system to raise an exception. In addition, if you set this property to [true](../../swift/true.md) for the version of the file returned by the [+ currentVersionOfItemAtURL:](<currentversionofitem(at_).md>) method, the system raises an exception.

## See Also

### Related Documentation

- [+ removeOtherVersionsOfItemAtURL:error:](<removeotherversionsofitem(at_).md>) — Removes all versions of a file, except the current one, from the version store.
- [- removeAndReturnError:](<remove().md>) — Remove this version object and its associated file from the version store.

### Accessing the Version Information

- [URL](url.md) — The URL identifying the location of the file associated with the file version object.
- [localizedName](localizedname.md) — The string containing the user-presentable name of the file version.
- [localizedNameOfSavingComputer](localizednameofsavingcomputer.md) — The user-presentable name of the computer on which the revision was saved.
- [modificationDate](modificationdate.md) — The modification date of the version.
- [persistentIdentifier](persistentidentifier.md) — The identifier for this version of the file.
