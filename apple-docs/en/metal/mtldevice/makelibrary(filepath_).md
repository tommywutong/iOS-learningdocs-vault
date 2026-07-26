---
title: 'makeLibrary(filepath:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.11+（13.0 起废弃）, tvOS（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtldevice/makelibrary(filepath:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makelibrary(filepath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makelibrary%28filepath%3A%29.json'
content_hash: 'sha256:68e4b8b14a65ca8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeLibrary(filepath:)

<sub>Instance Method</sub>

Creates a Metal library instance that contains the functions in the Metal library file at a file path.

> [!warning] Deprecated
> Use [- newLibraryWithURL:error:](<makelibrary(url_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeLibrary(filepath: String) throws -> any MTLLibrary
```

## Parameters

- `filepath` — A string of the absolute file path to a Metal library file (ending in `.metallib`).

## Return Value

A new [MTLLibrary](../mtllibrary.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## See Also

### Creating shader libraries

- [- newDefaultLibrary](<makedefaultlibrary().md>) — Creates a Metal library instance that contains the functions from your app’s default Metal library.
- [- newDefaultLibraryWithBundle:error:](<makedefaultlibrary(bundle_).md>) — Creates a Metal library instance that contains the functions in a bundle’s default Metal library.
- [- newLibraryWithURL:error:](<makelibrary(url_).md>) — Creates a Metal library instance that contains the functions in the Metal library file at a URL.
- [- newLibraryWithSource:options:error:](<makelibrary(source_options_).md>) — Synchronously creates a Metal library instance by compiling the functions in a source string.
- [- newLibraryWithSource:options:completionHandler:](<makelibrary(source_options_completionhandler_).md>) — Asynchronously creates a Metal library instance by compiling the functions in a source string.
- [- newLibraryWithStitchedDescriptor:error:](<makelibrary(stitcheddescriptor_).md>) — Synchronously creates a Metal library from the function stitching graphs in a descriptor.
- [- newLibraryWithStitchedDescriptor:completionHandler:](<makelibrary(stitcheddescriptor_completionhandler_).md>) — Asynchronously creates a Metal library from the function stitching graphs in a descriptor.
- [makeLibrary(data:)](<makelibrary(data_)-7khmh.md>) — Creates a Metal library instance that contains the functions in a precompiled Metal library.
- [- newLibraryWithData:error:](<makelibrary(data_).md>) — Creates a Metal library instance from a dispatch-data instance that contains the functions in a precompiled Metal library.
- [MTLNewLibraryCompletionHandler](../mtlnewlibrarycompletionhandler.md) — A completion handler signature a method calls when it finishes creating a Metal library.
