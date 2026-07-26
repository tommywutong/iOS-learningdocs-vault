---
title: 'removeAnimation(forKey:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/removeanimation(forkey:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/removeanimation(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/removeanimation%28forkey%3A%29.json'
content_hash: 'sha256:50bf42b2e29c5cd4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# removeAnimation(forKey:)

<sub>Instance Method</sub>

Remove the animation object with the specified key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func removeAnimation(forKey key: String)
```

## Parameters

- `key` — The identifier of the animation to remove.

## See Also

### Layer animations

- [- addAnimation:forKey:](<add(__forkey_).md>) — Add the specified animation object to the layer’s render tree.
- [- animationForKey:](<animation(forkey_).md>) — Returns the animation object with the specified identifier.
- [- removeAllAnimations](<removeallanimations().md>) — Remove all animations attached to the layer.
- [- animationKeys](<animationkeys().md>) — Returns an array of strings that identify the animations currently attached to the layer.
