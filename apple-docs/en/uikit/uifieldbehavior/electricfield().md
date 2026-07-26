---
title: electricField()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifieldbehavior/electricfield()
source_url: 'https://developer.apple.com/documentation/uikit/uifieldbehavior/electricfield()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifieldbehavior/electricfield%28%29.json'
content_hash: 'sha256:f98664f30c5db76b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFieldBehavior](../uifieldbehavior.md)

# electricField()

<sub>Type Method</sub>

Creates and returns a field behavior object that interacts with charged items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func electricField() -> Self
```

## Return Value

An field behavior object that applies an electric field to charged items.

## Discussion

The amount of force applied by the field is proportional to the charge of the item and is modeled after the first part of the Lorentz equation (`F = qE`). This equation means that the force equals the charge of the object multiplied by the strength of the electric field at the item’s current location in that field.

You can use electric fields as a way to apply forces to an object that are based on charge instead of mass. You can use electric fields to repel or attract items in your interface, with opposite charges attracting each other and similar charges repelling each other. In other words, an item with a positive charge value is attracted to fields whose [strength](strength.md) value is negative and repelled by fields whose [strength](strength.md) value is positive.

## See Also

### Getting the field behaviors

- [+ dragField](<dragfield().md>) — Creates and returns a field behavior for slowing an object’s velocity.
- [+ springField](<springfield().md>) — Creates and returns a spring field behavior.
- [+ velocityFieldWithVector:](<velocityfield(direction_).md>) — Creates and returns a field behavior object that applies a directional velocity to items.
- [+ magneticField](<magneticfield().md>) — Creates and returns a field behavior that interacts with charged items.
- [+ radialGravityFieldWithPosition:](<radialgravityfield(position_).md>) — Creates and returns a field behavior object that models a radial gravitational force.
- [+ linearGravityFieldWithVector:](<lineargravityfield(direction_).md>) — Creates and returns a field behavior object that models a linear gravitational force.
- [+ vortexField](<vortexfield().md>) — Creates and returns a field behavior object that applies a rotational force relative to the field’s position.
- [+ noiseFieldWithSmoothness:animationSpeed:](<noisefield(smoothness_animationspeed_).md>) — Creates and returns a field behavior object that applies random noise to other forces.
- [+ turbulenceFieldWithSmoothness:animationSpeed:](<turbulencefield(smoothness_animationspeed_).md>) — Creates and returns a field behavior object that applies noise to an item in motion.
- [+ fieldWithEvaluationBlock:](<field(evaluationblock_).md>) — Creates and returns a field behavior object that applies an app-specified field to items.
