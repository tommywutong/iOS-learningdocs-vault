---
title: contents
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemittercell/contents
source_url: 'https://developer.apple.com/documentation/quartzcore/caemittercell/contents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemittercell/contents.json'
content_hash: 'sha256:483189e3d534c6ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterCell](../caemittercell.md)

# contents

<sub>Instance Property</sub>

An object that provides the contents of the layer. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var contents: Any? { get set }
```

## Discussion

A layer can set this property to a [CGImage](../../coregraphics/cgimage.md) to display the image as its contents.

The default value of this property is `nil`.

## See Also

### Providing Emitter Cell Content

- [contentsRect](contentsrect.md) — A rectangle (in the unit coordinate space) that specifies the portion of [contents](contents.md) that the receiver should draw. Animatable.
- [emitterCells](emittercells.md) — An optional array containing the sub-cells of this cell.
