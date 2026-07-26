---
title: kCFTypeDictionaryKeyCallBacks
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcftypedictionarykeycallbacks
source_url: 'https://developer.apple.com/documentation/corefoundation/kcftypedictionarykeycallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcftypedictionarykeycallbacks.json'
content_hash: 'sha256:551831e882e37d16'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFTypeDictionaryKeyCallBacks

<sub>Global Variable</sub>

Predefined [CFDictionaryKeyCallBacks](cfdictionarykeycallbacks.md) structure containing a set of callbacks appropriate for use when the keys of a CFDictionary are all CFType-derived objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFTypeDictionaryKeyCallBacks: CFDictionaryKeyCallBacks
```

## Discussion

The retain callback is `CFRetain`, the release callback is `CFRelease`, the copy callback is `CFCopyDescription`, the equal callback is `CFEqual`. Therefore, if you use a pointer to this constant when creating the dictionary, keys are automatically retained when added to the collection, and released when removed from the collection.

## See Also

### Constants

- [kCFCopyStringDictionaryKeyCallBacks](kcfcopystringdictionarykeycallbacks.md) — Predefined [CFDictionaryKeyCallBacks](cfdictionarykeycallbacks.md) structure containing a set of callbacks appropriate for use when the keys of a CFDictionary are all CFString objects, which may be mutable and need to be copied in order to serve as constant keys for the values in the dictionary.
- [kCFTypeDictionaryValueCallBacks](kcftypedictionaryvaluecallbacks.md) — Predefined [CFDictionaryValueCallBacks](cfdictionaryvaluecallbacks.md) structure containing a set of callbacks appropriate for use when the values in a CFDictionary are all CFType-derived objects.
