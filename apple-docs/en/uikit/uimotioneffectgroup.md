---
title: UIMotionEffectGroup
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimotioneffectgroup
source_url: 'https://developer.apple.com/documentation/uikit/uimotioneffectgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimotioneffectgroup.json'
content_hash: 'sha256:c84d1166f32d754f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIMotionEffectGroup

<sub>Class</sub>

A collection of motion effects that you want to apply to a view at the same time.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIMotionEffectGroup
```

## Overview

This class behaves similarly to the [CAAnimationGroup](../quartzcore/caanimationgroup.md) class in Core Animation. The key paths and values returned by each motion effect object are applied simultaneously and with the same timing. Because [UIMotionEffectGroup](uimotioneffectgroup.md) is a subclass of [UIMotionEffect](uimotioneffect.md), you can treat it like a single motion effect in your code. After setting a value for the [motionEffects](uimotioneffectgroup/motioneffects.md) property, add the group object to one or more of your views.

## Relationships

- **Inherits From**: [UIMotionEffect](uimotioneffect.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Setting the group items

- [motionEffects](uimotioneffectgroup/motioneffects.md) — An array of motion effect objects to apply as a group to the view.

## See Also

### View-based effects

- [UIInterpolatingMotionEffect](uiinterpolatingmotioneffect.md) — An object that maps the horizontal or vertical tilt of a device to values that you specify so that UIKit can apply those values to your views.
