---
title: NSOwnedPointerMapKeyCallBacks
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsownedpointermapkeycallbacks
source_url: 'https://developer.apple.com/documentation/foundation/nsownedpointermapkeycallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsownedpointermapkeycallbacks.json'
content_hash: 'sha256:82c96d23881c0383'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSOwnedPointerMapKeyCallBacks

<sub>Global Variable</sub>

For keys that are pointers, with transfer of ownership upon insertion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSOwnedPointerMapKeyCallBacks: NSMapTableKeyCallBacks
```

## See Also

### Constants

- [NSIntegerMapKeyCallBacks](nsintegermapkeycallbacks.md) — For keys that are pointer-sized quantities or smaller (for example, `int`, `long`, or `unichar`).
- [NSIntMapKeyCallBacks](nsintmapkeycallbacks.md) — For keys that are pointer-sized quantities or smaller (for example, `int`, `long`, or `unichar`). _(deprecated)_
- [NSNonOwnedPointerMapKeyCallBacks](nsnonownedpointermapkeycallbacks.md) — For keys that are pointers not freed.
- [NSNonOwnedPointerOrNullMapKeyCallBacks](nsnonownedpointerornullmapkeycallbacks.md) — For keys that are pointers not freed, or `NULL`.
- [NSNonRetainedObjectMapKeyCallBacks](nsnonretainedobjectmapkeycallbacks.md) — For sets of objects, but without retaining/releasing.
- [NSObjectMapKeyCallBacks](nsobjectmapkeycallbacks.md) — For keys that are objects.
