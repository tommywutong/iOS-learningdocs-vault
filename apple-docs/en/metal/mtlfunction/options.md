---
title: options
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunction/options
source_url: 'https://developer.apple.com/documentation/metal/mtlfunction/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunction/options.json'
content_hash: 'sha256:b5ea8f06e31260f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunction](../mtlfunction.md)

# options

<sub>Instance Property</sub>

The options that Metal used to compile this function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var options: MTLFunctionOptions { get }
```

## See Also

### Identifying shader functions

- [device](device.md) — The device object that created the shader function.
- [label](label.md) — A string that identifies the shader function.
- [functionType](functiontype.md) — The shader function’s type.
- [name](name.md) — The function’s name.
- [MTLFunctionType](../mtlfunctiontype.md) — The type of a top-level Metal Shading Language (MSL) function.
- [MTLFunctionOptions](../mtlfunctionoptions.md) — Options that define how Metal compiles a GPU function.
