---
title: angle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipushbehavior/angle
source_url: 'https://developer.apple.com/documentation/uikit/uipushbehavior/angle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipushbehavior/angle.json'
content_hash: 'sha256:771a2869a292fdba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPushBehavior](../uipushbehavior.md)

# angle

<sub>Instance Property</sub>

The angle, in radians, of the force vector for the behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var angle: CGFloat { get set }
```

## Discussion

The default angle is `0` radians, using standard UIKit geometry. To configure the force vector for a push behavior, set the [magnitude](magnitude.md) property as well as the [angle](angle.md) property.

Alternatively, you can express the direction of force by using _x_ and _y_ components with the [pushDirection](pushdirection.md) property. Whichever approach you use, the alternate, equivalent values update automatically.

## See Also

### Configuring a push behavior

- [- setAngle:magnitude:](<setangle(__magnitude_).md>) — Sets the angle and magnitude of the force vector for the behavior.
- [magnitude](magnitude.md) — The magnitude of the force vector for the push behavior.
- [mode](mode-swift.property.md) — Returns the force mode for the push behavior.
- [- setTargetOffsetFromCenter:forItem:](<settargetoffsetfromcenter(__for_).md>) — Sets the offset, from the center of a dynamic item, at which to apply the push behavior’s force vector.
- [- targetOffsetFromCenterForItem:](<targetoffsetfromcenter(for_).md>) — Returns the offset, from the center of a dynamic item, at which the push behavior’s force vector is applied.
- [pushDirection](pushdirection.md) — The direction of the force vector for the behavior, expressed as _x_ and _y_ components and using standard UIKit geometry.
