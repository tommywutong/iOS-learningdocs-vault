---
title: 'updateItem(usingCurrentState:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidynamicanimator/updateitem(usingcurrentstate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicanimator/updateitem(usingcurrentstate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicanimator/updateitem%28usingcurrentstate%3A%29.json'
content_hash: 'sha256:86ef9717bef6e32a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicAnimator](../uidynamicanimator.md)

# updateItem(usingCurrentState:)

<sub>Instance Method</sub>

Asks a dynamic animator to read the current state of a dynamic item, replacing the animator’s internal representation of the item’s state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func updateItem(usingCurrentState item: any UIDynamicItem)
```

## Parameters

- `item` — The dynamic item whose state was changed by your app.

## Discussion

A dynamic animator automatically reads the initial state (position and rotation) of each dynamic item you add to it, and then takes responsibility for updating the item’s state. If you actively change the state of a dynamic item _after_ you’ve added it to a dynamic animator, call this method to ask the animator to read and incorporate the new state.

## See Also

### Accessing a dynamic animator’s state

- [elapsedTime](elapsedtime.md) — Returns the time interval since the dynamic animator started running.
- [running](isrunning.md) — Returns true if the dynamic animator is running.
- [behaviors](behaviors.md) — The dynamic behaviors managed by a dynamic animator.
- [referenceView](referenceview.md) — The view that a dynamic animator was initialized with.
