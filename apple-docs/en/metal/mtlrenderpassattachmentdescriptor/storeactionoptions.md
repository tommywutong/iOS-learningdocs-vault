---
title: storeActionOptions
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlrenderpassattachmentdescriptor/storeactionoptions
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassattachmentdescriptor/storeactionoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassattachmentdescriptor/storeactionoptions.json'
content_hash: 'sha256:a69363e52500a935'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassAttachmentDescriptor](../mtlrenderpassattachmentdescriptor.md)

# storeActionOptions

<sub>Instance Property</sub>

The options that modify the store action performed by this attachment.

> [!warning] Deprecated
> Store action options have no effect on Apple Silicon

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var storeActionOptions: MTLStoreActionOptions { get set }
```

## Discussion

This property specifies additional behavior for the store action specified by the [storeAction](storeaction.md) property.

The default value is [MTLStoreActionOptionNone](../mtlstoreactionoptions/mtlstoreactionoptionnone.md).

## See Also

### Specifying rendering pass actions

- [loadAction](loadaction.md) — The action performed by this attachment at the start of a rendering pass for a render command encoder.
- [storeAction](storeaction.md) — The action performed by this attachment at the end of a rendering pass for a render command encoder.
