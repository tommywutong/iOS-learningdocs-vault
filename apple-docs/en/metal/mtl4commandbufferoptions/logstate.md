---
title: logState
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4commandbufferoptions/logstate
source_url: 'https://developer.apple.com/documentation/metal/mtl4commandbufferoptions/logstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4commandbufferoptions/logstate.json'
content_hash: 'sha256:077d6d6c39e0ecbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4CommandBufferOptions](../mtl4commandbufferoptions.md)

# logState

<sub>Instance Property</sub>

Contains information related to shader logging.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var logState: (any MTLLogState)? { get set }
```

## Discussion

To enable shader logging, call [- beginCommandBufferWithAllocator:options:](<../mtl4commandbuffer/begincommandbuffer(allocator_options_).md>) with an instance of [MTL4CommandBufferOptions](../mtl4commandbufferoptions.md) that contains a non-`nil` [MTLLogState](../mtllogstate.md) instance in this property.

Shader functions log messages until the command buffer ends.
