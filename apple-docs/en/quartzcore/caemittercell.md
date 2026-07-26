---
title: CAEmitterCell
framework: Core Animation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caemittercell
source_url: 'https://developer.apple.com/documentation/quartzcore/caemittercell'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caemittercell.json'
content_hash: 'sha256:a9f5101bf3f480ff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAEmitterCell

<sub>Class</sub>

The definition of a particle emitted by a particle layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CAEmitterCell
```

## Overview

The [CAEmitterCell](caemittercell.md) class represents one source of particles being emitted by a [CAEmitterLayer](caemitterlayer.md) object. An emitter cell defines the direction and properties of the emitted particles. Emitter cells can have an array of sub-cells, which lets the particles themselves emit particles.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CAMediaTiming](camediatiming.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Providing Emitter Cell Content

- [contents](caemittercell/contents.md) — An object that provides the contents of the layer. Animatable.
- [contentsRect](caemittercell/contentsrect.md) — A rectangle (in the unit coordinate space) that specifies the portion of [contents](caemittercell/contents.md) that the receiver should draw. Animatable.
- [emitterCells](caemittercell/emittercells.md) — An optional array containing the sub-cells of this cell.

### Setting Emitter Cell Visual Attributes

- [enabled](caemittercell/isenabled.md) — A Boolean value indicating whether or not cells from this emitter are rendered.
- [color](caemittercell/color.md) — The color of each emitted object. Animatable.
- [redRange](caemittercell/redrange.md) — The amount by which the red color component of the cell can vary. Animatable.
- [greenRange](caemittercell/greenrange.md) — The amount by which the green color component of the cell can vary. Animatable.
- [blueRange](caemittercell/bluerange.md) — The amount by which the blue color component of the cell can vary. Animatable.
- [alphaRange](caemittercell/alpharange.md) — The amount by which the alpha component of the cell can vary. Animatable.
- [redSpeed](caemittercell/redspeed.md) — The speed, in seconds, at which the red color component changes over the lifetime of the cell. Animatable.
- [greenSpeed](caemittercell/greenspeed.md) — The speed, in seconds, at which the green color component changes over the lifetime of the cell. Animatable.
- [blueSpeed](caemittercell/bluespeed.md) — The speed, in seconds, at which the blue color component changes over the lifetime of the cell. Animatable.
- [alphaSpeed](caemittercell/alphaspeed.md) — The speed, in seconds, at which the alpha component changes over the lifetime of the cell. Animatable.
- [magnificationFilter](caemittercell/magnificationfilter.md) — The filter used when increasing the size of the content.
- [minificationFilter](caemittercell/minificationfilter.md) — The filter used when reducing the size of the content.
- [minificationFilterBias](caemittercell/minificationfilterbias.md) — The bias factor used by the minification filter to determine the levels of detail.
- [scale](caemittercell/scale.md) — Specifies the scale factor applied to the cell. Animatable.
- [scaleRange](caemittercell/scalerange.md) — Specifies the range over which the scale value can vary. Animatable.
- [contentsScale](caemittercell/contentsscale.md) — The scale factor of the cell contents.
- [name](caemittercell/name.md) — The name of the cell.
- [style](caemittercell/style.md) — An optional dictionary containing additional style values that are not explicitly defined by the receiver.

### Setting Emitter Cell Motion Attributes

- [spin](caemittercell/spin.md) — The rotational velocity, measured in radians per second, to apply to the cell. Animatable.
- [spinRange](caemittercell/spinrange.md) — The amount by which the spin of the cell can vary over its lifetime. Animatable.
- [emissionLatitude](caemittercell/emissionlatitude.md) — The latitudinal orientation of the emission angle. Animatable.
- [emissionLongitude](caemittercell/emissionlongitude.md) — The longitudinal orientation of the emission angle. Animatable.
- [emissionRange](caemittercell/emissionrange.md) — The angle, in radians, defining a cone around the emission angle. Animatable.

### Setting Emitter Cell Temporal Attributes

- [lifetime](caemittercell/lifetime.md) — The lifetime of the cell, in seconds. Animatable.
- [lifetimeRange](caemittercell/lifetimerange.md) — The mean value by which the [lifetime](caemittercell/lifetime.md) of the cell can vary. Animatable.
- [birthRate](caemittercell/birthrate.md) — The number of emitted objects created every second. Animatable.
- [scaleSpeed](caemittercell/scalespeed.md) — The speed at which the scale changes over the lifetime of the cell. Animatable.
- [velocity](caemittercell/velocity.md) — The initial velocity of the cell. Animatable.
- [velocityRange](caemittercell/velocityrange.md) — The amount by which the velocity of the cell can vary. Animatable.
- [xAcceleration](caemittercell/xacceleration.md) — The x component of an acceleration vector applied to cell.
- [yAcceleration](caemittercell/yacceleration.md) — The y component of an acceleration vector applied to cell.
- [zAcceleration](caemittercell/zacceleration.md) — The z component of an acceleration vector applied to cell.

### Using Key-Value Coding Extensions

- [+ defaultValueForKey:](<caemittercell/defaultvalue(forkey_).md>) — Returns the default value of the property with the specified key.
- [- shouldArchiveValueForKey:](<caemittercell/shouldarchivevalue(forkey_).md>) — Returns a Boolean value indicating whether the value for a given key should be archived.

### Initializers

- [init(coder:)](<caemittercell/init(coder_).md>)

## See Also

### Particle Systems

- [CAEmitterLayer](caemitterlayer.md) — A layer that emits, animates, and renders a particle system.
