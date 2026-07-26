---
title: progress
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsregularexpression/matchingflags/progress
source_url: 'https://developer.apple.com/documentation/foundation/nsregularexpression/matchingflags/progress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsregularexpression/matchingflags/progress.json'
content_hash: 'sha256:c58cd9308f10f580'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSRegularExpression](../../nsregularexpression.md) · [MatchingFlags](../matchingflags.md)

# progress

<sub>Type Property</sub>

Set when the Block is called to report progress during a long-running match operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var progress: NSRegularExpression.MatchingFlags { get }
```

## See Also

### Constants

- [NSMatchingCompleted](completed.md) — Set when the Block is called after matching has completed.
- [NSMatchingHitEnd](hitend.md) — Set when the current match operation reached the end of the search range.
- [NSMatchingRequiredEnd](requiredend.md) — Set when the current match depended on the location of the end of the search range.
- [NSMatchingInternalError](internalerror.md) — Set when matching failed due to an internal error.
