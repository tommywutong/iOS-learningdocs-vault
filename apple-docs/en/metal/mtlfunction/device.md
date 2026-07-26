---
title: device
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunction/device
source_url: 'https://developer.apple.com/documentation/metal/mtlfunction/device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunction/device.json'
content_hash: 'sha256:00a3399ffa297b3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunction](../mtlfunction.md)

# device

<sub>Instance Property</sub>

The device object that created the shader function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var device: any MTLDevice { get }
```

## Discussion

You can only use this function object with this [MTLDevice](../mtldevice.md).

## See Also

### Related Documentation

- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)

### Identifying shader functions

- [label](label.md) — A string that identifies the shader function.
- [functionType](functiontype.md) — The shader function’s type.
- [name](name.md) — The function’s name.
- [MTLFunctionType](../mtlfunctiontype.md) — The type of a top-level Metal Shading Language (MSL) function.
- [options](options.md) — The options that Metal used to compile this function.
- [MTLFunctionOptions](../mtlfunctionoptions.md) — Options that define how Metal compiles a GPU function.
