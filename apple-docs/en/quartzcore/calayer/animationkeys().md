---
title: animationKeys()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/animationkeys()
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/animationkeys()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/animationkeys%28%29.json'
content_hash: 'sha256:2290a13d64a36a36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# animationKeys()

<sub>Instance Method</sub>

Returns an array of strings that identify the animations currently attached to the layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func animationKeys() -> [String]?
```

## Return Value

An array of [NSString](../../foundation/nsstring.md) objects identifying the current animations.

## Discussion

The order of the array matches the order in which animations will be applied to the layer.

## See Also

### Layer animations

- [- addAnimation:forKey:](<add(__forkey_).md>) — Add the specified animation object to the layer’s render tree.
- [- animationForKey:](<animation(forkey_).md>) — Returns the animation object with the specified identifier.
- [- removeAllAnimations](<removeallanimations().md>) — Remove all animations attached to the layer.
- [- removeAnimationForKey:](<removeanimation(forkey_).md>) — Remove the animation object with the specified key.
