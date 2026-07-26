---
title: 'textViewportLayoutControllerDidLayout(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerdidlayout(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerdidlayout(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerdidlayout%28_%3A%29.json'
content_hash: 'sha256:9d66e35a27fc1f6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextViewportLayoutControllerDelegate](../nstextviewportlayoutcontrollerdelegate.md)

# textViewportLayoutControllerDidLayout(_:)

<sub>Instance Method</sub>

The method the framework calls when the text viewport layout controller finishes its layout process.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textViewportLayoutControllerDidLayout(_ textViewportLayoutController: NSTextViewportLayoutController)
```

## Parameters

- `textViewportLayoutController` — The [NSTextViewportLayoutController](../nstextviewportlayoutcontroller.md).

## Discussion

Layout information on `textViewportLayoutController` is up-to-date at the point of this call.

## See Also

### Responding to changes in the viewport

- [- textViewportLayoutController:configureRenderingSurfaceForTextLayoutFragment:](<textviewportlayoutcontroller(__configurerenderingsurfacefor_).md>) — The method the framework calls when the layout controller lays out a text layout fragment in the UI.
- [- textViewportLayoutControllerWillLayout:](<textviewportlayoutcontrollerwilllayout(__).md>) — The method the framework calls before the text viewport layout controller starts its layout process.
- [- textViewportLayoutControllerReceivedSetNeedsLayout:](<textviewportlayoutcontrollerreceivedsetneedslayout(__).md>) — Triggers relayout of the view.
- [- viewportBoundsForTextViewportLayoutController:](<viewportbounds(for_).md>) — Returns the current viewport, which is the view visible bounds plus the overdraw area.
