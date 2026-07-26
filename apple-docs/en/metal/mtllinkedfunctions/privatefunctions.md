---
title: privateFunctions
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtllinkedfunctions/privatefunctions
source_url: 'https://developer.apple.com/documentation/metal/mtllinkedfunctions/privatefunctions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllinkedfunctions/privatefunctions.json'
content_hash: 'sha256:7cd8d774ff948e33'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLinkedFunctions](../mtllinkedfunctions.md)

# privateFunctions

<sub>Instance Property</sub>

An array of function objects to link to the new function, without exporting the functions publicly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var privateFunctions: [any MTLFunction]? { get set }
```

## Discussion

The pipeline doesn’t export these functions as [MTLFunctionHandle](../mtlfunctionhandle.md) instances because the Metal device doesn’t need to support function pointers to link private functions.

## See Also

### Specifying related functions

- [functions](functions.md) — An array of function objects to link to the new function.
- [binaryFunctions](binaryfunctions.md) — An array of function objects already compiled to a binary representation to link.
- [groups](groups.md) — An optional list of groups specifying which functions your shader can call at each call site.
