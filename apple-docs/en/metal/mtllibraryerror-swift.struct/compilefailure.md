---
title: compileFailure
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtllibraryerror-swift.struct/compilefailure
source_url: 'https://developer.apple.com/documentation/metal/mtllibraryerror-swift.struct/compilefailure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllibraryerror-swift.struct/compilefailure.json'
content_hash: 'sha256:3602c65732186bfa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLibraryError](../mtllibraryerror-swift.struct.md)

# compileFailure

<sub>Type Property</sub>

The library or function failed to compile.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var compileFailure: MTLLibraryError.Code { get }
```

## See Also

### Errors

- [unsupported](unsupported.md) — Metal couldn’t support the requested action.
- [internal](internal.md) — The action caused an internal error.
- [compileWarning](compilewarning.md) — The library or function compiled successfully but generated warnings.
- [fileNotFound](filenotfound.md) — Metal couldn’t find the Metal source file.
- [functionNotFound](functionnotfound.md) — Metal couldn’t find the specified Metal function.
