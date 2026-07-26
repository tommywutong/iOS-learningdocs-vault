---
title: level
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtllogstatedescriptor/level
source_url: 'https://developer.apple.com/documentation/metal/mtllogstatedescriptor/level'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllogstatedescriptor/level.json'
content_hash: 'sha256:32301b8ffb7b3cc7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLogStateDescriptor](../mtllogstatedescriptor.md)

# level

<sub>Instance Property</sub>

The minimum level of messages that the shader can log.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var level: MTLLogLevel { get set }
```

## Discussion

The default value is [MTLLogLevelDebug](../mtlloglevel/debug.md).

Use this value to limit which logs from your shader the log state stores. The log state doesn’t store messages at a lower level. Increase the level to reduce verbosity of logging.

## See Also

### Instance properties

- [bufferSize](buffersize.md) — The size of the internal buffer the log state uses, specified in bytes.
