---
title: contentsRect
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemittercell/contentsrect
source_url: 'https://developer.apple.com/documentation/quartzcore/caemittercell/contentsrect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemittercell/contentsrect.json'
content_hash: 'sha256:d018920fc91a78de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterCell](../caemittercell.md)

# contentsRect

<sub>Instance Property</sub>

A rectangle (in the unit coordinate space) that specifies the portion of [contents](contents.md) that the receiver should draw. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var contentsRect: CGRect { get set }
```

## Discussion

By default, this property is set to the unit rectangle (0.0,0.0,1.0,1.0), which results in all of the layer’s contents being drawn.

If pixels outside the unit rectangle are requested, the edge pixels of the contents image are extended outwards.

If you assign an empty rectangle to this property, the results are undefined.

## See Also

### Providing Emitter Cell Content

- [contents](contents.md) — An object that provides the contents of the layer. Animatable.
- [emitterCells](emittercells.md) — An optional array containing the sub-cells of this cell.
