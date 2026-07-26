---
title: kCFCopyStringBagCallBacks
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfcopystringbagcallbacks
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfcopystringbagcallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfcopystringbagcallbacks.json'
content_hash: 'sha256:6504f3a5add14600'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFCopyStringBagCallBacks

<sub>Global Variable</sub>

Predefined [CFBagCallBacks](cfbagcallbacks.md) structure containing a set of callbacks appropriate for use when the values in a CFBag are all CFString objects. The bag makes immutable copies of the strings placed into it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFCopyStringBagCallBacks: CFBagCallBacks
```

## See Also

### Constants

- [kCFTypeBagCallBacks](kcftypebagcallbacks.md)
