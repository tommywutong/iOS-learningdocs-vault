---
title: NSIntegerMapKeyCallBacks
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsintegermapkeycallbacks
source_url: 'https://developer.apple.com/documentation/foundation/nsintegermapkeycallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsintegermapkeycallbacks.json'
content_hash: 'sha256:5f0a0c05fc4133a7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSIntegerMapKeyCallBacks

<sub>Global Variable</sub>

For keys that are pointer-sized quantities or smaller (for example, `int`, `long`, or `unichar`).

<sub>macOS</sub>

```swift
let NSIntegerMapKeyCallBacks: NSMapTableKeyCallBacks
```

## See Also

### Constants

- [NSIntMapKeyCallBacks](nsintmapkeycallbacks.md) — For keys that are pointer-sized quantities or smaller (for example, `int`, `long`, or `unichar`). _(deprecated)_
- [NSNonOwnedPointerMapKeyCallBacks](nsnonownedpointermapkeycallbacks.md) — For keys that are pointers not freed.
- [NSNonOwnedPointerOrNullMapKeyCallBacks](nsnonownedpointerornullmapkeycallbacks.md) — For keys that are pointers not freed, or `NULL`.
- [NSNonRetainedObjectMapKeyCallBacks](nsnonretainedobjectmapkeycallbacks.md) — For sets of objects, but without retaining/releasing.
- [NSObjectMapKeyCallBacks](nsobjectmapkeycallbacks.md) — For keys that are objects.
- [NSOwnedPointerMapKeyCallBacks](nsownedpointermapkeycallbacks.md) — For keys that are pointers, with transfer of ownership upon insertion.
