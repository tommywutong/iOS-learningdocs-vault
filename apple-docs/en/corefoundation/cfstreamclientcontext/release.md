---
title: release
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstreamclientcontext/release
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstreamclientcontext/release'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstreamclientcontext/release.json'
content_hash: 'sha256:8cd897a3dd200854'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFStreamClientContext](../cfstreamclientcontext.md)

# release

<sub>Instance Property</sub>

A release callback for your program-defined `info` pointer. Can be `NULL`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var release: ((UnsafeMutableRawPointer?) -> Void)!
```
