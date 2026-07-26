---
title: functionType
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionhandle/functiontype
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionhandle/functiontype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionhandle/functiontype.json'
content_hash: 'sha256:cf6e787fbdaceff4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionHandle](../mtlfunctionhandle.md)

# functionType

<sub>Instance Property</sub>

The shader function’s type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var functionType: MTLFunctionType { get }
```

## Discussion

A function’s type determines what kind of pipeline state objects you can create from it.

## See Also

### Querying handle properties

- [device](device.md) — The device object that created the shader function.
- [name](name.md) — The function’s name.
