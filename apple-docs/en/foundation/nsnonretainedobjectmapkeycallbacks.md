---
title: NSNonRetainedObjectMapKeyCallBacks
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnonretainedobjectmapkeycallbacks
source_url: 'https://developer.apple.com/documentation/foundation/nsnonretainedobjectmapkeycallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnonretainedobjectmapkeycallbacks.json'
content_hash: 'sha256:1b43f3de63b8fb82'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSNonRetainedObjectMapKeyCallBacks

<sub>Global Variable</sub>

For sets of objects, but without retaining/releasing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSNonRetainedObjectMapKeyCallBacks: NSMapTableKeyCallBacks
```

## See Also

### Constants

- [NSIntegerMapKeyCallBacks](nsintegermapkeycallbacks.md) — For keys that are pointer-sized quantities or smaller (for example, `int`, `long`, or `unichar`).
- [NSIntMapKeyCallBacks](nsintmapkeycallbacks.md) — For keys that are pointer-sized quantities or smaller (for example, `int`, `long`, or `unichar`). _(deprecated)_
- [NSNonOwnedPointerMapKeyCallBacks](nsnonownedpointermapkeycallbacks.md) — For keys that are pointers not freed.
- [NSNonOwnedPointerOrNullMapKeyCallBacks](nsnonownedpointerornullmapkeycallbacks.md) — For keys that are pointers not freed, or `NULL`.
- [NSObjectMapKeyCallBacks](nsobjectmapkeycallbacks.md) — For keys that are objects.
- [NSOwnedPointerMapKeyCallBacks](nsownedpointermapkeycallbacks.md) — For keys that are pointers, with transfer of ownership upon insertion.
