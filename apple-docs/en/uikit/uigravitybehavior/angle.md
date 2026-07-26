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
doc_path: /documentation/uikit/uigravitybehavior/angle
source_url: 'https://developer.apple.com/documentation/uikit/uigravitybehavior/angle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigravitybehavior/angle.json'
content_hash: 'sha256:ff8ba78336979364'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGravityBehavior](../uigravitybehavior.md)

# angle

<sub>Instance Property</sub>

The direction of the gravity vector, expressed in radians in the reference coordinate system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var angle: CGFloat { get set }
```

## Discussion

Modify this property when you want to change the angle of the gravity vector separately from the magnitude of that vector. The value in this property is tied to the value in the [gravityDirection](gravitydirection.md) property, so changes in one affect the other.

The default angle is `pi / 2` radians, which represents a downward force in the reference view. A value of `0` represents a force that moves items toward the right side of the reference view.

## See Also

### Configuring a gravity behavior

- [gravityDirection](gravitydirection.md) — The direction and magnitude of the gravitational force, expressed as a vector.
- [magnitude](magnitude.md) — The magnitude of the gravity vector.
- [- setAngle:magnitude:](<setangle(__magnitude_).md>) — Sets the angle and magnitude of the gravity vector for the behavior.
