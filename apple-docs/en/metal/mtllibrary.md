---
title: MTLLibrary
framework: Metal
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtllibrary
source_url: 'https://developer.apple.com/documentation/metal/mtllibrary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllibrary.json'
content_hash: 'sha256:666c7c2baf387664'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLLibrary

<sub>Protocol</sub>

A collection of Metal shader functions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol MTLLibrary : NSObjectProtocol, Sendable
```

## Overview

An [MTLLibrary](mtllibrary.md) instance contains Metal shading language source code compiled during an app’s build process or at runtime from a text string.

Don’t implement this protocol yourself; instead, use the library creation methods provided by the [MTLDevice](mtldevice.md) protocol. To create an [MTLLibrary](mtllibrary.md) from a precompiled Metal library binary, call one of these [MTLDevice](mtldevice.md) methods:

- [- newDefaultLibrary](<mtldevice/makedefaultlibrary().md>)
- [- newLibraryWithFile:error:](<mtldevice/makelibrary(filepath_).md>)
- [- newLibraryWithData:error:](<mtldevice/makelibrary(data_).md>)

To create an [MTLLibrary](mtllibrary.md) by compiling source code at runtime, call one of these [MTLDevice](mtldevice.md) methods:

- [- newLibraryWithSource:options:completionHandler:](<mtldevice/makelibrary(source_options_completionhandler_).md>)
- [- newLibraryWithSource:options:error:](<mtldevice/makelibrary(source_options_).md>)

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Querying basic library attributes

- [installName](mtllibrary/installname.md) — The installation name for a dynamic library.
- [type](mtllibrary/type.md) — The library’s basic type.

### Querying library contents

- [functionNames](mtllibrary/functionnames.md) — The names of all public functions in the library.

### Creating shader function instances

- [- newFunctionWithName:](<mtllibrary/makefunction(name_).md>) — Creates an instance that represents a shader function in the library.
- [- newFunctionWithName:constantValues:completionHandler:](<mtllibrary/makefunction(name_constantvalues_completionhandler_).md>) — Asynchronously creates a specialized shader function.
- [- newFunctionWithName:constantValues:error:](<mtllibrary/makefunction(name_constantvalues_).md>) — Synchronously creates a specialized shader function.
- [- newFunctionWithDescriptor:completionHandler:](<mtllibrary/makefunction(descriptor_completionhandler_).md>) — Asynchronously creates an object representing a shader function, using the specified descriptor.
- [- newFunctionWithDescriptor:error:](<mtllibrary/makefunction(descriptor_).md>) — Synchronously creates an object representing a shader function, using the specified descriptor.

### Creating intersection function instances

- [- newIntersectionFunctionWithDescriptor:completionHandler:](<mtllibrary/makeintersectionfunction(descriptor_completionhandler_).md>) — Asynchronously creates an object representing a ray-tracing intersection function, using the specified descriptor.
- [- newIntersectionFunctionWithDescriptor:error:](<mtllibrary/makeintersectionfunction(descriptor_).md>) — Synchronously creates an object representing a ray-tracing intersection function, using the specified descriptor.

### Identifying the library

- [device](mtllibrary/device.md) — The Metal device object that created the library.
- [label](mtllibrary/label.md) — A string that identifies the library.

### Instance Methods

- [- reflectionForFunctionWithName:](<mtllibrary/reflection(functionname_).md>) — Retrieves reflection information for a function in the library.

## See Also

### Shader library management

- [MTLDynamicLibrary](mtldynamiclibrary.md) — A dynamically linkable representation of compiled shader code for a specific Metal device object.
- [MTLBinaryArchive](mtlbinaryarchive.md) — A container for pipeline state descriptors and their associated compiled shader code.
- [MTLCompileOptions](mtlcompileoptions.md) — Compilation settings for a Metal shader library.
- [MTLLibraryType](mtllibrarytype.md) — A set of options for Metal library types.
- [MTLLanguageVersion](mtllanguageversion.md) — Metal shading language versions.
- [MTLCompileSymbolVisibility](mtlcompilesymbolvisibility.md)
- [MTLLibraryOptimizationLevel](mtllibraryoptimizationlevel.md) — The optimization options for the Metal compiler.
