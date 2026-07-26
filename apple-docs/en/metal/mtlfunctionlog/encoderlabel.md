---
title: encoderLabel
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionlog/encoderlabel
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionlog/encoderlabel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionlog/encoderlabel.json'
content_hash: 'sha256:582cc341c013dea1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionLog](../mtlfunctionlog.md)

# encoderLabel

<sub>Instance Property</sub>

The label for the encoder that logged the message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var encoderLabel: String? { get }
```

## See Also

### Getting execution details

- [debugLocation](debuglocation.md) — If known, the location of the logging command within a shader source file.
- [function](function.md) — When known, the function object corresponding to the logged message.
- [MTLFunctionLogDebugLocation](../mtlfunctionlogdebuglocation.md) — The source code that logged a debug message.
