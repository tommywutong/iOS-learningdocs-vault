---
title: isRunning
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidynamicanimator/isrunning
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicanimator/isrunning'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicanimator/isrunning.json'
content_hash: 'sha256:af531d6594391ca3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicAnimator](../uidynamicanimator.md)

# isRunning

<sub>Instance Property</sub>

Returns true if the dynamic animator is running.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isRunning: Bool { get }
```

## Discussion

The views associated with an animator’s behaviors can change position or change transform only when the animator is running. For optimization purposes, iOS can pause and then restart an animator. Use this method if you need to check whether or not your views are currently subject to changes in position or transform.

## See Also

### Accessing a dynamic animator’s state

- [elapsedTime](elapsedtime.md) — Returns the time interval since the dynamic animator started running.
- [behaviors](behaviors.md) — The dynamic behaviors managed by a dynamic animator.
- [referenceView](referenceview.md) — The view that a dynamic animator was initialized with.
- [- updateItemUsingCurrentState:](<updateitem(usingcurrentstate_).md>) — Asks a dynamic animator to read the current state of a dynamic item, replacing the animator’s internal representation of the item’s state.
