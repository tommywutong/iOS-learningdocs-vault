---
title: kCFTypeArrayCallBacks
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcftypearraycallbacks
source_url: 'https://developer.apple.com/documentation/corefoundation/kcftypearraycallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcftypearraycallbacks.json'
content_hash: 'sha256:912b6ac537146486'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFTypeArrayCallBacks

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFTypeArrayCallBacks: CFArrayCallBacks
```

## Discussion

Predefined [CFArrayCallBacks](cfarraycallbacks.md) structure containing a set of callbacks appropriate for use when the values in a CFArray are all CFType-derived objects. The retain callback is `CFRetain`, the release callback is `CFRelease`, the copy callback is `CFCopyDescription`, and the equal callback is `CFEqual`. Therefore, if you use this constant when creating the collection, items are automatically retained when added to the collection, and released when removed from the collection.
