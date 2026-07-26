---
title: resuming
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtl4renderencoderoptions/resuming
source_url: 'https://developer.apple.com/documentation/metal/mtl4renderencoderoptions/resuming'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4renderencoderoptions/resuming.json'
content_hash: 'sha256:5656b0e88b3e49c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4RenderEncoderOptions](../mtl4renderencoderoptions.md)

# resuming

<sub>Type Property</sub>

Configures the render pass to as _resuming_.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var resuming: MTL4RenderEncoderOptions { get }
```

## Discussion

Pass this option to [- renderCommandEncoderWithDescriptor:options:](<../mtl4commandbuffer/makerendercommandencoder(descriptor_options_).md>) to specify that Metal can stitch the work a render command encoder encodes with a prior “suspending” render command encoder.
