---
title: NSIntMapValueCallBacks
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+（2.0 起废弃）, iPadOS 2.0+（2.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsintmapvaluecallbacks
source_url: 'https://developer.apple.com/documentation/foundation/nsintmapvaluecallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsintmapvaluecallbacks.json'
content_hash: 'sha256:b9c91bd8c2903cfa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSIntMapValueCallBacks

<sub>Global Variable</sub>

For values that are pointer-sized quantities, (for example, `int`, `long`, or `unichar`).

> [!warning] Deprecated
> Use `NSIntegerMapValueCallBacks` instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
let NSIntMapValueCallBacks: NSMapTableValueCallBacks
```

## See Also

### Constants

- [NSIntegerMapValueCallBacks](nsintegermapvaluecallbacks.md) — For values that are pointer-sized quantities, (for example, `int`, `long`, or `unichar`).
- [NSNonOwnedPointerMapValueCallBacks](nsnonownedpointermapvaluecallbacks.md) — For values that are not owned pointers.
- [NSOwnedPointerMapValueCallBacks](nsownedpointermapvaluecallbacks.md) — For values that are owned pointers.
- [NSNonRetainedObjectMapValueCallBacks](nsnonretainedobjectmapvaluecallbacks.md) — For sets of objects, but without retaining/releasing.
- [NSObjectMapValueCallBacks](nsobjectmapvaluecallbacks.md) — For values that are objects.
