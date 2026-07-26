---
title: flushUpdates
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewpropertyanimator/flushupdates
source_url: 'https://developer.apple.com/documentation/uikit/uiviewpropertyanimator/flushupdates'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewpropertyanimator/flushupdates.json'
content_hash: 'sha256:b0e87dbe6d1f8fc8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewPropertyAnimator](../uiviewpropertyanimator.md)

# flushUpdates

<sub>Instance Property</sub>

Flush all pending updates (including traits, properties, and layout) whenever the animation context changes. This includes flushing updates:

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var flushUpdates: Bool { get set }
```

## Discussion

- Before entering an animation scope, for invalidations that happened previously without animation.
- Before entering a nested animation scope, for invalidations that happened in the outer animation scope.
- Before exiting any animation scope, for invalidations that happened in that animation scope.
- Before disabling animations, for invalidations that happened in the animation scope with animations enabled.
- Before re-enabling animations, for invalidations that happened in the scope with animations disabled. This behavior implicitly applies to any nested animation scopes, even if they don’t explicitly specify this.
