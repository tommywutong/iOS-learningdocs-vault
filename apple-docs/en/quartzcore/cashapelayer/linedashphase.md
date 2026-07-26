---
title: lineDashPhase
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cashapelayer/linedashphase
source_url: 'https://developer.apple.com/documentation/quartzcore/cashapelayer/linedashphase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cashapelayer/linedashphase.json'
content_hash: 'sha256:f1d87674bb81dd72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAShapeLayer](../cashapelayer.md)

# lineDashPhase

<sub>Instance Property</sub>

The dash phase applied to the shape’s path when stroked. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var lineDashPhase: CGFloat { get set }
```

## Discussion

Line dash phase specifies how far into the dash pattern the line starts.

Default is `0`.

The following code shows how you can create a “marching ant” effect by adding an animation to a shape layer that animates its [lineDashPhase](linedashphase.md) from `0` to the sum of the segment lengths of its [lineDashPattern](linedashpattern.md).

```swift
let shapeLayer = CAShapeLayer()
shapeLayer.strokeColor = UIColor.black.cgColor
shapeLayer.fillColor = UIColor.clear.cgColor
shapeLayer.lineWidth = 5
shapeLayer.lineDashPattern = [10,5,5,5]
     
let path = CGMutablePath()
path.addLines(between: [CGPoint(x: 0, y: 100),
                        CGPoint(x: 640, y: 100)])
shapeLayer.path = path
     
let lineDashAnimation = CABasicAnimation(keyPath: "lineDashPhase")
lineDashAnimation.fromValue = 0
lineDashAnimation.toValue = shapeLayer.lineDashPattern?.reduce(0) { $0 + $1.intValue }
lineDashAnimation.duration = 1
lineDashAnimation.repeatCount = Float.greatestFiniteMagnitude
     
shapeLayer.add(lineDashAnimation, forKey: nil)
```

## See Also

### Accessing Shape Style Properties

- [fillColor](fillcolor.md) — The color used to fill the shape’s path. Animatable.
- [fillRule](fillrule.md) — The fill rule used when filling the shape’s path.
- [lineCap](linecap.md) — Specifies the line cap style for the shape’s path.
- [lineDashPattern](linedashpattern.md) — The dash pattern applied to the shape’s path when stroked.
- [lineJoin](linejoin.md) — Specifies the line join style for the shape’s path.
- [lineWidth](linewidth.md) — Specifies the line width of the shape’s path. Animatable.
- [miterLimit](miterlimit.md) — The miter limit used when stroking the shape’s path. Animatable.
- [strokeColor](strokecolor.md) — The color used to stroke the shape’s path. Animatable.
- [strokeStart](strokestart.md) — The relative location at which to begin stroking the path. Animatable.
- [strokeEnd](strokeend.md) — The relative location at which to stop stroking the path. Animatable.
