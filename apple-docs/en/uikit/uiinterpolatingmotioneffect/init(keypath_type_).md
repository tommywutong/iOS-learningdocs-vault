---
title: 'init(keyPath:type:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiinterpolatingmotioneffect/init(keypath:type:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect/init(keypath:type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinterpolatingmotioneffect/init%28keypath%3Atype%3A%29.json'
content_hash: 'sha256:038b44a2ca26ff79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIInterpolatingMotionEffect](../uiinterpolatingmotioneffect.md)

# init(keyPath:type:)

<sub>Initializer</sub>

Initializes and returns an interpolating motion effect object configured for the specific tilt direction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(keyPath: String, type: UIInterpolatingMotionEffect.EffectType)
```

## Parameters

- `keyPath` — The key path of the view that you want to modify. This path must correspond to an animatable property of the view on which this motion effect is applied. For example, to update the [center](../uiview/center.md) property of the view, specify the string “center”.

- `type` — The type of motion to track. You can track horizontal or vertical tilt. For a list of possible values, see [EffectType](effecttype.md).

## Return Value

An initialized interpolating motion effect object.

## See Also

### Initializing a motion effect

- [- initWithCoder:](<init(coder_).md>) — Creates a motion effect from data in an unarchiver.
