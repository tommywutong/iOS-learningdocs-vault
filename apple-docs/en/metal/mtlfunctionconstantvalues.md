---
title: MTLFunctionConstantValues
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionconstantvalues
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionconstantvalues.json'
content_hash: 'sha256:f1522e090394e1de'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLFunctionConstantValues

<sub>Class</sub>

A set of constant values that specialize a graphics or compute GPU function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLFunctionConstantValues
```

## Overview

An [MTLFunctionConstantValues](mtlfunctionconstantvalues.md) instance sets constant values for function constants. You declare function constants with the `[[ function_constant(index) ]]` attribute in MSL (Metal Shading Language) source code. See the [Metal Shading Language specification](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf) for more information.

With an [MTLFunctionConstantValues](mtlfunctionconstantvalues.md) instance, you can set each constant value individually with an index or a name, or set multiple constant values with an index range.

You can apply a single [MTLFunctionConstantValues](mtlfunctionconstantvalues.md) instance to multiple [MTLFunction](mtlfunction.md) instances of any kind, such as a vertex function and a fragment function. When you create a specialized function, subsequent changes to its constant values have no effect. However, you can reset, add, or modify a constant value in your [MTLFunctionConstantValues](mtlfunctionconstantvalues.md) instance and reuse it to create another [MTLFunction](mtlfunction.md) instance.

> [!tip] Tip
> See [Using function specialization to build pipeline variants](using-function-specialization-to-build-pipeline-variants.md) for a sample code project that applies function constant values.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Setting constant values

- [- setConstantValue:type:atIndex:](<mtlfunctionconstantvalues/setconstantvalue(__type_index_).md>) — Sets a value for a function constant at a specific index.
- [- setConstantValue:type:withName:](<mtlfunctionconstantvalues/setconstantvalue(__type_withname_).md>) — Sets a value for a function constant with a specific name.
- [setConstantValues(_:type:range:)](<mtlfunctionconstantvalues/setconstantvalues(__type_range_).md>) — Sets values for a group of function constants within a specific index range.

### Resetting constant values

- [- reset](<mtlfunctionconstantvalues/reset().md>) — Deletes all previously set constant values.

## See Also

### Compile-time variant functions

- [MTLFunctionConstant](mtlfunctionconstant.md) — A constant that specializes the behavior of a shader.
