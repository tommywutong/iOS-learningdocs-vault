---
title: bufferSize
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtllogstatedescriptor/buffersize
source_url: 'https://developer.apple.com/documentation/metal/mtllogstatedescriptor/buffersize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllogstatedescriptor/buffersize.json'
content_hash: 'sha256:3979e33d1fdf0b97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLogStateDescriptor](../mtllogstatedescriptor.md)

# bufferSize

<sub>Instance Property</sub>

The size of the internal buffer the log state uses, specified in bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var bufferSize: Int { get set }
```

## Discussion

The default value is 1MB. The minimum size of log buffer is 1KB and the maximum size is 1GB.

Carefully consider the size of this buffer based on how many messages you expect your shader to log and be useful to diagnose problems. A smaller size might lead to the shader dropping more messages while a larger size might result in a larger memory footprint and reduced performance due to excessive logging.

## See Also

### Instance properties

- [level](level.md) — The minimum level of messages that the shader can log.
