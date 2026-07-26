---
title: getDescent
framework: Core Text
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctrundelegatecallbacks/getdescent
source_url: 'https://developer.apple.com/documentation/coretext/ctrundelegatecallbacks/getdescent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctrundelegatecallbacks/getdescent.json'
content_hash: 'sha256:882d74913e21ecc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTRunDelegateCallbacks](../ctrundelegatecallbacks.md)

# getDescent

<sub>Instance Property</sub>

The callback invoked to request the run delegate to determine and return the typographic descent of glyphs in the run. This callback may be `NULL`, which is equivalent to a `getDescent` callback that always returns 0.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var getDescent: CTRunDelegateGetDescentCallback
```

## See Also

### Instance Properties

- [dealloc](dealloc.md) — The callback invoked when the retain count of a CTRunDelegate reaches 0 and the CTRunDelegate is deallocated. This callback may be `NULL`.
- [getAscent](getascent.md) — The callback invoked to request the run delegate to determine and return the typographic ascent of glyphs in the run. This callback may be `NULL`, which is equivalent to a `getAscent` callback that always returns 0.
- [getWidth](getwidth.md) — The callback invoked to request the run delegate to determine and return the typographic width of glyphs in the run. This callback may be `NULL`, which is equivalent to a `getWidth` callback that always returns 0.
- [version](version.md) — The version number of the callbacks being passed in as a parameter to [CTRunDelegateCreate](<../ctrundelegatecreate(____).md>). The initial version is [kCTRunDelegateVersion1](../kctrundelegateversion1.md).
