---
title: groups
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4staticlinkingdescriptor/groups
source_url: 'https://developer.apple.com/documentation/metal/mtl4staticlinkingdescriptor/groups'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4staticlinkingdescriptor/groups.json'
content_hash: 'sha256:71c3aeca9a1c84c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4StaticLinkingDescriptor](../mtl4staticlinkingdescriptor.md)

# groups

<sub>Instance Property</sub>

Assigns groups of functions to match call-site attributes in shader code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var groups: [String : [MTL4FunctionDescriptor]]? { get set }
```

## Discussion

Function groups help the compiler reduce the number of candidate functions it needs to evaluate for shader function calls, potentially increasing runtime performance.
