---
title: MTLFunctionType
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctiontype
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctiontype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctiontype.json'
content_hash: 'sha256:80310bda312071cd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLFunctionType

<sub>Enumeration</sub>

The type of a top-level Metal Shading Language (MSL) function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLFunctionType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Function types

- [MTLFunctionTypeVertex](mtlfunctiontype/vertex.md) — A vertex function you can use in a render pipeline state object.
- [MTLFunctionTypeFragment](mtlfunctiontype/fragment.md) — A fragment function you can use in a render pipeline state object.
- [MTLFunctionTypeKernel](mtlfunctiontype/kernel.md) — A kernel you can use in a compute pipeline state object.
- [MTLFunctionTypeIntersection](mtlfunctiontype/intersection.md) — A function you can use in an intersection function table.
- [MTLFunctionTypeVisible](mtlfunctiontype/visible.md) — A function you can use in a visible function table.

### Enumeration Cases

- [MTLFunctionTypeMesh](mtlfunctiontype/mesh.md)
- [MTLFunctionTypeObject](mtlfunctiontype/object.md)

### Initializers

- [init(rawValue:)](<mtlfunctiontype/init(rawvalue_).md>)

## See Also

### Identifying shader functions

- [device](mtlfunction/device.md) — The device object that created the shader function.
- [label](mtlfunction/label.md) — A string that identifies the shader function.
- [functionType](mtlfunction/functiontype.md) — The shader function’s type.
- [name](mtlfunction/name.md) — The function’s name.
- [options](mtlfunction/options.md) — The options that Metal used to compile this function.
- [MTLFunctionOptions](mtlfunctionoptions.md) — Options that define how Metal compiles a GPU function.
