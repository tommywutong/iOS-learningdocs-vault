---
title: release
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfdictionaryvaluecallbacks/release
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionaryvaluecallbacks/release'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionaryvaluecallbacks/release.json'
content_hash: 'sha256:a5bfcf992c9c1100'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFDictionaryValueCallBacks](../cfdictionaryvaluecallbacks.md)

# release

<sub>Instance Property</sub>

The callback used to release values as they are removed from the dictionary. If `NULL`, values are not released. See [CFDictionaryReleaseCallBack](../cfdictionaryreleasecallback.md) for a description of this callback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var release: CFDictionaryReleaseCallBack!
```
