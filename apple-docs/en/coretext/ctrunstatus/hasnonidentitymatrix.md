---
title: hasNonIdentityMatrix
framework: Core Text
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctrunstatus/hasnonidentitymatrix
source_url: 'https://developer.apple.com/documentation/coretext/ctrunstatus/hasnonidentitymatrix'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrunstatus/hasnonidentitymatrix.json'
content_hash: 'sha256:62bd4d778e94d8e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTRunStatus](../ctrunstatus.md)

# hasNonIdentityMatrix

<sub>Type Property</sub>

The run requires a specific text matrix to be set in the current Core Graphics context for proper drawing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var hasNonIdentityMatrix: CTRunStatus { get }
```

## See Also

### Constants

- [kCTRunStatusRightToLeft](righttoleft.md) — The run proceeds from right to left.
- [kCTRunStatusNonMonotonic](nonmonotonic.md) — The run isn’t in strictly increasing or decreasing order.
