---
title: kCFCopyStringDictionaryKeyCallBacks
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfcopystringdictionarykeycallbacks
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfcopystringdictionarykeycallbacks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfcopystringdictionarykeycallbacks.json'
content_hash: 'sha256:990d7ae632b6a747'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFCopyStringDictionaryKeyCallBacks

<sub>Global Variable</sub>

Predefined [CFDictionaryKeyCallBacks](cfdictionarykeycallbacks.md) structure containing a set of callbacks appropriate for use when the keys of a CFDictionary are all CFString objects, which may be mutable and need to be copied in order to serve as constant keys for the values in the dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFCopyStringDictionaryKeyCallBacks: CFDictionaryKeyCallBacks
```

## Discussion

You typically use a pointer to this constant when creating a new dictionary.

> [!important] Important
> For performance reasons, the default `kCFCopyStringDictionaryKeyCallBacks` behavior uses [CFEqual](<cfequal(____).md>) which does not normalize the strings. This means that, for example, it does not consider CFStrings to be equal when they are the same but one is in pre-composed form (say, originating from a UTF-16 text file) and the other in decomposed form (say, originating from a file name). In cases where you use strings from different sources, you may want to pre-normalize the keys or else use a different set of functions to perform the comparison.

## See Also

### Constants

- [kCFTypeDictionaryKeyCallBacks](kcftypedictionarykeycallbacks.md) — Predefined [CFDictionaryKeyCallBacks](cfdictionarykeycallbacks.md) structure containing a set of callbacks appropriate for use when the keys of a CFDictionary are all CFType-derived objects.
- [kCFTypeDictionaryValueCallBacks](kcftypedictionaryvaluecallbacks.md) — Predefined [CFDictionaryValueCallBacks](cfdictionaryvaluecallbacks.md) structure containing a set of callbacks appropriate for use when the values in a CFDictionary are all CFType-derived objects.
