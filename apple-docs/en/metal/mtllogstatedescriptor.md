---
title: MTLLogStateDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtllogstatedescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtllogstatedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllogstatedescriptor.json'
content_hash: 'sha256:9cb93c4f1fe4f020'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLLogStateDescriptor

<sub>Class</sub>

An interface that represents a log state configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLLogStateDescriptor
```

## Overview

Configure the descriptor to create an [MTLLogState](mtllogstate.md) by calling [- newLogStateWithDescriptor:error:](<mtldevice/makelogstate(descriptor_).md>).

If you’ve set the environment variables `MTL_LOG_BUFFER_SIZE` or `MTL_LOG_LEVEL`, then the system automatically enables logging. If any command buffer or command queue has an attached log state, then the system uses the log state’s settings instead of the environment variable values.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Instance properties

- [bufferSize](mtllogstatedescriptor/buffersize.md) — The size of the internal buffer the log state uses, specified in bytes.
- [level](mtllogstatedescriptor/level.md) — The minimum level of messages that the shader can log.

### Log levels

- [MTLLogLevel](mtlloglevel.md) — The supported log levels for shader logging.

## See Also

### Shader logging

- [MTLLogState](mtllogstate.md) — A container for shader log messages.
