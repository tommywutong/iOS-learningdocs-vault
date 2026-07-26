---
title: kCFTypeSetCallBacks
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcftypesetcallbacks
source_url: 'https://developer.apple.com/documentation/corefoundation/kcftypesetcallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcftypesetcallbacks.json'
content_hash: 'sha256:678255466aa4ea71'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFTypeSetCallBacks

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFTypeSetCallBacks: CFSetCallBacks
```

## Discussion

Predefined [CFSetCallBacks](cfsetcallbacks.md) structure containing a set of callbacks  appropriate for use when the values in a CFSet are all CFType-derived objects. The retain callback is [CFRetain](cfretain.md), the release callback is [CFRelease](cfrelease.md), the copy callback is [CFCopyDescription](<cfcopydescription(__).md>), the equal callback is [CFEqual](<cfequal(____).md>), and the hash callback is [CFHash](<cfhash(__).md>). Therefore, if you use this constant when creating the collection, items are automatically retained when added to the collection, and released when removed from the collection.

## See Also

### Constants

- [kCFCopyStringSetCallBacks](kcfcopystringsetcallbacks.md) — Predefined [CFSetCallBacks](cfsetcallbacks.md) structure containing a set of callbacks  appropriate for use when the values in a set are all CFString objects. The retain callback makes an immutable copy of strings added to the set.
