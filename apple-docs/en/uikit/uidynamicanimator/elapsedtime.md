---
title: elapsedTime
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidynamicanimator/elapsedtime
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicanimator/elapsedtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicanimator/elapsedtime.json'
content_hash: 'sha256:51663ac6dc937f5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicAnimator](../uidynamicanimator.md)

# elapsedTime

<sub>Instance Property</sub>

Returns the time interval since the dynamic animator started running.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var elapsedTime: TimeInterval { get }
```

## Return Value

The elapsed time since the dynamic animator started running.

## See Also

### Accessing a dynamic animator’s state

- [running](isrunning.md) — Returns true if the dynamic animator is running.
- [behaviors](behaviors.md) — The dynamic behaviors managed by a dynamic animator.
- [referenceView](referenceview.md) — The view that a dynamic animator was initialized with.
- [- updateItemUsingCurrentState:](<updateitem(usingcurrentstate_).md>) — Asks a dynamic animator to read the current state of a dynamic item, replacing the animator’s internal representation of the item’s state.
