---
title: 'makeLibrary(source:options:completionHandler:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makelibrary(source:options:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makelibrary(source:options:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makelibrary%28source%3Aoptions%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:18e323aafcd78877'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeLibrary(source:options:completionHandler:)

<sub>Instance Method</sub>

Asynchronously creates a Metal library instance by compiling the functions in a source string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeLibrary(source: String, options: MTLCompileOptions?, completionHandler: @escaping @Sendable ((any MTLLibrary)?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeLibrary(source: String, options: MTLCompileOptions?) async throws -> any MTLLibrary
```

## Parameters

- `source` — A string that contains source code for one or more Metal functions. For information about writing source in Metal Shading Language (MSL), see the [Metal Shading Language Specification](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).

- `options` — An [MTLCompileOptions](../mtlcompileoptions.md) instance that affects the compilation of the source code in the string.

- `completionHandler` — A Swift closure or an Objective-C block the method calls when the library finishes loading.

## Discussion

Because there’s no search path to find other functions, the source may only import the Metal default library.

## See Also

### Creating shader libraries

- [- newDefaultLibrary](<makedefaultlibrary().md>) — Creates a Metal library instance that contains the functions from your app’s default Metal library.
- [- newDefaultLibraryWithBundle:error:](<makedefaultlibrary(bundle_).md>) — Creates a Metal library instance that contains the functions in a bundle’s default Metal library.
- [- newLibraryWithURL:error:](<makelibrary(url_).md>) — Creates a Metal library instance that contains the functions in the Metal library file at a URL.
- [- newLibraryWithSource:options:error:](<makelibrary(source_options_).md>) — Synchronously creates a Metal library instance by compiling the functions in a source string.
- [- newLibraryWithStitchedDescriptor:error:](<makelibrary(stitcheddescriptor_).md>) — Synchronously creates a Metal library from the function stitching graphs in a descriptor.
- [- newLibraryWithStitchedDescriptor:completionHandler:](<makelibrary(stitcheddescriptor_completionhandler_).md>) — Asynchronously creates a Metal library from the function stitching graphs in a descriptor.
- [makeLibrary(data:)](<makelibrary(data_)-7khmh.md>) — Creates a Metal library instance that contains the functions in a precompiled Metal library.
- [- newLibraryWithData:error:](<makelibrary(data_).md>) — Creates a Metal library instance from a dispatch-data instance that contains the functions in a precompiled Metal library.
- [MTLNewLibraryCompletionHandler](../mtlnewlibrarycompletionhandler.md) — A completion handler signature a method calls when it finishes creating a Metal library.
- [- newLibraryWithFile:error:](<makelibrary(filepath_).md>) — Creates a Metal library instance that contains the functions in the Metal library file at a file path. _(deprecated)_
