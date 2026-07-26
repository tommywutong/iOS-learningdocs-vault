---
title: logs
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffer/logs-518l2
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/logs-518l2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/logs-518l2.json'
content_hash: 'sha256:a967c8637f27040e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# logs

<sub>Instance Property</sub>

The messages the command buffer records as the GPU runs its commands.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var logs: MTLLogContainer { get }
```

## Discussion

The value of this property is valid only after the command buffer finishes executing.
