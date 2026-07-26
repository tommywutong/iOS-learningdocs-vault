---
title: 'setArgumentTable(_:stages:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4rendercommandencoder/setargumenttable(_:stages:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setargumenttable(_:stages:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4rendercommandencoder/setargumenttable%28_%3Astages%3A%29.json'
content_hash: 'sha256:d581f277c5ec5269'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderCommandEncoder](../mtl4rendercommandencoder.md)

# setArgumentTable(_:stages:)

<sub>Instance Method</sub>

Associates an argument table with a set of render stages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setArgumentTable(_ argumentTable: (any MTL4ArgumentTable)?, stages: MTLRenderStages)
```

## Parameters

- `argumentTable` — [MTL4ArgumentTable](../mtl4argumenttable.md) to set.

- `stages` — A [MTLRenderStages](../mtlrenderstages.md) bitmask that specifies the shader stages with visibility over the table.

## Discussion

Metal takes a snapshot of the resources in the argument table when you encode a draw, dispatch, or execute command. This snapshot becomes available to the `stages` you specify to this method.
