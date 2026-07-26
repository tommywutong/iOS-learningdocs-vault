---
title: Shader library and archive creation
framework: Metal
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/shader-library-and-archive-creation
source_url: 'https://developer.apple.com/documentation/metal/shader-library-and-archive-creation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/shader-library-and-archive-creation.json'
content_hash: 'sha256:dfd5354e71192fe0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md) · [GPU devices and work submission](gpu-devices-and-work-submission.md) · [MTLDevice](mtldevice.md)

# Shader library and archive creation

<sub>API Collection</sub>

Create static and dynamic shader libraries, and binary shader archives.

## Topics

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
- [MTLNewLibraryCompletionHandler](mtlnewlibrarycompletionhandler.md) — A completion handler signature a method calls when it finishes creating a Metal library.
- [- newLibraryWithFile:error:](<mtldevice/makelibrary(filepath_).md>) — Creates a Metal library instance that contains the functions in the Metal library file at a file path. _(deprecated)_

### Creating dynamic shader libraries

- [supportsDynamicLibraries](mtldevice/supportsdynamiclibraries.md) — A Boolean value that indicates whether the GPU device can create and use dynamic libraries in compute pipelines.
- [supportsRenderDynamicLibraries](mtldevice/supportsrenderdynamiclibraries.md) — A Boolean value that indicates whether the GPU device can create and use dynamic libraries in render pipelines.
- [- newDynamicLibrary:error:](<mtldevice/makedynamiclibrary(library_).md>) — Creates a Metal dynamic library instance from a Metal library instance.
- [- newDynamicLibraryWithURL:error:](<mtldevice/makedynamiclibrary(url_).md>) — Creates a Metal dynamic library instance that contains the functions in the Metal library file at a URL.
- [Code](mtldynamiclibraryerror-swift.struct/code.md) — Error codes that Metal can generate when creating dynamic libraries.
- [MTLDynamicLibraryDomain](mtldynamiclibrarydomain.md) — The domain for Metal dynamic library errors.

### Creating binary shader archives

- [- newBinaryArchiveWithDescriptor:error:](<mtldevice/makebinaryarchive(descriptor_).md>) — Creates a Metal binary archive instance.
- [MTLBinaryArchiveDescriptor](mtlbinaryarchivedescriptor.md) — A description of a binary shader archive that you want to create.
- [Code](mtlbinaryarchiveerror-swift.struct/code.md) — Error codes when creating binary archives of compiled shader code.
- [MTLBinaryArchiveDomain](mtlbinaryarchivedomain.md) — The domain for Metal binary archive errors.

## See Also

### Working with GPU devices

- [Device inspection](device-inspection.md) — Locate and identify a GPU and the features it supports, and sample its counters.
- [Work submission](work-submission.md) — Create queues that submit work to the GPU or load assets into GPU resources, and indirect command buffers that group your frequent commands together.
- [Pipeline state creation](pipeline-state-creation.md) — Create pipeline states for render and compute passes, samplers, depth and stencil states, and indirect command buffers.
- [Resource creation](resource-creation.md) — Load assets with input/output queues and make various resource instances, such as buffers, textures, acceleration structures, and memory heaps.
