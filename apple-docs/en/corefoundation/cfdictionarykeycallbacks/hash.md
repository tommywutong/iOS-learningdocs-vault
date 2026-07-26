---
title: hash
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfdictionarykeycallbacks/hash
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks/hash'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionarykeycallbacks/hash.json'
content_hash: 'sha256:460d38ff1274757d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFDictionaryKeyCallBacks](../cfdictionarykeycallbacks.md)

# hash

<sub>Instance Property</sub>

The callback used to compute a hash code for keys as they are used to access, add, or remove values in the dictionary. If `NULL`, the collection computes a hash code by converting the pointer value to an integer. See [CFDictionaryHashCallBack](../cfdictionaryhashcallback.md) for a description of this callback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hash: CFDictionaryHashCallBack!
```
