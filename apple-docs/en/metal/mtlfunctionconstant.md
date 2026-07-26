---
title: MTLFunctionConstant
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctionconstant
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionconstant'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionconstant.json'
content_hash: 'sha256:b20290224e09ff1c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLFunctionConstant

<sub>Class</sub>

A constant that specializes the behavior of a shader.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLFunctionConstant
```

## Overview

Don’t create an [MTLFunctionConstant](mtlfunctionconstant.md) instance directly. Instead, the list of function constants for a function by querying the `functionConstants` property of an [MTLFunction](mtlfunction.md) instance.

An [MTLFunctionConstant](mtlfunctionconstant.md) instance should only be obtained from a nonspecialized function created with the [- newFunctionWithName:](<mtllibrary/makefunction(name_).md>) method. You only need an [MTLFunctionConstant](mtlfunctionconstant.md) instance if you don’t have sufficient information to create an [MTLFunctionConstantValues](mtlfunctionconstantvalues.md) instance used to create a specialized function with the [- newFunctionWithName:constantValues:error:](<mtllibrary/makefunction(name_constantvalues_).md>) or [- newFunctionWithName:constantValues:completionHandler:](<mtllibrary/makefunction(name_constantvalues_completionhandler_).md>) method.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Reading the function constant’s properties

- [name](mtlfunctionconstant/name.md) — The name of the function constant.
- [type](mtlfunctionconstant/type.md) — The data type of the function constant.
- [index](mtlfunctionconstant/index.md) — The index of the function constant.
- [required](mtlfunctionconstant/required.md) — A Boolean value indicating whether the function constant needs to be provided to specialize the function.

## See Also

### Compile-time variant functions

- [MTLFunctionConstantValues](mtlfunctionconstantvalues.md) — A set of constant values that specialize a graphics or compute GPU function.
