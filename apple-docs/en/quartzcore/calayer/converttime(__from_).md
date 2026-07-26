---
title: 'convertTime(_:from:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/converttime(_:from:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/converttime(_:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/converttime%28_%3Afrom%3A%29.json'
content_hash: 'sha256:ca9aad6a91d0a651'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# convertTime(_:from:)

<sub>Instance Method</sub>

Converts the time interval from the specified layer’s time space to the receiver’s time space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func convertTime(_ t: CFTimeInterval, from l: CALayer?) -> CFTimeInterval
```

## Parameters

- `t` — A point specifying a location in the coordinate system of `l`.

- `l` — The layer with `t` in its time space. The receiver and `l` and must share a common parent layer.

## Return Value

The time interval converted to the receiver’s time space.

## Discussion

The following code shows the creation of two layers, layer and `offsetSlowMoLayer`. `offsetSlowMoLayer` has an offset time of 1 second and its [speed](../camediatiming/speed.md) is set to `0.5`.  The last line converts and prints a time interval of 0.5 seconds converted from the time space of `layer` to the time space of `offsetSlowMoLayer`.

```swift
let layer = CALayer()
let offsetSlowMoLayer = CALayer()
       
offsetSlowMoLayer.timeOffset = CFTimeInterval(1)
offsetSlowMoLayer.speed = 0.5
       
print(offsetSlowMoLayer.convertTime(CFTimeInterval(0.5), from: layer)) // prints 1.25
```

## See Also

### Mapping between coordinate and time spaces

- [- convertPoint:fromLayer:](<convert(__from_)-8kl76.md>) — Converts the point from the specified layer’s coordinate system to the receiver’s coordinate system.
- [- convertPoint:toLayer:](<convert(__to_)-7dcke.md>) — Converts the point from the receiver’s coordinate system to the specified layer’s coordinate system.
- [- convertRect:fromLayer:](<convert(__from_)-4kx9l.md>) — Converts the rectangle from the specified layer’s coordinate system to the receiver’s coordinate system.
- [- convertRect:toLayer:](<convert(__to_)-tly5.md>) — Converts the rectangle from the receiver’s coordinate system to the specified layer’s coordinate system.
- [- convertTime:toLayer:](<converttime(__to_).md>) — Converts the time interval from the receiver’s time space to the specified layer’s time space
