---
title: function
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionlog/function
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionlog/function'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionlog/function.json'
content_hash: 'sha256:591486807ce0a2fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionLog](../mtlfunctionlog.md)

# function

<sub>Instance Property</sub>

When known, the function object corresponding to the logged message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var function: (any MTLFunction)? { get }
```

## See Also

### Getting execution details

- [debugLocation](debuglocation.md) — If known, the location of the logging command within a shader source file.
- [encoderLabel](encoderlabel.md) — The label for the encoder that logged the message.
- [MTLFunctionLogDebugLocation](../mtlfunctionlogdebuglocation.md) — The source code that logged a debug message.
