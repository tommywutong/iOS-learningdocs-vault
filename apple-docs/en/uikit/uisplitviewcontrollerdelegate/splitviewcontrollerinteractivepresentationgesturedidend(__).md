---
title: 'splitViewControllerInteractivePresentationGestureDidEnd(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollerinteractivepresentationgesturedidend(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollerinteractivepresentationgesturedidend(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontrollerdelegate/splitviewcontrollerinteractivepresentationgesturedidend%28_%3A%29.json'
content_hash: 'sha256:c0e3c6422465f67c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewControllerDelegate](../uisplitviewcontrollerdelegate.md)

# splitViewControllerInteractivePresentationGestureDidEnd(_:)

<sub>Instance Method</sub>

Tells the delegate when the interactive presentation gesture ends.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func splitViewControllerInteractivePresentationGestureDidEnd(_ svc: UISplitViewController)
```

## Parameters

- `svc` — The split view controller responding to the interactive presentation gesture.

## Discussion

This delegate method only applies to column-style split view interfaces. For more information, see [Split view styles](../uisplitviewcontroller.md#Split-view-styles).

The split view controller calls this method when the interactive presentation gesture ends. Use this method for performance optimizations related to drawing the column content or other work related to handling the interactive gesture.

## See Also

### Handling the presentation gesture

- [- splitViewControllerInteractivePresentationGestureWillBegin:](<splitviewcontrollerinteractivepresentationgesturewillbegin(__).md>) — Tells the delegate that the interactive presentation gesture is about to begin.
