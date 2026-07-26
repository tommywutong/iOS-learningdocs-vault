---
title: isResolved
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfileversion/isresolved
source_url: 'https://developer.apple.com/documentation/foundation/nsfileversion/isresolved'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileversion/isresolved.json'
content_hash: 'sha256:c5264f611cdbdf14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileVersion](../nsfileversion.md)

# isResolved

<sub>Instance Property</sub>

A Boolean value that indicates if the version object is in conflict or not.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isResolved: Bool { get set }
```

## Discussion

When the system detects a conflict involving versions of a file, it sets this property to [false](../../swift/false.md) to indicate an unresolved conflict. After you resolve the conflict, set this property to [true](../../swift/true.md) to tell the system it is resolved; you must then remove any versions of the file that are no longer useful.

> [!important] Important
> If you do not explicitly remove versions of a file that are no longer useful, iCloud continues to sync them to all a user’s devices and those versions continue to consume user iCloud quota.

To remove an unused version of a file, call the [- removeAndReturnError:](<remove().md>) method. To remove all unused versions of a file, call the [+ removeOtherVersionsOfItemAtURL:error:](<removeotherversionsofitem(at_).md>) method.

> [!important] Important
> Never set the value of this property to [false](../../swift/false.md). If you do, the system raises an exception.

Resolving a conflict causes the file version object to be removed from any reports about conflicting versions, such as those returned by the [+ unresolvedConflictVersionsOfItemAtURL:](<unresolvedconflictversionsofitem(at_).md>) method.

## See Also

### Handling Version Conflicts

- [conflict](isconflict.md) — A Boolean value indicating whether the contents of the version are in conflict with the contents of another version.
- [+ unresolvedConflictVersionsOfItemAtURL:](<unresolvedconflictversionsofitem(at_).md>) — Returns an array of version objects that are currently in conflict for the specified URL.
