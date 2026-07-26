---
title: fileNotFound
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtllibraryerror-swift.struct/filenotfound
source_url: 'https://developer.apple.com/documentation/metal/mtllibraryerror-swift.struct/filenotfound'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllibraryerror-swift.struct/filenotfound.json'
content_hash: 'sha256:3c33795983296764'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLibraryError](../mtllibraryerror-swift.struct.md)

# fileNotFound

<sub>Type Property</sub>

Metal couldn’t find the Metal source file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var fileNotFound: MTLLibraryError.Code { get }
```

## See Also

### Errors

- [unsupported](unsupported.md) — Metal couldn’t support the requested action.
- [internal](internal.md) — The action caused an internal error.
- [compileFailure](compilefailure.md) — The library or function failed to compile.
- [compileWarning](compilewarning.md) — The library or function compiled successfully but generated warnings.
- [functionNotFound](functionnotfound.md) — Metal couldn’t find the specified Metal function.
