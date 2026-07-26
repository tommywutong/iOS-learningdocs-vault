---
title: 'convert(_:from:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/convert(_:from:)-4kx9l'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/convert(_:from:)-4kx9l'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/convert%28_%3Afrom%3A%29-4kx9l.json'
content_hash: 'sha256:62fb336aa2e3962f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# convert(_:from:)

<sub>Instance Method</sub>

Converts the rectangle from the specified layer’s coordinate system to the receiver’s coordinate system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func convert(_ r: CGRect, from l: CALayer?) -> CGRect
```

## Parameters

- `r` — A point specifying a location in the coordinate system of `l`.

- `l` — The layer with `r` in its coordinate system. The receiver and `l` and must share a common parent layer. This parameter may be `nil`.

## Return Value

The rectangle converted to the receiver’s coordinate system.

## Discussion

If you specify `nil` for the `l` parameter, this method returns the original rect with an origin subtracted from the layer’s frame’s origin.

The following example shows code that creates two layers, `redLayer` and `yellowLayer`. `yellowLayer` is scaled so that it is half of its original size.

```swift
let layerFrame = CGRect(x: 0, y: 0, width: 640, height: 480)
     
let redLayer = CALayer()
redLayer.frame = layerFrame
redLayer.backgroundColor = UIColor.red.cgColor
     
let yellowLayer = CALayer()
yellowLayer.frame = layerFrame
yellowLayer.backgroundColor = UIColor.yellow.cgColor
yellowLayer.transform = CATransform3DMakeScale(0.5, 0.5, 1)
```

The following figure shows the two layers and an overlaid rectangle with a frame of `(50, 50, 200, 200)` in the red layer’s coordinate system.

![Layers with different coordinate systems](../../../../attachments/04558faab052c26b463625dbc8c7cc46/media-2850326@2x.png)

The following code shows how you can find the coordinates of that rectangle in the yellow layer’s coordinate system.

```swift
let rect = CGRect(x: 50, y: 50, width: 200, height: 200)
print(yellowLayer.convert(rect, from: redLayer)) // prints (-220.0, -140.0, 400.0, 400.0)
```

## See Also

### Mapping between coordinate and time spaces

- [- convertPoint:fromLayer:](<convert(__from_)-8kl76.md>) — Converts the point from the specified layer’s coordinate system to the receiver’s coordinate system.
- [- convertPoint:toLayer:](<convert(__to_)-7dcke.md>) — Converts the point from the receiver’s coordinate system to the specified layer’s coordinate system.
- [- convertRect:toLayer:](<convert(__to_)-tly5.md>) — Converts the rectangle from the receiver’s coordinate system to the specified layer’s coordinate system.
- [- convertTime:fromLayer:](<converttime(__from_).md>) — Converts the time interval from the specified layer’s time space to the receiver’s time space.
- [- convertTime:toLayer:](<converttime(__to_).md>) — Converts the time interval from the receiver’s time space to the specified layer’s time space
