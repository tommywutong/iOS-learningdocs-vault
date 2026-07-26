---
title: bounds
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionrenderer/bounds
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionrenderer/bounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionrenderer/bounds.json'
content_hash: 'sha256:b202863563517f5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptionRenderer](../avcaptionrenderer.md)

# bounds

<sub>Instance Property</sub>

The drawing bounds of caption scenes.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var bounds: CGRect { get set }
```

## Discussion

Set this property value before drawing. The renderer uses the value in each call to [- renderInContext:forTime:](<render(in_for_).md>), until you change it to a new value.

## See Also

### Configuring the renderer

- [captions](captions.md) — The captions to render.
