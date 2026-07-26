---
title: 'setResource(_:bufferIndex:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4argumenttable/setresource(_:bufferindex:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4argumenttable/setresource(_:bufferindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4argumenttable/setresource%28_%3Abufferindex%3A%29.json'
content_hash: 'sha256:c8ade28aea486307'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ArgumentTable](../mtl4argumenttable.md)

# setResource(_:bufferIndex:)

<sub>Instance Method</sub>

Binds a resource to a buffer binding slot.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setResource(_ resourceID: MTLResourceID, bufferIndex bindingIndex: Int)
```

## Parameters

- `resourceID` — The [MTLResourceID](../mtlresourceid.md) of the Metal resource to bind.

- `bindingIndex` — A valid binding index in the buffer binding range. It is an error for this value to match or exceed the value of property [maxBufferBindCount](../mtl4argumenttabledescriptor/maxbufferbindcount.md) on the descriptor from which you created this argument table.
