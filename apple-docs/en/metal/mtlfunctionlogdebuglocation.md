---
title: MTLFunctionLogDebugLocation
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionlogdebuglocation
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionlogdebuglocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionlogdebuglocation.json'
content_hash: 'sha256:a4292ddd6166c914'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLFunctionLogDebugLocation

<sub>Protocol</sub>

The source code that logged a debug message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLFunctionLogDebugLocation : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Inspecting the location details

- [functionName](mtlfunctionlogdebuglocation/functionname.md) — The name of the shader function.
- [URL](mtlfunctionlogdebuglocation/url.md) — The URL of the file that contains the shader function.
- [line](mtlfunctionlogdebuglocation/line.md) — The line that the log message appears on.
- [column](mtlfunctionlogdebuglocation/column.md) — The column where the log message appears.

## See Also

### Getting execution details

- [debugLocation](mtlfunctionlog/debuglocation.md) — If known, the location of the logging command within a shader source file.
- [encoderLabel](mtlfunctionlog/encoderlabel.md) — The label for the encoder that logged the message.
- [function](mtlfunctionlog/function.md) — When known, the function object corresponding to the logged message.
