---
title: emitterCells
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemittercell/emittercells
source_url: 'https://developer.apple.com/documentation/quartzcore/caemittercell/emittercells'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemittercell/emittercells.json'
content_hash: 'sha256:ebbc663efe51bc22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAEmitterCell](../caemittercell.md)

# emitterCells

<sub>Instance Property</sub>

An optional array containing the sub-cells of this cell.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var emitterCells: [CAEmitterCell]? { get set }
```

## Discussion

When specified, each particle emitted by the cell acts as an emitter for each of the cell’s sub-cells. The emission point is the current particle position and the emission angle is relative to the current direction of the particle.

The default value of this property is `nil`.

The following code shows how you can create a firework style effect using sub-cells. The `fireworkCell` has an emission longitude of one quarter turn anti-clockwise to emit particles upwards. It emits `trailCell` instances which have a slight [yAcceleration](yacceleration.md) that simulates gravity.

Note that the [scale](scale.md) and [color](color.md) of `fireworkCell` are inherited by `trailCell`.

Listing 1. Creating particle trails

```swift
let image = UIImage(named: "RadialGradient.png")!.cgImage
    
let emitterLayer = CAEmitterLayer()
    
emitterLayer.emitterPosition = CGPoint(x: 512, y: 512)
    
let fireworkCell = CAEmitterCell()
fireworkCell.color = UIColor.red.cgColor
fireworkCell.birthRate = 3
fireworkCell.lifetime = 10
fireworkCell.velocity = 100
fireworkCell.scale = 0.05
fireworkCell.emissionLongitude = -CGFloat.pi * 0.5
fireworkCell.emissionRange = -CGFloat.pi * 0.25
fireworkCell.contents = image
    
let trailCell = CAEmitterCell()
trailCell.yAcceleration = 20
trailCell.birthRate = 10
trailCell.lifetime = 3
trailCell.contents = image
    
fireworkCell.emitterCells = [trailCell]
emitterLayer.emitterCells = [fireworkCell]
    
view.layer.addSublayer(emitterLayer)
```

## See Also

### Providing Emitter Cell Content

- [contents](contents.md) — An object that provides the contents of the layer. Animatable.
- [contentsRect](contentsrect.md) — A rectangle (in the unit coordinate space) that specifies the portion of [contents](contents.md) that the receiver should draw. Animatable.
