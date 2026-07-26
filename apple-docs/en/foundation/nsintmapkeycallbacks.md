---
title: NSIntMapKeyCallBacks
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsintmapkeycallbacks
source_url: 'https://developer.apple.com/documentation/foundation/nsintmapkeycallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsintmapkeycallbacks.json'
content_hash: 'sha256:c4568366c1d083d3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSIntMapKeyCallBacks

<sub>Global Variable</sub>

For keys that are pointer-sized quantities or smaller (for example, `int`, `long`, or `unichar`).

> [!warning] Deprecated
> Use `NSIntegerMapKeyCallBacks` instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
let NSIntMapKeyCallBacks: NSMapTableKeyCallBacks
```

## See Also

### Constants

- [NSIntegerMapKeyCallBacks](nsintegermapkeycallbacks.md) — For keys that are pointer-sized quantities or smaller (for example, `int`, `long`, or `unichar`).
- [NSNonOwnedPointerMapKeyCallBacks](nsnonownedpointermapkeycallbacks.md) — For keys that are pointers not freed.
- [NSNonOwnedPointerOrNullMapKeyCallBacks](nsnonownedpointerornullmapkeycallbacks.md) — For keys that are pointers not freed, or `NULL`.
- [NSNonRetainedObjectMapKeyCallBacks](nsnonretainedobjectmapkeycallbacks.md) — For sets of objects, but without retaining/releasing.
- [NSObjectMapKeyCallBacks](nsobjectmapkeycallbacks.md) — For keys that are objects.
- [NSOwnedPointerMapKeyCallBacks](nsownedpointermapkeycallbacks.md) — For keys that are pointers, with transfer of ownership upon insertion.
