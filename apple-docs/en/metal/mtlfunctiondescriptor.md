---
title: MTLFunctionDescriptor
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunctiondescriptor
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctiondescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctiondescriptor.json'
content_hash: 'sha256:65ebea77599b7666'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLFunctionDescriptor

<sub>Class</sub>

A description of a function object to create.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLFunctionDescriptor
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [MTLIntersectionFunctionDescriptor](mtlintersectionfunctiondescriptor.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Specifying the function configuration

- [name](mtlfunctiondescriptor/name.md) — The name of the function to fetch from the library.
- [specializedName](mtlfunctiondescriptor/specializedname.md) — A new name for the created function object.
- [constantValues](mtlfunctiondescriptor/constantvalues.md) — The set of constant values assigned to the function constants.
- [options](mtlfunctiondescriptor/options.md) — Flags specifying how Metal should create the new function object.
- [binaryArchives](mtlfunctiondescriptor/binaryarchives.md) — The binary archives to search for a previously-compiled version of this function.
- [MTLFunctionOptions](mtlfunctionoptions.md) — Options that define how Metal compiles a GPU function.
- [MTLLinkedFunctions](mtllinkedfunctions.md) — A set of related functions that Metal links to when necessary to create the function instance.

## See Also

### Related Documentation

- [- newFunctionWithDescriptor:completionHandler:](<mtllibrary/makefunction(descriptor_completionhandler_).md>) — Asynchronously creates an object representing a shader function, using the specified descriptor.
- [- newFunctionWithDescriptor:error:](<mtllibrary/makefunction(descriptor_).md>) — Synchronously creates an object representing a shader function, using the specified descriptor.

### Shader functions

- [MTLFunction](mtlfunction.md) — A interface that represents a public shader function in a Metal library.
- [MTLFunctionHandle](mtlfunctionhandle.md) — An object representing a function that you can add to a visible function table.
- [MTLVisibleFunctionTableDescriptor](mtlvisiblefunctiontabledescriptor.md) — A specification of how to create a visible function table.
- [MTLVisibleFunctionTable](mtlvisiblefunctiontable.md) — A table of shader functions visible to your app that you can pass into compute commands to customize the behavior of a shader.
- [MTLIntersectionFunctionDescriptor](mtlintersectionfunctiondescriptor.md) — A description of an intersection function that performs an intersection test.
- [MTLIntersectionFunctionTableDescriptor](mtlintersectionfunctiontabledescriptor.md) — A specification of how to create an intersection function table.
- [MTLIntersectionFunctionTable](mtlintersectionfunctiontable.md) — A table of intersection functions that Metal calls to perform ray-tracing intersection tests.
