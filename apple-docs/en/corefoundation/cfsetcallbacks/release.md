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
doc_path: /documentation/corefoundation/cfsetcallbacks/release
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsetcallbacks/release'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsetcallbacks/release.json'
content_hash: 'sha256:77749241f8410d94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFSetCallBacks](../cfsetcallbacks.md)

# release

<sub>Instance Property</sub>

The callback used to release values as they are removed from the collection. If `NULL`, values are not released. See [CFSetReleaseCallBack](../cfsetreleasecallback.md) for a description of this callback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var release: CFSetReleaseCallBack!
```
