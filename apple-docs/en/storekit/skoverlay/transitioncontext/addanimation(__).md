---
title: 'addAnimation(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/storekit/skoverlay/transitioncontext/addanimation(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/skoverlay/transitioncontext/addanimation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skoverlay/transitioncontext/addanimation%28_%3A%29.json'
content_hash: 'sha256:e76e14b98f4381c3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SKOverlay](../../skoverlay.md) · [TransitionContext](../transitioncontext.md)

# addAnimation(_:)

<sub>Instance Method</sub>

Adds a closure you can use to animate view properties.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func addAnimation(_ block: @escaping () -> Void)
```

## Parameters

- `block` — A closure that sets animatable view properties and runs on the main thread.

## See Also

### Adding an Animation

- [startFrame](startframe.md) — The size and location of the overlay before the transition.
- [endFrame](endframe.md) — The size and location of the overlay at the end of the transition.
