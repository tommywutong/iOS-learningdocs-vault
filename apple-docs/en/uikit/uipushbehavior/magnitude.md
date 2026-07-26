---
title: magnitude
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipushbehavior/magnitude
source_url: 'https://developer.apple.com/documentation/uikit/uipushbehavior/magnitude'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipushbehavior/magnitude.json'
content_hash: 'sha256:32fcfb273579e838'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPushBehavior](../uipushbehavior.md)

# magnitude

<sub>Instance Property</sub>

The magnitude of the force vector for the push behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var magnitude: CGFloat { get set }
```

## Discussion

The default magnitude is `0.0`, equivalent to no force. A continuous force vector with a magnitude of `1.0`, applied to a 100 point x 100 point view whose density value is `1.0`, results in view acceleration of 100 points / second² in the direction indicated by the [angle](angle.md) or [pushDirection](pushdirection.md) property.

Setting the [magnitude](magnitude.md) parameter to a negative value reverses the direction of the force.

## See Also

### Configuring a push behavior

- [- setAngle:magnitude:](<setangle(__magnitude_).md>) — Sets the angle and magnitude of the force vector for the behavior.
- [angle](angle.md) — The angle, in radians, of the force vector for the behavior.
- [mode](mode-swift.property.md) — Returns the force mode for the push behavior.
- [- setTargetOffsetFromCenter:forItem:](<settargetoffsetfromcenter(__for_).md>) — Sets the offset, from the center of a dynamic item, at which to apply the push behavior’s force vector.
- [- targetOffsetFromCenterForItem:](<targetoffsetfromcenter(for_).md>) — Returns the offset, from the center of a dynamic item, at which the push behavior’s force vector is applied.
- [pushDirection](pushdirection.md) — The direction of the force vector for the behavior, expressed as _x_ and _y_ components and using standard UIKit geometry.
