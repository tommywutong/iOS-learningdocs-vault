---
title: gravityDirection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigravitybehavior/gravitydirection
source_url: 'https://developer.apple.com/documentation/uikit/uigravitybehavior/gravitydirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigravitybehavior/gravitydirection.json'
content_hash: 'sha256:fa365121ccfcf04f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGravityBehavior](../uigravitybehavior.md)

# gravityDirection

<sub>Instance Property</sub>

The direction and magnitude of the gravitational force, expressed as a vector.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var gravityDirection: CGVector { get set }
```

## Discussion

The gravity vector is expressed as an _x, y_ pair that represents the relative motion along the x and y axes of the reference view. A value of `1.0` corresponds to an acceleration of 1000 points / second², which is referred to as UIKit gravity and approximates the Earth’s own gravitational force. A value of `-1.0` represents the same amount of force, but in the opposite direction of the corresponding axis.

The default value of this property is the vector (`0.0, 1.0`), which represents a downward force in the reference view. Changing the [angle](angle.md) or [magnitude](magnitude.md) values also changes the value of this property.

## See Also

### Configuring a gravity behavior

- [angle](angle.md) — The direction of the gravity vector, expressed in radians in the reference coordinate system.
- [magnitude](magnitude.md) — The magnitude of the gravity vector.
- [- setAngle:magnitude:](<setangle(__magnitude_).md>) — Sets the angle and magnitude of the gravity vector for the behavior.
