---
title: 'setAngle(_:magnitude:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipushbehavior/setangle(_:magnitude:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipushbehavior/setangle(_:magnitude:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipushbehavior/setangle%28_%3Amagnitude%3A%29.json'
content_hash: 'sha256:f03b6648b2298107'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPushBehavior](../uipushbehavior.md)

# setAngle(_:magnitude:)

<sub>Instance Method</sub>

Sets the angle and magnitude of the force vector for the behavior.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setAngle(_ angle: CGFloat, magnitude: CGFloat)
```

## Parameters

- `angle` — The angle, in radians, of the force vector for the push behavior. The default angle is `0` radians, using standard UIKit geometry.

- `magnitude` — The magnitude of the force vector for the push behavior. The default magnitude is `nil`, equivalent to no force. A force vector with a magnitude of `1.0`, applied to a 100 point x 100 point view whose density value is `1.0`, results in view acceleration of 100 points / second². Setting the [magnitude](magnitude.md) parameter to a negative value reverses the direction of the force.

## Discussion

Whether you express a push behavior’s force direction in terms of radian angle or with _x_, _y_ components, the alternate, equivalent values update automatically.

## See Also

### Configuring a push behavior

- [angle](angle.md) — The angle, in radians, of the force vector for the behavior.
- [magnitude](magnitude.md) — The magnitude of the force vector for the push behavior.
- [mode](mode-swift.property.md) — Returns the force mode for the push behavior.
- [- setTargetOffsetFromCenter:forItem:](<settargetoffsetfromcenter(__for_).md>) — Sets the offset, from the center of a dynamic item, at which to apply the push behavior’s force vector.
- [- targetOffsetFromCenterForItem:](<targetoffsetfromcenter(for_).md>) — Returns the offset, from the center of a dynamic item, at which the push behavior’s force vector is applied.
- [pushDirection](pushdirection.md) — The direction of the force vector for the behavior, expressed as _x_ and _y_ components and using standard UIKit geometry.
