---
title: referenceView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidynamicanimator/referenceview
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicanimator/referenceview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicanimator/referenceview.json'
content_hash: 'sha256:e5af29937189fc9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicAnimator](../uidynamicanimator.md)

# referenceView

<sub>Instance Property</sub>

The view that a dynamic animator was initialized with.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var referenceView: UIView? { get }
```

## Discussion

This property has a value only for a dynamic animator initialized using the [- initWithReferenceView:](<init(referenceview_).md>) method.

## See Also

### Accessing a dynamic animator’s state

- [elapsedTime](elapsedtime.md) — Returns the time interval since the dynamic animator started running.
- [running](isrunning.md) — Returns true if the dynamic animator is running.
- [behaviors](behaviors.md) — The dynamic behaviors managed by a dynamic animator.
- [- updateItemUsingCurrentState:](<updateitem(usingcurrentstate_).md>) — Asks a dynamic animator to read the current state of a dynamic item, replacing the animator’s internal representation of the item’s state.
