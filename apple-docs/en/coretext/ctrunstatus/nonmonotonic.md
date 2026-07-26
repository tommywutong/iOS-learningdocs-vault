---
title: nonMonotonic
framework: Core Text
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctrunstatus/nonmonotonic
source_url: 'https://developer.apple.com/documentation/coretext/ctrunstatus/nonmonotonic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrunstatus/nonmonotonic.json'
content_hash: 'sha256:6ba80f0ad5ebfc78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTRunStatus](../ctrunstatus.md)

# nonMonotonic

<sub>Type Property</sub>

The run isn’t in strictly increasing or decreasing order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var nonMonotonic: CTRunStatus { get }
```

## Discussion

The run is reordered so that the string indices associated with the glyphs aren’t in strictly increasing (for left-to-right runs) or decreasing (for right-to-left runs) order.

## See Also

### Constants

- [kCTRunStatusRightToLeft](righttoleft.md) — The run proceeds from right to left.
- [kCTRunStatusHasNonIdentityMatrix](hasnonidentitymatrix.md) — The run requires a specific text matrix to be set in the current Core Graphics context for proper drawing.
