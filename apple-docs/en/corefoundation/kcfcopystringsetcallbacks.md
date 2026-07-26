---
title: kCFCopyStringSetCallBacks
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfcopystringsetcallbacks
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfcopystringsetcallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfcopystringsetcallbacks.json'
content_hash: 'sha256:0c911ae89db03fd8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFCopyStringSetCallBacks

<sub>Global Variable</sub>

Predefined [CFSetCallBacks](cfsetcallbacks.md) structure containing a set of callbacks  appropriate for use when the values in a set are all CFString objects. The retain callback makes an immutable copy of strings added to the set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFCopyStringSetCallBacks: CFSetCallBacks
```

## See Also

### Constants

- [kCFTypeSetCallBacks](kcftypesetcallbacks.md)
