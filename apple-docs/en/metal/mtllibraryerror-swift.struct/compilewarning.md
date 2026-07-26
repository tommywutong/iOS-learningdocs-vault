---
title: compileWarning
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtllibraryerror-swift.struct/compilewarning
source_url: 'https://developer.apple.com/documentation/metal/mtllibraryerror-swift.struct/compilewarning'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllibraryerror-swift.struct/compilewarning.json'
content_hash: 'sha256:10af615525f80496'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLibraryError](../mtllibraryerror-swift.struct.md)

# compileWarning

<sub>Type Property</sub>

The library or function compiled successfully but generated warnings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var compileWarning: MTLLibraryError.Code { get }
```

## See Also

### Errors

- [unsupported](unsupported.md) — Metal couldn’t support the requested action.
- [internal](internal.md) — The action caused an internal error.
- [compileFailure](compilefailure.md) — The library or function failed to compile.
- [fileNotFound](filenotfound.md) — Metal couldn’t find the Metal source file.
- [functionNotFound](functionnotfound.md) — Metal couldn’t find the specified Metal function.
