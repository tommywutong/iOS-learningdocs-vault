---
title: retain
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfdictionarykeycallbacks/retain
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks/retain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionarykeycallbacks/retain.json'
content_hash: 'sha256:1b51c712f83c3930'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFDictionaryKeyCallBacks](../cfdictionarykeycallbacks.md)

# retain

<sub>Instance Property</sub>

The callback used to retain each key as they are added to the collection. This callback returns the value to use as the key in the dictionary, which is usually the value parameter passed to this callback, but may be a different value if a different value should be used as the key. If `NULL`, keys are not retained. See [CFDictionaryRetainCallBack](../cfdictionaryretaincallback.md) for a descriptions of this function’s parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var retain: CFDictionaryRetainCallBack!
```
