---
title: 'subscript(_:)'
framework: Metal
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrenderpasscolorattachmentdescriptorarray/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpasscolorattachmentdescriptorarray/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpasscolorattachmentdescriptorarray/subscript%28_%3A%29.json'
content_hash: 'sha256:791a4adf342b4a5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassColorAttachmentDescriptorArray](../mtlrenderpasscolorattachmentdescriptorarray.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns the descriptor object for the specified color attachment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
subscript(attachmentIndex: Int) -> MTLRenderPassColorAttachmentDescriptor! { get set }
```

## Parameters

- `attachmentIndex` — An index in the color attachment array.

## Return Value

A descriptor object that contains color attachment information.
