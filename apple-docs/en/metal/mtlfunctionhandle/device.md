---
title: device
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionhandle/device
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionhandle/device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionhandle/device.json'
content_hash: 'sha256:e6a062c9a281e6ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionHandle](../mtlfunctionhandle.md)

# device

<sub>Instance Property</sub>

The device object that created the shader function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var device: any MTLDevice { get }
```

## Discussion

You can only use the function handle with this [MTLDevice](../mtldevice.md).

## See Also

### Related Documentation

- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)

### Querying handle properties

- [functionType](functiontype.md) — The shader function’s type.
- [name](name.md) — The function’s name.
