---
title: 'unresolvedConflictVersionsOfItem(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfileversion/unresolvedconflictversionsofitem(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfileversion/unresolvedconflictversionsofitem(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileversion/unresolvedconflictversionsofitem%28at%3A%29.json'
content_hash: 'sha256:ee444da590c11633'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileVersion](../nsfileversion.md)

# unresolvedConflictVersionsOfItem(at:)

<sub>Type Method</sub>

Returns an array of version objects that are currently in conflict for the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func unresolvedConflictVersionsOfItem(at url: URL) -> [NSFileVersion]?
```

## Parameters

- `url` — The URL of the file that has associated version objects.

## Return Value

An array of `NSFileVersion` objects that represent the versions in conflict or `nil` if the file at URL does not exist.

## See Also

### Handling Version Conflicts

- [conflict](isconflict.md) — A Boolean value indicating whether the contents of the version are in conflict with the contents of another version.
- [resolved](isresolved.md) — A Boolean value that indicates if the version object is in conflict or not.
