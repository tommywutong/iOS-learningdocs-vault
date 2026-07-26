---
title: pushDirection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipushbehavior/pushdirection
source_url: 'https://developer.apple.com/documentation/uikit/uipushbehavior/pushdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipushbehavior/pushdirection.json'
content_hash: 'sha256:f8cb3ebbad32a8ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPushBehavior](../uipushbehavior.md)

# pushDirection

<sub>Instance Property</sub>

The direction of the force vector for the behavior, expressed as _x_ and _y_ components and using standard UIKit geometry.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var pushDirection: CGVector { get set }
```

## Discussion

The default `x` and `y` values of the push direction vector are each `0.0`. A value for either component of `1.0`, applied to a 100 point x 100 point view, whose density value is `1.0`, results in view acceleration of 100 points / second² in the positive direction for the component.

Setting either direction component to a negative value reverses the direction of force for the component.

Whether you express a push behavior’s push direction in terms of _x_, _y_ components or with an angle (by using the [angle](angle.md) property), the alternate, equivalent value updates automatically.

## See Also

### Configuring a push behavior

- [- setAngle:magnitude:](<setangle(__magnitude_).md>) — Sets the angle and magnitude of the force vector for the behavior.
- [angle](angle.md) — The angle, in radians, of the force vector for the behavior.
- [magnitude](magnitude.md) — The magnitude of the force vector for the push behavior.
- [mode](mode-swift.property.md) — Returns the force mode for the push behavior.
- [- setTargetOffsetFromCenter:forItem:](<settargetoffsetfromcenter(__for_).md>) — Sets the offset, from the center of a dynamic item, at which to apply the push behavior’s force vector.
- [- targetOffsetFromCenterForItem:](<targetoffsetfromcenter(for_).md>) — Returns the offset, from the center of a dynamic item, at which the push behavior’s force vector is applied.
