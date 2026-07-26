---
title: UIInterpolatingMotionEffect
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiinterpolatingmotioneffect
source_url: 'https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinterpolatingmotioneffect.json'
content_hash: 'sha256:78e2ec68c73312ef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIInterpolatingMotionEffect

<sub>Class</sub>

An object that maps the horizontal or vertical tilt of a device to values that you specify so that UIKit can apply those values to your views.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIInterpolatingMotionEffect
```

## Overview

You use this class to determine the amount of tilt along a single axis to apply to a view. After creating an instance of this class, you must assign appropriate values to the [minimumRelativeValue](uiinterpolatingmotioneffect/minimumrelativevalue.md) and [maximumRelativeValue](uiinterpolatingmotioneffect/maximumrelativevalue.md) properties. As the user moves the device, the motion effect object translates the fixed offset values returned by the system (which are in the range `-1` to `1`) to the range of values you specified. UIKit then applies the translated values to any target views.

## Relationships

- **Inherits From**: [UIMotionEffect](uimotioneffect.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing a motion effect

- [- initWithKeyPath:type:](<uiinterpolatingmotioneffect/init(keypath_type_).md>) — Initializes and returns an interpolating motion effect object configured for the specific tilt direction.
- [- initWithCoder:](<uiinterpolatingmotioneffect/init(coder_).md>) — Creates a motion effect from data in an unarchiver.

### Accessing the motion attributes

- [keyPath](uiinterpolatingmotioneffect/keypath.md) — The key path you want to modify on the view.
- [type](uiinterpolatingmotioneffect/type.md) — The tilt direction to monitor.
- [minimumRelativeValue](uiinterpolatingmotioneffect/minimumrelativevalue.md) — The value that maps to the minimum viewer offset.
- [maximumRelativeValue](uiinterpolatingmotioneffect/maximumrelativevalue.md) — The value that maps to the maximum viewer offset.

### Constants

- [EffectType](uiinterpolatingmotioneffect/effecttype.md) — The axis to use when interpolating values.

## See Also

### View-based effects

- [UIMotionEffectGroup](uimotioneffectgroup.md) — A collection of motion effects that you want to apply to a view at the same time.
