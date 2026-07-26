---
title: rightToLeft
framework: Core Text
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctrunstatus/righttoleft
source_url: 'https://developer.apple.com/documentation/coretext/ctrunstatus/righttoleft'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrunstatus/righttoleft.json'
content_hash: 'sha256:38eeb682f1ab4b5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTRunStatus](../ctrunstatus.md)

# rightToLeft

<sub>Type Property</sub>

The run proceeds from right to left.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var rightToLeft: CTRunStatus { get }
```

## See Also

### Constants

- [kCTRunStatusNonMonotonic](nonmonotonic.md) — The run isn’t in strictly increasing or decreasing order.
- [kCTRunStatusHasNonIdentityMatrix](hasnonidentitymatrix.md) — The run requires a specific text matrix to be set in the current Core Graphics context for proper drawing.
