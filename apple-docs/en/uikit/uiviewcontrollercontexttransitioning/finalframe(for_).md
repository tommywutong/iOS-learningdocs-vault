---
title: 'finalFrame(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontrollercontexttransitioning/finalframe(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/finalframe(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollercontexttransitioning/finalframe%28for%3A%29.json'
content_hash: 'sha256:4d72e7bd360076b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerContextTransitioning](../uiviewcontrollercontexttransitioning.md)

# finalFrame(for:)

<sub>Instance Method</sub>

Returns the ending frame rectangle for the specified view controller’s view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func finalFrame(for vc: UIViewController) -> CGRect
```

## Parameters

- `vc` — The view controller whose frame rectangle you want.

## Return Value

The frame rectangle for the view or [CGRectZero](../../coregraphics/cgrectzero.md) if the frame rectangle is not known or the view is not visible.

## Discussion

The rectangle returned by this method represents the size of the corresponding view at the end of the transition. For the view being covered during the presentation, the value returned by this method might be [CGRectZero](../../coregraphics/cgrectzero.md) but it might also be a valid frame rectangle.

## See Also

### Getting the transition frame rectangles

- [- initialFrameForViewController:](<initialframe(for_).md>) — Returns the starting frame rectangle for the specified view controller’s view.
