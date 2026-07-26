---
title: isConflict
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfileversion/isconflict
source_url: 'https://developer.apple.com/documentation/foundation/nsfileversion/isconflict'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileversion/isconflict.json'
content_hash: 'sha256:ed4889d3b70fb316'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileVersion](../nsfileversion.md)

# isConflict

<sub>Instance Property</sub>

A Boolean value indicating whether the contents of the version are in conflict with the contents of another version.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isConflict: Bool { get }
```

## Discussion

When two or more versions of a file are written at the same time, perhaps because the file is saved in the cloud and one or more of the writers were offline when they were writing, the system attempts to resolve the conflict automatically. It does this by picking one of the file versions to be the current file and setting this property to [true](../../swift/true.md) for the other file versions that are in conflict.

## See Also

### Handling Version Conflicts

- [resolved](isresolved.md) — A Boolean value that indicates if the version object is in conflict or not.
- [+ unresolvedConflictVersionsOfItemAtURL:](<unresolvedconflictversionsofitem(at_).md>) — Returns an array of version objects that are currently in conflict for the specified URL.
