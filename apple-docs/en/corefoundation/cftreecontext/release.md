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
doc_path: /documentation/corefoundation/cftreecontext/release
source_url: 'https://developer.apple.com/documentation/corefoundation/cftreecontext/release'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cftreecontext/release.json'
content_hash: 'sha256:31ab86bb86090c28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFTreeContext](../cftreecontext.md)

# release

<sub>Instance Property</sub>

The callback used to release a previously retained `info` field. If this parameter is not a pointer to a function of the correct prototype, the behavior is undefined. This value may be `NULL`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var release: CFTreeReleaseCallBack!
```
