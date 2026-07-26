---
title: none
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldynamiclibraryerror-swift.struct/none
source_url: 'https://developer.apple.com/documentation/metal/mtldynamiclibraryerror-swift.struct/none'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldynamiclibraryerror-swift.struct/none.json'
content_hash: 'sha256:e66782c9e3af2a15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDynamicLibraryError](../mtldynamiclibraryerror-swift.struct.md)

# none

<sub>Type Property</sub>

An error code that represents the absence of any problems.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var none: MTLDynamicLibraryError.Code { get }
```

## See Also

### Error codes

- [invalidFile](invalidfile.md) — An error code that indicates an app is using an invalid reference to a library file, typically related to a URL.
- [compilationFailure](compilationfailure.md) — An error code that indicates Metal couldn’t compile a dynamic library.
- [unresolvedInstallName](unresolvedinstallname.md) — An error code that indicates Metal couldn’t resolve the installation name for a new dynamic library.
- [dependencyLoadFailure](dependencyloadfailure.md) — An error code that indicates a dynamic library couldn’t link to other dynamic libraries.
- [unsupported](unsupported.md) — An error code that indicates the GPU device doesn’t support dynamic libraries.
- [Code](code.md) — Error codes that Metal can generate when creating dynamic libraries.
