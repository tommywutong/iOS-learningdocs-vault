---
title: maxInstanceCount
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/maxinstancecount
source_url: 'https://developer.apple.com/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/maxinstancecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/maxinstancecount.json'
content_hash: 'sha256:c2e3ba8c15bf4274'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4IndirectInstanceAccelerationStructureDescriptor](../mtl4indirectinstanceaccelerationstructuredescriptor.md)

# maxInstanceCount

<sub>Instance Property</sub>

Controls the maximum number of instance descriptors the instance descriptor buffer can reference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxInstanceCount: Int { get set }
```

## Discussion

You are responsible for ensuring that the final number of instances at build time, which you provide indirectly via a buffer reference in [instanceCountBuffer](instancecountbuffer.md), is less than or equal to this number.
