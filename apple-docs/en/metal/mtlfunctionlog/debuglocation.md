---
title: debugLocation
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionlog/debuglocation
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionlog/debuglocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionlog/debuglocation.json'
content_hash: 'sha256:9f393ecf7f920c35'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionLog](../mtlfunctionlog.md)

# debugLocation

<sub>Instance Property</sub>

If known, the location of the logging command within a shader source file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var debugLocation: (any MTLFunctionLogDebugLocation)? { get }
```

## See Also

### Getting execution details

- [encoderLabel](encoderlabel.md) — The label for the encoder that logged the message.
- [function](function.md) — When known, the function object corresponding to the logged message.
- [MTLFunctionLogDebugLocation](../mtlfunctionlogdebuglocation.md) — The source code that logged a debug message.
