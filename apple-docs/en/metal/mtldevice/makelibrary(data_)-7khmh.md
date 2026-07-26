---
title: 'makeLibrary(data:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.11+, tvOS 8.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makelibrary(data:)-7khmh'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makelibrary(data:)-7khmh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makelibrary%28data%3A%29-7khmh.json'
content_hash: 'sha256:6403210a965b286a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeLibrary(data:)

<sub>Instance Method</sub>

Creates a Metal library instance that contains the functions in a precompiled Metal library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeLibrary(data: DispatchData) throws -> any MTLLibrary
```

## Parameters

- `data` — The data from a precompiled Metal library. For more information, see [Building a shader library by precompiling source files](../building-a-shader-library-by-precompiling-source-files.md).

## Return Value

A new [MTLLibrary](../mtllibrary.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## Discussion

Use this method if your application manages its own archiving system for libraries — for example, if your app uses a single file that contains several libraries.

> [!note] Note
> This is a Swift default implementation for the [- newLibraryWithData:error:](<makelibrary(data_).md>) method.

## See Also

### Creating shader libraries

- [- newDefaultLibrary](<makedefaultlibrary().md>) — Creates a Metal library instance that contains the functions from your app’s default Metal library.
- [- newDefaultLibraryWithBundle:error:](<makedefaultlibrary(bundle_).md>) — Creates a Metal library instance that contains the functions in a bundle’s default Metal library.
- [- newLibraryWithURL:error:](<makelibrary(url_).md>) — Creates a Metal library instance that contains the functions in the Metal library file at a URL.
- [- newLibraryWithSource:options:error:](<makelibrary(source_options_).md>) — Synchronously creates a Metal library instance by compiling the functions in a source string.
- [- newLibraryWithSource:options:completionHandler:](<makelibrary(source_options_completionhandler_).md>) — Asynchronously creates a Metal library instance by compiling the functions in a source string.
- [- newLibraryWithStitchedDescriptor:error:](<makelibrary(stitcheddescriptor_).md>) — Synchronously creates a Metal library from the function stitching graphs in a descriptor.
- [- newLibraryWithStitchedDescriptor:completionHandler:](<makelibrary(stitcheddescriptor_completionhandler_).md>) — Asynchronously creates a Metal library from the function stitching graphs in a descriptor.
- [- newLibraryWithData:error:](<makelibrary(data_).md>) — Creates a Metal library instance from a dispatch-data instance that contains the functions in a precompiled Metal library.
- [MTLNewLibraryCompletionHandler](../mtlnewlibrarycompletionhandler.md) — A completion handler signature a method calls when it finishes creating a Metal library.
- [- newLibraryWithFile:error:](<makelibrary(filepath_).md>) — Creates a Metal library instance that contains the functions in the Metal library file at a file path. _(deprecated)_
