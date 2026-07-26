---
title: privateFunctionDescriptors
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4staticlinkingdescriptor/privatefunctiondescriptors
source_url: 'https://developer.apple.com/documentation/metal/mtl4staticlinkingdescriptor/privatefunctiondescriptors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4staticlinkingdescriptor/privatefunctiondescriptors.json'
content_hash: 'sha256:135887014144a6e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4StaticLinkingDescriptor](../mtl4staticlinkingdescriptor.md)

# privateFunctionDescriptors

<sub>Instance Property</sub>

Provides an array of private functions to link at the Metal IR level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var privateFunctionDescriptors: [MTL4FunctionDescriptor]? { get set }
```

## Discussion

You specify private functions to link separately from [functionDescriptors](functiondescriptors.md) because pipelines don’t export private functions as [MTLFunctionHandle](../mtlfunctionhandle.md) instances.

> [!note] Note
> You can link private functions even when your [MTLDevice](../mtldevice.md) doesn’t support function pointers.
