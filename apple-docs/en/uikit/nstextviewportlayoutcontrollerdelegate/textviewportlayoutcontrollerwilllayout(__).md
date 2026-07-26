---
title: 'textViewportLayoutControllerWillLayout(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerwilllayout(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerwilllayout(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontrollerwilllayout%28_%3A%29.json'
content_hash: 'sha256:821e944cece4ea0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextViewportLayoutControllerDelegate](../nstextviewportlayoutcontrollerdelegate.md)

# textViewportLayoutControllerWillLayout(_:)

<sub>Instance Method</sub>

The method the framework calls before the text viewport layout controller starts its layout process.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textViewportLayoutControllerWillLayout(_ textViewportLayoutController: NSTextViewportLayoutController)
```

## Parameters

- `textViewportLayoutController` — The [NSTextViewportLayoutController](../nstextviewportlayoutcontroller.md).

## See Also

### Responding to changes in the viewport

- [- textViewportLayoutController:configureRenderingSurfaceForTextLayoutFragment:](<textviewportlayoutcontroller(__configurerenderingsurfacefor_).md>) — The method the framework calls when the layout controller lays out a text layout fragment in the UI.
- [- textViewportLayoutControllerDidLayout:](<textviewportlayoutcontrollerdidlayout(__).md>) — The method the framework calls when the text viewport layout controller finishes its layout process.
- [- textViewportLayoutControllerReceivedSetNeedsLayout:](<textviewportlayoutcontrollerreceivedsetneedslayout(__).md>) — Triggers relayout of the view.
- [- viewportBoundsForTextViewportLayoutController:](<viewportbounds(for_).md>) — Returns the current viewport, which is the view visible bounds plus the overdraw area.
