---
title: behaviors
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidynamicanimator/behaviors
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicanimator/behaviors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicanimator/behaviors.json'
content_hash: 'sha256:7a9ca0b55ca32a8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicAnimator](../uidynamicanimator.md)

# behaviors

<sub>Instance Property</sub>

The dynamic behaviors managed by a dynamic animator.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var behaviors: [UIDynamicBehavior] { get }
```

## See Also

### Accessing a dynamic animator’s state

- [elapsedTime](elapsedtime.md) — Returns the time interval since the dynamic animator started running.
- [running](isrunning.md) — Returns true if the dynamic animator is running.
- [referenceView](referenceview.md) — The view that a dynamic animator was initialized with.
- [- updateItemUsingCurrentState:](<updateitem(usingcurrentstate_).md>) — Asks a dynamic animator to read the current state of a dynamic item, replacing the animator’s internal representation of the item’s state.
