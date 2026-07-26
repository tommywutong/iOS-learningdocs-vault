---
title: MTLNewLibraryCompletionHandler
framework: Metal
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlnewlibrarycompletionhandler
source_url: 'https://developer.apple.com/documentation/metal/mtlnewlibrarycompletionhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlnewlibrarycompletionhandler.json'
content_hash: 'sha256:11641e39be81c2ce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLNewLibraryCompletionHandler

<sub>Type Alias</sub>

A completion handler signature a method calls when it finishes creating a Metal library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
typealias MTLNewLibraryCompletionHandler = ((any MTLLibrary)?, (any Error)?) -> Void
```

## Parameters

- `library` — An [MTLLibrary](mtllibrary.md) instance if the method successfully compiles the library without any errors; otherwise `nil`.

- `error` — An error instance if the compiler generates any errors; otherwise `nil`.

## Discussion

The framework reports compiler warnings to the console. The `error` parameter doesn’t report warnings because it’s `nil` when there aren’t any compiler errors.

## See Also

### Creating shader libraries

- [- newDefaultLibrary](<mtldevice/makedefaultlibrary().md>) — Creates a Metal library instance that contains the functions from your app’s default Metal library.
- [- newDefaultLibraryWithBundle:error:](<mtldevice/makedefaultlibrary(bundle_).md>) — Creates a Metal library instance that contains the functions in a bundle’s default Metal library.
- [- newLibraryWithURL:error:](<mtldevice/makelibrary(url_).md>) — Creates a Metal library instance that contains the functions in the Metal library file at a URL.
- [- newLibraryWithSource:options:error:](<mtldevice/makelibrary(source_options_).md>) — Synchronously creates a Metal library instance by compiling the functions in a source string.
- [- newLibraryWithSource:options:completionHandler:](<mtldevice/makelibrary(source_options_completionhandler_).md>) — Asynchronously creates a Metal library instance by compiling the functions in a source string.
- [- newLibraryWithStitchedDescriptor:error:](<mtldevice/makelibrary(stitcheddescriptor_).md>) — Synchronously creates a Metal library from the function stitching graphs in a descriptor.
- [- newLibraryWithStitchedDescriptor:completionHandler:](<mtldevice/makelibrary(stitcheddescriptor_completionhandler_).md>) — Asynchronously creates a Metal library from the function stitching graphs in a descriptor.
- [makeLibrary(data:)](<mtldevice/makelibrary(data_)-7khmh.md>) — Creates a Metal library instance that contains the functions in a precompiled Metal library.
- [- newLibraryWithData:error:](<mtldevice/makelibrary(data_).md>) — Creates a Metal library instance from a dispatch-data instance that contains the functions in a precompiled Metal library.
- [- newLibraryWithFile:error:](<mtldevice/makelibrary(filepath_).md>) — Creates a Metal library instance that contains the functions in the Metal library file at a file path. _(deprecated)_
