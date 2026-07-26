---
title: MTLDynamicLibraryError.Code
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldynamiclibraryerror-swift.struct/code
source_url: 'https://developer.apple.com/documentation/metal/mtldynamiclibraryerror-swift.struct/code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldynamiclibraryerror-swift.struct/code.json'
content_hash: 'sha256:4d65fc96e4841d7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDynamicLibraryError](../mtldynamiclibraryerror-swift.struct.md)

# MTLDynamicLibraryError.Code

<sub>Enumeration</sub>

Error codes that Metal can generate when creating dynamic libraries.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum Code
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Error codes

- [MTLDynamicLibraryErrorNone](code/none.md) — An error code that represents the absence of any problems.
- [MTLDynamicLibraryErrorInvalidFile](code/invalidfile.md) — An error code that indicates an app is using an invalid reference to a library file, typically related to a URL.
- [MTLDynamicLibraryErrorCompilationFailure](code/compilationfailure.md) — An error code that indicates Metal couldn’t compile a dynamic library.
- [MTLDynamicLibraryErrorUnresolvedInstallName](code/unresolvedinstallname.md) — An error code that indicates Metal couldn’t resolve the installation name for a new dynamic library.
- [MTLDynamicLibraryErrorDependencyLoadFailure](code/dependencyloadfailure.md) — An error code that indicates a dynamic library couldn’t link to other dynamic libraries.
- [MTLDynamicLibraryErrorUnsupported](code/unsupported.md) — An error code that indicates the GPU device doesn’t support dynamic libraries.
- [MTLDynamicLibraryErrorNone](code/none.md) — An error code that represents the absence of any problems.
- [MTLDynamicLibraryErrorInvalidFile](code/invalidfile.md) — An error code that indicates an app is using an invalid reference to a library file, typically related to a URL.
- [MTLDynamicLibraryErrorCompilationFailure](code/compilationfailure.md) — An error code that indicates Metal couldn’t compile a dynamic library.
- [MTLDynamicLibraryErrorUnresolvedInstallName](code/unresolvedinstallname.md) — An error code that indicates Metal couldn’t resolve the installation name for a new dynamic library.
- [MTLDynamicLibraryErrorDependencyLoadFailure](code/dependencyloadfailure.md) — An error code that indicates a dynamic library couldn’t link to other dynamic libraries.
- [MTLDynamicLibraryErrorUnsupported](code/unsupported.md) — An error code that indicates the GPU device doesn’t support dynamic libraries.

### Initializers

- [init(rawValue:)](<code/init(rawvalue_).md>)

## See Also

### Error codes

- [none](none.md) — An error code that represents the absence of any problems.
- [invalidFile](invalidfile.md) — An error code that indicates an app is using an invalid reference to a library file, typically related to a URL.
- [compilationFailure](compilationfailure.md) — An error code that indicates Metal couldn’t compile a dynamic library.
- [unresolvedInstallName](unresolvedinstallname.md) — An error code that indicates Metal couldn’t resolve the installation name for a new dynamic library.
- [dependencyLoadFailure](dependencyloadfailure.md) — An error code that indicates a dynamic library couldn’t link to other dynamic libraries.
- [unsupported](unsupported.md) — An error code that indicates the GPU device doesn’t support dynamic libraries.
