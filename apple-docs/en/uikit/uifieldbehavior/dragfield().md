---
title: dragField()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifieldbehavior/dragfield()
source_url: 'https://developer.apple.com/documentation/uikit/uifieldbehavior/dragfield()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifieldbehavior/dragfield%28%29.json'
content_hash: 'sha256:00e4c2538a03f199'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFieldBehavior](../uifieldbehavior.md)

# dragField()

<sub>Type Method</sub>

Creates and returns a field behavior for slowing an object’s velocity.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func dragField() -> Self
```

## Return Value

A field behavior object that applies a drag force to items.

## Discussion

This field simulates the force of friction on an item. The force is applied in the opposite direction of the affected item’s velocity vector and has a magnitude that is proportional to the field’s [strength](strength.md) property and the item’s current velocity.

## See Also

### Getting the field behaviors

- [+ springField](<springfield().md>) — Creates and returns a spring field behavior.
- [+ velocityFieldWithVector:](<velocityfield(direction_).md>) — Creates and returns a field behavior object that applies a directional velocity to items.
- [+ electricField](<electricfield().md>) — Creates and returns a field behavior object that interacts with charged items.
- [+ magneticField](<magneticfield().md>) — Creates and returns a field behavior that interacts with charged items.
- [+ radialGravityFieldWithPosition:](<radialgravityfield(position_).md>) — Creates and returns a field behavior object that models a radial gravitational force.
- [+ linearGravityFieldWithVector:](<lineargravityfield(direction_).md>) — Creates and returns a field behavior object that models a linear gravitational force.
- [+ vortexField](<vortexfield().md>) — Creates and returns a field behavior object that applies a rotational force relative to the field’s position.
- [+ noiseFieldWithSmoothness:animationSpeed:](<noisefield(smoothness_animationspeed_).md>) — Creates and returns a field behavior object that applies random noise to other forces.
- [+ turbulenceFieldWithSmoothness:animationSpeed:](<turbulencefield(smoothness_animationspeed_).md>) — Creates and returns a field behavior object that applies noise to an item in motion.
- [+ fieldWithEvaluationBlock:](<field(evaluationblock_).md>) — Creates and returns a field behavior object that applies an app-specified field to items.
