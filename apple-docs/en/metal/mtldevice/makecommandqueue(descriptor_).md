---
title: 'makeCommandQueue(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makecommandqueue(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makecommandqueue(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makecommandqueue%28descriptor%3A%29.json'
content_hash: 'sha256:dee21a7bd19cf586'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeCommandQueue(descriptor:)

<sub>Instance Method</sub>

Creates a command queue with the provided configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeCommandQueue(descriptor: MTLCommandQueueDescriptor) -> (any MTLCommandQueue)?
```

## Parameters

- `descriptor` — The configuration for the new command queue.
