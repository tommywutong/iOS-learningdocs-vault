---
title: kCFTypeBagCallBacks
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcftypebagcallbacks
source_url: 'https://developer.apple.com/documentation/corefoundation/kcftypebagcallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcftypebagcallbacks.json'
content_hash: 'sha256:64f7685bc9b66e2c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFTypeBagCallBacks

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFTypeBagCallBacks: CFBagCallBacks
```

## Discussion

Predefined [CFBagCallBacks](cfbagcallbacks.md) structure containing a set of callbacks appropriate for use when the values in a CFBag are all CFType-derived objects. The retain callback is `CFRetain`, the release callback is `CFRelease`, the copy callback is `CFCopyDescription`, the equal callback is `CFEqual`, and the hash callback is `CFHash`. Therefore, if you use this constant when creating the collection, items are automatically retained when added to the collection, and released when removed from the collection.

## See Also

### Constants

- [kCFCopyStringBagCallBacks](kcfcopystringbagcallbacks.md) — Predefined [CFBagCallBacks](cfbagcallbacks.md) structure containing a set of callbacks appropriate for use when the values in a CFBag are all CFString objects. The bag makes immutable copies of the strings placed into it.
