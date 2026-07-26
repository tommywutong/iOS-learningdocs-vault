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
doc_path: /documentation/uikit/uigravitybehavior/magnitude
source_url: 'https://developer.apple.com/documentation/uikit/uigravitybehavior/magnitude'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigravitybehavior/magnitude.json'
content_hash: 'sha256:7407ea01756a8308'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGravityBehavior](../uigravitybehavior.md)

# magnitude

<sub>Instance Property</sub>

The magnitude of the gravity vector.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var magnitude: CGFloat { get set }
```

## Discussion

Modify this property when you want to change the magnitude of the gravity vector separately from the angle of that vector. A magnitude value of `1.0` represents an acceleration of 1000 points / second² at the specified angle, which roughly approximates the force of Earth’s gravity. The value in this property is tied to the value in the [gravityDirection](gravitydirection.md) property, so changes in one affect the other.

The default value of this property is `1.0`.

> [!important] Important
> Setting the value of this property to `0.0` creates the vector (`0.0`, `0.0`) and resets the [angle](angle.md) property to `0.0` radians. If you make subsequent changes to this property, also remember to update the [angle](angle.md) property.

## See Also

### Configuring a gravity behavior

- [gravityDirection](gravitydirection.md) — The direction and magnitude of the gravitational force, expressed as a vector.
- [angle](angle.md) — The direction of the gravity vector, expressed in radians in the reference coordinate system.
- [- setAngle:magnitude:](<setangle(__magnitude_).md>) — Sets the angle and magnitude of the gravity vector for the behavior.
