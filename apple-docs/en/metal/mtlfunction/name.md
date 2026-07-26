---
title: name
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunction/name
source_url: 'https://developer.apple.com/documentation/metal/mtlfunction/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunction/name.json'
content_hash: 'sha256:803c64abd76c108f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunction](../mtlfunction.md)

# name

<sub>Instance Property</sub>

The function’s name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var name: String { get }
```

## See Also

### Identifying shader functions

- [device](device.md) — The device object that created the shader function.
- [label](label.md) — A string that identifies the shader function.
- [functionType](functiontype.md) — The shader function’s type.
- [MTLFunctionType](../mtlfunctiontype.md) — The type of a top-level Metal Shading Language (MSL) function.
- [options](options.md) — The options that Metal used to compile this function.
- [MTLFunctionOptions](../mtlfunctionoptions.md) — Options that define how Metal compiles a GPU function.
