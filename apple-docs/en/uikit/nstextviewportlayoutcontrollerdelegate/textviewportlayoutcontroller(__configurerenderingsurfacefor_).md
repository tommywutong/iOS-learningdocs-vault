---
title: 'textViewportLayoutController(_:configureRenderingSurfaceFor:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:configurerenderingsurfacefor:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller(_:configurerenderingsurfacefor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextviewportlayoutcontrollerdelegate/textviewportlayoutcontroller%28_%3Aconfigurerenderingsurfacefor%3A%29.json'
content_hash: 'sha256:b248609ff0fd8830'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextViewportLayoutControllerDelegate](../nstextviewportlayoutcontrollerdelegate.md)

# textViewportLayoutController(_:configureRenderingSurfaceFor:)

<sub>Instance Method</sub>

The method the framework calls when the layout controller lays out a text layout fragment in the UI.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func textViewportLayoutController(_ textViewportLayoutController: NSTextViewportLayoutController, configureRenderingSurfaceFor textLayoutFragment: NSTextLayoutFragment)
```

## Parameters

- `textViewportLayoutController` — The `NSTextViewportLayoutController` associated with this text layout fragment.

- `textLayoutFragment` — An `NSTextLayoutFragment`.

## Discussion

The delegate presents the text layout fragment in the UI, for example, in a sublayer or a subview. Layout information such as `viewportBounds` on `textViewportLayoutController` isn’t up to date at the point of this call.

## See Also

### Responding to changes in the viewport

- [- textViewportLayoutControllerDidLayout:](<textviewportlayoutcontrollerdidlayout(__).md>) — The method the framework calls when the text viewport layout controller finishes its layout process.
- [- textViewportLayoutControllerWillLayout:](<textviewportlayoutcontrollerwilllayout(__).md>) — The method the framework calls before the text viewport layout controller starts its layout process.
- [- textViewportLayoutControllerReceivedSetNeedsLayout:](<textviewportlayoutcontrollerreceivedsetneedslayout(__).md>) — Triggers relayout of the view.
- [- viewportBoundsForTextViewportLayoutController:](<viewportbounds(for_).md>) — Returns the current viewport, which is the view visible bounds plus the overdraw area.
