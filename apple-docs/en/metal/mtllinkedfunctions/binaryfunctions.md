---
title: binaryFunctions
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtllinkedfunctions/binaryfunctions
source_url: 'https://developer.apple.com/documentation/metal/mtllinkedfunctions/binaryfunctions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllinkedfunctions/binaryfunctions.json'
content_hash: 'sha256:7d13970a8bb985f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLinkedFunctions](../mtllinkedfunctions.md)

# binaryFunctions

<sub>Instance Property</sub>

An array of function objects already compiled to a binary representation to link.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var binaryFunctions: [any MTLFunction]? { get set }
```

## See Also

### Specifying related functions

- [functions](functions.md) — An array of function objects to link to the new function.
- [groups](groups.md) — An optional list of groups specifying which functions your shader can call at each call site.
- [privateFunctions](privatefunctions.md) — An array of function objects to link to the new function, without exporting the functions publicly.
