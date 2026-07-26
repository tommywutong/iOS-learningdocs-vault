---
title: 'initialFrame(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontrollercontexttransitioning/initialframe(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/initialframe(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollercontexttransitioning/initialframe%28for%3A%29.json'
content_hash: 'sha256:661b77510e2a7941'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerContextTransitioning](../uiviewcontrollercontexttransitioning.md)

# initialFrame(for:)

<sub>Instance Method</sub>

Returns the starting frame rectangle for the specified view controller’s view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func initialFrame(for vc: UIViewController) -> CGRect
```

## Parameters

- `vc` — The view controller whose frame rectangle you want.

## Return Value

The frame rectangle for the view or [CGRectZero](../../coregraphics/cgrectzero.md) if the frame rectangle is not known or the view is not visible.

## Discussion

The rectangle returned by this method represents the size of the corresponding view at the beginning of the transition. For the view controller that is already onscreen, this rectangle typically matches the frame rectangle of the container view. For the view controller being presented, the value returned by this method is typically [CGRectZero](../../coregraphics/cgrectzero.md) because the view is not yet on screen.

## See Also

### Getting the transition frame rectangles

- [- finalFrameForViewController:](<finalframe(for_).md>) — Returns the ending frame rectangle for the specified view controller’s view.
