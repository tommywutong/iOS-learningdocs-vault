---
title: enqueueBarrier()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliocommandqueue/enqueuebarrier()
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandqueue/enqueuebarrier()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandqueue/enqueuebarrier%28%29.json'
content_hash: 'sha256:039f531e762dd403'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOCommandQueue](../mtliocommandqueue.md)

# enqueueBarrier()

<sub>Instance Method</sub>

Appends a barrier that tells the input/output command queue to finish running all in-flight command buffers before running any new command buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func enqueueBarrier()
```
