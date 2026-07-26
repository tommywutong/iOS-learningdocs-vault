---
title: info
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunlooptimercontext/info
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunlooptimercontext/info'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunlooptimercontext/info.json'
content_hash: 'sha256:ece70dfdbf7ca7f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFRunLoopTimerContext](../cfrunlooptimercontext.md)

# info

<sub>Instance Property</sub>

An arbitrary pointer to program-defined data, which can be associated with the run loop timer at creation time. This pointer is passed to all the callbacks defined in the context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var info: UnsafeMutableRawPointer!
```
