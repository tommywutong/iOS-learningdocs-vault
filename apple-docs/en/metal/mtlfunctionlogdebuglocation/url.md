---
title: url
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionlogdebuglocation/url
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionlogdebuglocation/url'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionlogdebuglocation/url.json'
content_hash: 'sha256:3e5b0306d97bb63d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionLogDebugLocation](../mtlfunctionlogdebuglocation.md)

# url

<sub>Instance Property</sub>

The URL of the file that contains the shader function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var url: URL? { get }
```

## See Also

### Inspecting the location details

- [functionName](functionname.md) — The name of the shader function.
- [line](line.md) — The line that the log message appears on.
- [column](column.md) — The column where the log message appears.
