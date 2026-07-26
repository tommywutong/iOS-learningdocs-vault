---
title: CAEmitterLayer
framework: Core Animation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemitterlayer
source_url: 'https://developer.apple.com/documentation/quartzcore/caemitterlayer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemitterlayer.json'
content_hash: 'sha256:192125150d6baaf4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAEmitterLayer

<sub>Class</sub>

A layer that emits, animates, and renders a particle system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CAEmitterLayer
```

## Overview

The particles, defined by instances of [CAEmitterCell](caemittercell.md), are drawn above the layer’s background color and border.

The following code shows how to set up a simple point (the default [emitterShape](caemitterlayer/emittershape.md) is [kCAEmitterLayerPoint](caemitterlayeremittershape/point.md)) particle emitter. It uses an image named `RadialGradient.png` as the cell contents and, by setting the emitter cell’s [emissionRange](caemittercell/emissionrange.md) to `2` × [pi](../swift/floatingpoint/pi.md), the particles are emitted in all directions.

```swift
let emitterLayer = CAEmitterLayer()
    
emitterLayer.emitterPosition = CGPoint(x: 320, y: 320)
    
let cell = CAEmitterCell()
cell.birthRate = 100
cell.lifetime = 10
cell.velocity = 100
cell.scale = 0.1
    
cell.emissionRange = CGFloat.pi * 2.0
cell.contents = UIImage(named: "RadialGradient.png")!.cgImage
    
emitterLayer.emitterCells = [cell]
    
view.layer.addSublayer(emitterLayer)
```

## Relationships

- **Inherits From**: [CALayer](calayer.md)

- **Conforms To**: [CAMediaTiming](camediatiming.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Specifying Particle Emitter Cells

- [emitterCells](caemitterlayer/emittercells.md) — The array emitter cells attached to the layer.

### Emitter Geometry

- [renderMode](caemitterlayer/rendermode.md) — Defines how particle cells are rendered into the layer.
- [emitterPosition](caemitterlayer/emitterposition.md) — The position of the center of the particle emitter. Animatable.
- [emitterShape](caemitterlayer/emittershape.md) — Specifies the emitter shape.
- [emitterZPosition](caemitterlayer/emitterzposition.md) — Specifies the center of the particle emitter shape along the z-axis. Animatable.
- [emitterDepth](caemitterlayer/emitterdepth.md) — Determines the depth of the emitter shape.
- [emitterSize](caemitterlayer/emittersize.md) — Determines the size of the particle emitter shape. Animatable.

### Emitter Cell Attribute Multipliers

- [scale](caemitterlayer/scale.md) — Defines a multiplier applied to the cell-defined particle scale.
- [seed](caemitterlayer/seed.md) — Specifies the seed used to initialize the random number generator.
- [spin](caemitterlayer/spin.md) — Defines a multiplier applied to the cell-defined particle spin. Animatable.
- [velocity](caemitterlayer/velocity.md) — Defines a multiplier applied to the cell-defined particle velocity. Animatable.
- [birthRate](caemitterlayer/birthrate.md) — Defines a multiplier that is applied to the cell-defined birth rate. Animatable
- [emitterMode](caemitterlayer/emittermode.md) — Specifies the emitter mode.
- [lifetime](caemitterlayer/lifetime.md) — Defines a multiplier applied to the cell-defined lifetime range when particles are created. Animatable.
- [preservesDepth](caemitterlayer/preservesdepth.md) — Defines whether the layer flattens the particles into its plane.

### Constants

- [Emitter Shape](emitter-shape.md) — The emission shape is a one, two or three dimensional shape that defines where the emitted particles originate. The shapes are defined by a subset of [emitterPosition](caemitterlayer/emitterposition.md), [emitterZPosition](caemitterlayer/emitterzposition.md), [emitterSize](caemitterlayer/emittersize.md) and [emitterDepth](caemitterlayer/emitterdepth.md) properties.
- [Emitter Modes](emitter-modes.md) — These constants specify the possible emitter modes. They are used by the [emitterMode](caemitterlayer/emittermode.md) property.
- [Emitter Render Order](emitter-render-order.md) — These constants specify the order that emitter cells are composited. They are used by the [renderMode](caemitterlayer/rendermode.md) property.

## See Also

### Particle Systems

- [CAEmitterCell](caemittercell.md) — The definition of a particle emitted by a particle layer.
