---
title: 'makeLibrary(stitchedDescriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makelibrary(stitcheddescriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makelibrary(stitcheddescriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makelibrary%28stitcheddescriptor%3A%29.json'
content_hash: 'sha256:2f07e81795e25325'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeLibrary(stitchedDescriptor:)

<sub>Instance Method</sub>

Synchronously creates a Metal library from the function stitching graphs in a descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeLibrary(stitchedDescriptor descriptor: MTLStitchedLibraryDescriptor) throws -> any MTLLibrary
```

## Parameters

- `descriptor` — An [MTLStitchedLibraryDescriptor](../mtlstitchedlibrarydescriptor.md) instance.

## Return Value

A new [MTLLibrary](../mtllibrary.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## See Also

### Creating shader libraries

- [- newDefaultLibrary](<makedefaultlibrary().md>) — Creates a Metal library instance that contains the functions from your app’s default Metal library.
- [- newDefaultLibraryWithBundle:error:](<makedefaultlibrary(bundle_).md>) — Creates a Metal library instance that contains the functions in a bundle’s default Metal library.
- [- newLibraryWithURL:error:](<makelibrary(url_).md>) — Creates a Metal library instance that contains the functions in the Metal library file at a URL.
- [- newLibraryWithSource:options:error:](<makelibrary(source_options_).md>) — Synchronously creates a Metal library instance by compiling the functions in a source string.
- [- newLibraryWithSource:options:completionHandler:](<makelibrary(source_options_completionhandler_).md>) — Asynchronously creates a Metal library instance by compiling the functions in a source string.
- [- newLibraryWithStitchedDescriptor:completionHandler:](<makelibrary(stitcheddescriptor_completionhandler_).md>) — Asynchronously creates a Metal library from the function stitching graphs in a descriptor.
- [makeLibrary(data:)](<makelibrary(data_)-7khmh.md>) — Creates a Metal library instance that contains the functions in a precompiled Metal library.
- [- newLibraryWithData:error:](<makelibrary(data_).md>) — Creates a Metal library instance from a dispatch-data instance that contains the functions in a precompiled Metal library.
- [MTLNewLibraryCompletionHandler](../mtlnewlibrarycompletionhandler.md) — A completion handler signature a method calls when it finishes creating a Metal library.
- [- newLibraryWithFile:error:](<makelibrary(filepath_).md>) — Creates a Metal library instance that contains the functions in the Metal library file at a file path. _(deprecated)_
