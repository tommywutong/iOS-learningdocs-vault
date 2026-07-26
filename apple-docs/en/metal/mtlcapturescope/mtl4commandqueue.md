---
title: mtl4CommandQueue
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcapturescope/mtl4commandqueue
source_url: 'https://developer.apple.com/documentation/metal/mtlcapturescope/mtl4commandqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcapturescope/mtl4commandqueue.json'
content_hash: 'sha256:0bcb3bff81593372'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCaptureScope](../mtlcapturescope.md)

# mtl4CommandQueue

<sub>Instance Property</sub>

If set, this scope will only capture Metal commands from the associated Metal 4 command queue. Defaults to nil (all command queues from the associated device are captured).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var mtl4CommandQueue: (any MTL4CommandQueue)? { get }
```
