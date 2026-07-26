---
title: required
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionconstant/required
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionconstant/required'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionconstant/required.json'
content_hash: 'sha256:35f080cf9d41027d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionConstant](../mtlfunctionconstant.md)

# required

<sub>Instance Property</sub>

A Boolean value indicating whether the function constant needs to be provided to specialize the function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var required: Bool { get }
```

## Discussion

This value is [true](../../swift/true.md) if a constant value needs to be provided for the function constant. A function constant is optional only if it is referenced in a call to the built-in `is_function_constant_defined(name)` function.

Refer to the [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364) for more information.

## See Also

### Reading the function constant’s properties

- [name](name.md) — The name of the function constant.
- [type](type.md) — The data type of the function constant.
- [index](index.md) — The index of the function constant.
