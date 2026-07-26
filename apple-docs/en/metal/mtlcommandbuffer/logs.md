---
title: logs
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcommandbuffer/logs
source_url: 'https://developer.apple.com/documentation/metal/mtlcommandbuffer/logs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcommandbuffer/logs.json'
content_hash: 'sha256:06997ce1b3e3125f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCommandBuffer](../mtlcommandbuffer.md)

# logs

<sub>Instance Property</sub>

The messages the command buffer records as the GPU runs its commands.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
@property (readonly) id<MTLLogContainer> logs;
```

## Discussion

The value of this property is valid only after the command buffer finishes executing.

## Default Implementations

### MTLCommandBuffer Implementations

- [logs](logs-518l2.md) — The messages the command buffer records as the GPU runs its commands.
