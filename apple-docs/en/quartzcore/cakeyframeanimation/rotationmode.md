---
title: rotationMode
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cakeyframeanimation/rotationmode
source_url: 'https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/rotationmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cakeyframeanimation/rotationmode.json'
content_hash: 'sha256:fe682605a6f7a0ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAKeyframeAnimation](../cakeyframeanimation.md)

# rotationMode

<sub>Instance Property</sub>

Determines whether objects animating along the path rotate to match the path tangent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var rotationMode: CAAnimationRotationMode? { get set }
```

## Discussion

The possible values for this property are described in [Rotation Mode Values](../rotation-mode-values.md). The default value of this property is `nil`, which indicates that objects should not rotate to follow the path.

The effect of setting this property to a non-`nil` value when no path object is supplied is undefined.

## See Also

### Related Documentation

- [path](path.md) — The path for a point-based property to follow.
