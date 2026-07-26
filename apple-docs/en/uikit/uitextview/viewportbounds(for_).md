---
title: 'viewportBounds(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift, occ, occ]
beta: true
deprecated: false
doc_path: '/documentation/uikit/uitextview/viewportbounds(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/viewportbounds(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/viewportbounds%28for%3A%29.json'
content_hash: 'sha256:12e65c4cf45e5c05'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# viewportBounds(for:)

<sub>Instance Method</sub>

`NSTextViewportLayoutControllerDelegate` method that the framework calls to request the current viewport, which is the view visible bounds plus the overdraw area. Requires a call to super.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func viewportBounds(for textViewportLayoutController: NSTextViewportLayoutController) -> CGRect
```

## See Also

### Customizing viewport layout

- [- textViewportLayoutControllerWillLayout:](<textviewportlayoutcontrollerwilllayout(__).md>) — `NSTextViewportLayoutControllerDelegate` method that the framework calls when the text viewport layout controller starts its layout process. Requires a call to super. _(beta)_
- [- textViewportLayoutControllerDidLayout:](<textviewportlayoutcontrollerdidlayout(__).md>) — `NSTextViewportLayoutControllerDelegate` method that the framework calls when the text viewport layout controller finishes its layout process. Requires a call to super. _(beta)_
- [- textViewportLayoutControllerReceivedSetNeedsLayout:](<textviewportlayoutcontrollerreceivedsetneedslayout(__).md>) — `NSTextViewportLayoutControllerDelegate` method that the framework calls when the text viewport layout controller receives a `setNeedsLayout` call. Requires a call to super. _(beta)_
