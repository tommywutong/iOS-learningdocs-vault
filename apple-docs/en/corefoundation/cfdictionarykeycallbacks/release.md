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
doc_path: /documentation/corefoundation/cfdictionarykeycallbacks/release
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdictionarykeycallbacks/release'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdictionarykeycallbacks/release.json'
content_hash: 'sha256:b8aa0b67ed2c7acd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFDictionaryKeyCallBacks](../cfdictionarykeycallbacks.md)

# release

<sub>Instance Property</sub>

The callback used to release keys as they are removed from the dictionary. If `NULL`, keys are not released. See [CFDictionaryReleaseCallBack](../cfdictionaryreleasecallback.md) for a description of this callback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var release: CFDictionaryReleaseCallBack!
```
