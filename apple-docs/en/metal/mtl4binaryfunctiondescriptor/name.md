---
title: name
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4binaryfunctiondescriptor/name
source_url: 'https://developer.apple.com/documentation/metal/mtl4binaryfunctiondescriptor/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4binaryfunctiondescriptor/name.json'
content_hash: 'sha256:2d72bd747ea85f6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4BinaryFunctionDescriptor](../mtl4binaryfunctiondescriptor.md)

# name

<sub>Instance Property</sub>

Associates a string that uniquely identifies a binary function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var name: String { get set }
```

## Discussion

You can use this property to look up a corresponding binary function by name in a [MTL4Archive](../mtl4archive.md) instance.
