---
title: functionType
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunction/functiontype
source_url: 'https://developer.apple.com/documentation/metal/mtlfunction/functiontype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunction/functiontype.json'
content_hash: 'sha256:adc75a26456cb782'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunction](../mtlfunction.md)

# functionType

<sub>Instance Property</sub>

The shader function’s type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var functionType: MTLFunctionType { get }
```

## Discussion

A function’s type determines what kind of pipeline state objects you can create from it and whether you can use it as a callable function in a function table.

## See Also

### Identifying shader functions

- [device](device.md) — The device object that created the shader function.
- [label](label.md) — A string that identifies the shader function.
- [name](name.md) — The function’s name.
- [MTLFunctionType](../mtlfunctiontype.md) — The type of a top-level Metal Shading Language (MSL) function.
- [options](options.md) — The options that Metal used to compile this function.
- [MTLFunctionOptions](../mtlfunctionoptions.md) — Options that define how Metal compiles a GPU function.
