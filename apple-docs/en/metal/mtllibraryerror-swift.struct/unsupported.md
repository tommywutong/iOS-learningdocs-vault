---
title: unsupported
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/metal/mtllibraryerror-swift.struct/unsupported
source_url: 'https://developer.apple.com/documentation/metal/mtllibraryerror-swift.struct/unsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllibraryerror-swift.struct/unsupported.json'
content_hash: 'sha256:3151ba778fa1d8b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLibraryError](../mtllibraryerror-swift.struct.md)

# unsupported

<sub>Type Property</sub>

Metal couldn’t support the requested action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var unsupported: MTLLibraryError.Code { get }
```

## Discussion

For example, the requested library file has improper formatting, or the requested library isn’t accessible.

## See Also

### Errors

- [internal](internal.md) — The action caused an internal error.
- [compileFailure](compilefailure.md) — The library or function failed to compile.
- [compileWarning](compilewarning.md) — The library or function compiled successfully but generated warnings.
- [fileNotFound](filenotfound.md) — Metal couldn’t find the Metal source file.
- [functionNotFound](functionnotfound.md) — Metal couldn’t find the specified Metal function.
