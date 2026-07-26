---
title: 'splitViewControllerInteractivePresentationGestureWillBegin(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollerinteractivepresentationgesturewillbegin(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollerinteractivepresentationgesturewillbegin(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollerinteractivepresentationgesturewillbegin%28_%3A%29.json'
content_hash: 'sha256:020ac861b981d04b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewControllerDelegate](../uisplitviewcontrollerdelegate.md)

# splitViewControllerInteractivePresentationGestureWillBegin(_:)

<sub>Instance Method</sub>

Tells the delegate that the interactive presentation gesture is about to begin.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func splitViewControllerInteractivePresentationGestureWillBegin(_ svc: UISplitViewController)
```

## Parameters

- `svc` — The split view controller responding to the interactive presentation gesture.

## Discussion

This delegate method only applies to column-style split view interfaces. For more information, see [Split view styles](../uisplitviewcontroller.md#Split-view-styles).

The split view controller calls this method when the interactive presentation gesture is about to begin. Use this method for performance optimizations related to drawing the column content or other work related to handling the interactive gesture.

## See Also

### Handling the presentation gesture

- [- splitViewControllerInteractivePresentationGestureDidEnd:](<splitviewcontrollerinteractivepresentationgesturedidend(__).md>) — Tells the delegate when the interactive presentation gesture ends.
