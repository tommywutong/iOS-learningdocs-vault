---
title: 'animation(forKey:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/animation(forkey:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/animation(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/animation%28forkey%3A%29.json'
content_hash: 'sha256:97d426f428f56bdb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# animation(forKey:)

<sub>Instance Method</sub>

Returns the animation object with the specified identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func animation(forKey key: String) -> CAAnimation?
```

## Parameters

- `key` — A string that specifies the identifier of the animation. This string corresponds to the identifier string you passed to the [- addAnimation:forKey:](<add(__forkey_).md>) method.

## Return Value

The animation object matching the identifier, or `nil` if no such animation exists.

## Discussion

Use this method to retrieve only animation objects already associated with a layer. Modifying any properties of the returned object results in undefined behavior.

## See Also

### Layer animations

- [- addAnimation:forKey:](<add(__forkey_).md>) — Add the specified animation object to the layer’s render tree.
- [- removeAllAnimations](<removeallanimations().md>) — Remove all animations attached to the layer.
- [- removeAnimationForKey:](<removeanimation(forkey_).md>) — Remove the animation object with the specified key.
- [- animationKeys](<animationkeys().md>) — Returns an array of strings that identify the animations currently attached to the layer.
