---
title: 'layerWillDraw(_:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayerdelegate/layerwilldraw(_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayerdelegate/layerwilldraw(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayerdelegate/layerwilldraw%28_%3A%29.json'
content_hash: 'sha256:2de0ac21c865acbc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayerDelegate](../calayerdelegate.md)

# layerWillDraw(_:)

<sub>Instance Method</sub>

Notifies the delegate of an imminent draw.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func layerWillDraw(_ layer: CALayer)
```

## Parameters

- `layer` — The layer whose contents will be drawn.

## Discussion

The [- layerWillDraw:](<layerwilldraw(__).md>) method is called before [- drawLayer:inContext:](<draw(__in_).md>). You can use this method to configure any layer state affecting contents prior to [- drawLayer:inContext:](<draw(__in_).md>) such as [contentsFormat](../calayer/contentsformat.md) and [opaque](../calayer/isopaque.md).

> [!important] Important
> This method is not called if the delegate implements [- displayLayer:](<display(__).md>).

## See Also

### Providing the Layer’s Content

- [- displayLayer:](<display(__).md>) — Tells the delegate to implement the display process.
- [- drawLayer:inContext:](<draw(__in_).md>) — Tells the delegate to implement the display process using the layer’s context.
