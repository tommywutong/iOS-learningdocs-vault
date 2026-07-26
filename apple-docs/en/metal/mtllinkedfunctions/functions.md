---
title: functions
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtllinkedfunctions/functions
source_url: 'https://developer.apple.com/documentation/metal/mtllinkedfunctions/functions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllinkedfunctions/functions.json'
content_hash: 'sha256:175fe9d0d2665f53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLinkedFunctions](../mtllinkedfunctions.md)

# functions

<sub>Instance Property</sub>

An array of function objects to link to the new function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var functions: [any MTLFunction]? { get set }
```

## See Also

### Specifying related functions

- [binaryFunctions](binaryfunctions.md) — An array of function objects already compiled to a binary representation to link.
- [groups](groups.md) — An optional list of groups specifying which functions your shader can call at each call site.
- [privateFunctions](privatefunctions.md) — An array of function objects to link to the new function, without exporting the functions publicly.
