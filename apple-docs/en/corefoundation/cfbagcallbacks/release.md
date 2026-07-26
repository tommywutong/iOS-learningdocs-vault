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
doc_path: /documentation/corefoundation/cfbagcallbacks/release
source_url: 'https://developer.apple.com/documentation/corefoundation/cfbagcallbacks/release'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfbagcallbacks/release.json'
content_hash: 'sha256:ee7bb574131f2a5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFBagCallBacks](../cfbagcallbacks.md)

# release

<sub>Instance Property</sub>

The callback used to release values as they are removed from the collection. If `NULL`, values are not released. See [CFBagReleaseCallBack](../cfbagreleasecallback.md) for a description of this callback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var release: CFBagReleaseCallBack!
```
