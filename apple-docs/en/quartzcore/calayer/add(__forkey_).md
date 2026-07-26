---
title: 'add(_:forKey:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/add(_:forkey:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/add(_:forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/add%28_%3Aforkey%3A%29.json'
content_hash: 'sha256:93f46f4ad068f8e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# add(_:forKey:)

<sub>Instance Method</sub>

Add the specified animation object to the layer’s render tree.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func add(_ anim: CAAnimation, forKey key: String?)
```

## Parameters

- `anim` — The animation to be added to the render tree. This object is copied by the render tree, not referenced. Therefore, subsequent modifications to the object are not propagated into the render tree.

- `key` — A string that identifies the animation. Only one animation per unique key is added to the layer. The special key [kCATransition](../kcatransition.md) is automatically used for transition animations. You may specify `nil` for this parameter.

## Discussion

If the `duration` property of the animation is zero or negative, the duration is changed to the current value of the [kCATransactionAnimationDuration](../kcatransactionanimationduration.md) transaction property (if set) or to the default value of `0.25` seconds.

## See Also

### Layer animations

- [- animationForKey:](<animation(forkey_).md>) — Returns the animation object with the specified identifier.
- [- removeAllAnimations](<removeallanimations().md>) — Remove all animations attached to the layer.
- [- removeAnimationForKey:](<removeanimation(forkey_).md>) — Remove the animation object with the specified key.
- [- animationKeys](<animationkeys().md>) — Returns an array of strings that identify the animations currently attached to the layer.
