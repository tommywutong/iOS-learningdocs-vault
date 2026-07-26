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
doc_path: /documentation/corefoundation/cfdictionaryvaluecallbacks/retain
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionaryvaluecallbacks/retain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionaryvaluecallbacks/retain.json'
content_hash: 'sha256:9c146c5d5a0225de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFDictionaryValueCallBacks](../cfdictionaryvaluecallbacks.md)

# retain

<sub>Instance Property</sub>

The callback used to retain each value as they are added to the collection. This callback returns the value to use as the value in the dictionary, which is usually the value parameter passed to this callback, but may be a different value if a different value should be used as the value. If `NULL`, values are not retained. See [CFDictionaryRetainCallBack](../cfdictionaryretaincallback.md) for a descriptions of this function’s parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var retain: CFDictionaryRetainCallBack!
```
