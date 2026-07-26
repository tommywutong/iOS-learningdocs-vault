---
title: MTLFunctionLog
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionlog
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionlog'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionlog.json'
content_hash: 'sha256:0cd0b8e12ac3bc97'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLFunctionLog

<sub>Protocol</sub>

A log entry a Metal device generates when the it runs a command buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLFunctionLog : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the log messsage

- [type](mtlfunctionlog/type.md) — The type of message that was logged.
- [MTLFunctionLogType](mtlfunctionlogtype.md) — Options for different kinds of function logs.

### Getting execution details

- [debugLocation](mtlfunctionlog/debuglocation.md) — If known, the location of the logging command within a shader source file.
- [encoderLabel](mtlfunctionlog/encoderlabel.md) — The label for the encoder that logged the message.
- [function](mtlfunctionlog/function.md) — When known, the function object corresponding to the logged message.
- [MTLFunctionLogDebugLocation](mtlfunctionlogdebuglocation.md) — The source code that logged a debug message.

## See Also

### Shader logs

- [MTLLogContainer](mtllogcontainer-swift.struct.md) — A collection of logged messages, created when a Metal device runs a command buffer.
