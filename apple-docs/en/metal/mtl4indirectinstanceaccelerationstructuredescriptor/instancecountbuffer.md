---
title: instanceCountBuffer
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/instancecountbuffer
source_url: 'https://developer.apple.com/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/instancecountbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/instancecountbuffer.json'
content_hash: 'sha256:389720fb9b7b9fbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4IndirectInstanceAccelerationStructureDescriptor](../mtl4indirectinstanceaccelerationstructuredescriptor.md)

# instanceCountBuffer

<sub>Instance Property</sub>

Provides a reference to a buffer containing the number of instances in the instance descriptor buffer, formatted as a 32-bit unsigned integer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var instanceCountBuffer: MTL4BufferRange { get set }
```

## Discussion

You are responsible for ensuring that the final number of instances at build time, which you provide indirectly via this buffer reference , is less than or equal to the value of property [maxInstanceCount](maxinstancecount.md).
