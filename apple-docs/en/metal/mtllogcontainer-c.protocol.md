---
title: MTLLogContainer
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtllogcontainer-c.protocol
source_url: 'https://developer.apple.com/documentation/metal/mtllogcontainer-c.protocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllogcontainer-c.protocol.json'
content_hash: 'sha256:8229d2a9850398f3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLLogContainer

<sub>Protocol</sub>

A collection of logged messages, created when a Metal device runs a command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
@protocol MTLLogContainer <NSObject, NSFastEnumeration>
```

## Overview

Enumerate a log container object to get a list of [MTLFunctionLog](mtlfunctionlog.md) instances.

## Relationships

- **Inherits From**: [NSFastEnumeration](../foundation/nsfastenumeration.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

### Shader logs

- [MTLFunctionLog](mtlfunctionlog.md) — A log entry a Metal device generates when the it runs a command buffer.
