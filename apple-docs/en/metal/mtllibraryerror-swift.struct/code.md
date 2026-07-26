---
title: MTLLibraryError.Code
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtllibraryerror-swift.struct/code
source_url: 'https://developer.apple.com/documentation/metal/mtllibraryerror-swift.struct/code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllibraryerror-swift.struct/code.json'
content_hash: 'sha256:cf391aa3536e61ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLibraryError](../mtllibraryerror-swift.struct.md)

# MTLLibraryError.Code

<sub>Enumeration</sub>

Error codes for Metal library errors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum Code
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Errors

- [MTLLibraryErrorUnsupported](code/unsupported.md) — Metal couldn’t support the requested action.
- [MTLLibraryErrorInternal](code/internal.md) — The action caused an internal error.
- [MTLLibraryErrorCompileFailure](code/compilefailure.md) — The library or function failed to compile.
- [MTLLibraryErrorCompileWarning](code/compilewarning.md) — The library or function compiled successfully but generated warnings.
- [MTLLibraryErrorFileNotFound](code/filenotfound.md) — Metal couldn’t find the Metal source file.
- [MTLLibraryErrorFunctionNotFound](code/functionnotfound.md) — Metal couldn’t find the specified Metal function.
- [MTLLibraryErrorUnsupported](code/unsupported.md) — Metal couldn’t support the requested action.
- [MTLLibraryErrorInternal](code/internal.md) — The action caused an internal error.
- [MTLLibraryErrorCompileFailure](code/compilefailure.md) — The library or function failed to compile.
- [MTLLibraryErrorCompileWarning](code/compilewarning.md) — The library or function compiled successfully but generated warnings.
- [MTLLibraryErrorFileNotFound](code/filenotfound.md) — Metal couldn’t find the Metal source file.
- [MTLLibraryErrorFunctionNotFound](code/functionnotfound.md) — Metal couldn’t find the specified Metal function.

### Initializers

- [init(rawValue:)](<code/init(rawvalue_).md>)

## See Also

### Errors

- [MTLLibraryError](../mtllibraryerror-swift.struct.md) — Metal errors related to libraries.
- [MTLLibraryErrorDomain](../mtllibraryerrordomain.md) — The error domain for Metal libraries.
