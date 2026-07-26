---
title: MTLLibraryError
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtllibraryerror-swift.struct
source_url: 'https://developer.apple.com/documentation/metal/mtllibraryerror-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllibraryerror-swift.struct.json'
content_hash: 'sha256:7182c8ab6e07dfae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLLibraryError

<sub>Structure</sub>

Metal errors related to libraries.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLLibraryError
```

## Relationships

- **Conforms To**: [CustomNSError](../foundation/customnserror.md), [Equatable](../swift/equatable.md), [Error](../swift/error.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Errors

- [unsupported](mtllibraryerror-swift.struct/unsupported.md) — Metal couldn’t support the requested action.
- [internal](mtllibraryerror-swift.struct/internal.md) — The action caused an internal error.
- [compileFailure](mtllibraryerror-swift.struct/compilefailure.md) — The library or function failed to compile.
- [compileWarning](mtllibraryerror-swift.struct/compilewarning.md) — The library or function compiled successfully but generated warnings.
- [fileNotFound](mtllibraryerror-swift.struct/filenotfound.md) — Metal couldn’t find the Metal source file.
- [functionNotFound](mtllibraryerror-swift.struct/functionnotfound.md) — Metal couldn’t find the specified Metal function.

### Error domain

- [errorDomain](mtllibraryerror-swift.struct/errordomain.md) — The error domain used by Metal when returning library or function creation errors.

## See Also

### Errors

- [Code](mtllibraryerror-swift.struct/code.md) — Error codes for Metal library errors.
- [MTLLibraryErrorDomain](mtllibraryerrordomain.md) — The error domain for Metal libraries.
