---
title: groups
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtllinkedfunctions/groups
source_url: 'https://developer.apple.com/documentation/metal/mtllinkedfunctions/groups'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllinkedfunctions/groups.json'
content_hash: 'sha256:d68c86e00f520597'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLinkedFunctions](../mtllinkedfunctions.md)

# groups

<sub>Instance Property</sub>

An optional list of groups specifying which functions your shader can call at each call site.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var groups: [String : [any MTLFunction]]? { get set }
```

## Discussion

The default value is `nil`.

The default behavior is conservative and assumes that your shader can call any linked function from every call site. If you know that the shader can only call a limited subset of functions at a call site, you can annotate those sites in the shader with a name of a group and then specify the list of functions for that call site using this property. Specifying call sites and callable functions more precisely can improve performance.

For more information on how to specify call site groups, see [Metal Shading Language Specification](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).

The value of this property is a dictionary whose keys are call site names and values are arrays specifying the list of functions that the shader can call from each site.

## See Also

### Specifying related functions

- [functions](functions.md) — An array of function objects to link to the new function.
- [binaryFunctions](binaryfunctions.md) — An array of function objects already compiled to a binary representation to link.
- [privateFunctions](privatefunctions.md) — An array of function objects to link to the new function, without exporting the functions publicly.
