---
title: MTLLogContainer
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtllogcontainer-swift.struct
source_url: 'https://developer.apple.com/documentation/metal/mtllogcontainer-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllogcontainer-swift.struct.json'
content_hash: 'sha256:26ae47335f2ef893'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLLogContainer

<sub>Structure</sub>

A collection of logged messages, created when a Metal device runs a command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLLogContainer
```

## Overview

Enumerate a log container object to get a list of [MTLFunctionLog](mtlfunctionlog.md) instances.

## Relationships

- **Conforms To**: [Sequence](../swift/sequence.md)

## See Also

### Shader logs

- [MTLFunctionLog](mtlfunctionlog.md) — A log entry a Metal device generates when the it runs a command buffer.
