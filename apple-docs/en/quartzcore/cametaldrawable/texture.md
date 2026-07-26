---
title: texture
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametaldrawable/texture
source_url: 'https://developer.apple.com/documentation/quartzcore/cametaldrawable/texture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametaldrawable/texture.json'
content_hash: 'sha256:59c5fb1769fc53c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMetalDrawable](../cametaldrawable.md)

# texture

<sub>Instance Property</sub>

A Metal texture object that contains the drawable’s contents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var texture: any MTLTexture { get }
```

## Discussion

Use this object to configure a [MTLRenderPipelineColorAttachmentDescriptor](../../metal/mtlrenderpipelinecolorattachmentdescriptor.md) object to render to the drawable object.
