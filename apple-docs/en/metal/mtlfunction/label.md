---
title: label
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunction/label
source_url: 'https://developer.apple.com/documentation/metal/mtlfunction/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunction/label.json'
content_hash: 'sha256:ea443c74a744a210'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunction](../mtlfunction.md)

# label

<sub>Instance Property</sub>

A string that identifies the shader function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var label: String? { get set }
```

## Discussion

Object and command labels are useful identifiers at runtime or when profiling and debugging your app using any Metal tool. See [Naming resources and commands](../../xcode/naming-resources-and-commands.md).

## See Also

### Identifying shader functions

- [device](device.md) — The device object that created the shader function.
- [functionType](functiontype.md) — The shader function’s type.
- [name](name.md) — The function’s name.
- [MTLFunctionType](../mtlfunctiontype.md) — The type of a top-level Metal Shading Language (MSL) function.
- [options](options.md) — The options that Metal used to compile this function.
- [MTLFunctionOptions](../mtlfunctionoptions.md) — Options that define how Metal compiles a GPU function.
