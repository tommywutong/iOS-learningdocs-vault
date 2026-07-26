---
title: info
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfstreamclientcontext/info
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstreamclientcontext/info'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstreamclientcontext/info.json'
content_hash: 'sha256:8f1298da1c3c3249'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFStreamClientContext](../cfstreamclientcontext.md)

# info

<sub>Instance Property</sub>

An arbitrary pointer to program-defined data, which can be associated with the client. This pointer is passed to the callbacks defined in the context and to the client callback function [CFReadStreamClientCallBack](../cfreadstreamclientcallback.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var info: UnsafeMutableRawPointer!
```
