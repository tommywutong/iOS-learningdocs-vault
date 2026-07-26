---
title: NSNonOwnedPointerOrNullMapKeyCallBacks
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnonownedpointerornullmapkeycallbacks
source_url: 'https://developer.apple.com/documentation/foundation/nsnonownedpointerornullmapkeycallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnonownedpointerornullmapkeycallbacks.json'
content_hash: 'sha256:357a431086f7164b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSNonOwnedPointerOrNullMapKeyCallBacks

<sub>Global Variable</sub>

For keys that are pointers not freed, or `NULL`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSNonOwnedPointerOrNullMapKeyCallBacks: NSMapTableKeyCallBacks
```

## See Also

### Constants

- [NSIntegerMapKeyCallBacks](nsintegermapkeycallbacks.md) — For keys that are pointer-sized quantities or smaller (for example, `int`, `long`, or `unichar`).
- [NSIntMapKeyCallBacks](nsintmapkeycallbacks.md) — For keys that are pointer-sized quantities or smaller (for example, `int`, `long`, or `unichar`). _(deprecated)_
- [NSNonOwnedPointerMapKeyCallBacks](nsnonownedpointermapkeycallbacks.md) — For keys that are pointers not freed.
- [NSNonRetainedObjectMapKeyCallBacks](nsnonretainedobjectmapkeycallbacks.md) — For sets of objects, but without retaining/releasing.
- [NSObjectMapKeyCallBacks](nsobjectmapkeycallbacks.md) — For keys that are objects.
- [NSOwnedPointerMapKeyCallBacks](nsownedpointermapkeycallbacks.md) — For keys that are pointers, with transfer of ownership upon insertion.
