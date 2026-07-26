---
title: sourceView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（13.0 起废弃）, iPadOS 9.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 9.0+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontrollerpreviewing/sourceview
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewing/sourceview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollerpreviewing/sourceview.json'
content_hash: 'sha256:2be2d44ea9cefbf8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerPreviewing](../uiviewcontrollerpreviewing.md)

# sourceView

<sub>Instance Property</sub>

A source view, in a previewing view controller’s view hierarchy, responds to a 3D Touch by the user.

> [!warning] Deprecated
> For more information, see [UIViewControllerPreviewing](../uiviewcontrollerpreviewing.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var sourceView: UIView { get }
```

## Discussion

Set the value of this property when you register a view controller to participate in 3D Touch. Do this in the view controller’s [- registerForPreviewingWithDelegate:sourceView:](<../uiviewcontroller/registerforpreviewing(with_sourceview_).md>) method.

When the user begins to press on the source view, the system blurs the surrounding area to let the user know that a preview (peek) is available. At this time, the system calls your [- previewingContext:viewControllerForLocation:](<../uiviewcontrollerpreviewingdelegate/previewingcontext(__viewcontrollerforlocation_).md>) method to let you prepare the presentation of a preview. If the user presses more deeply, the system presents the preview defined in your delegate method.

If the user presses deeper on the preview, the system navigates to the view you’ve specified in your [- previewingContext:commitViewController:](<../uiviewcontrollerpreviewingdelegate/previewingcontext(__commit_).md>) method. The commit view then fills the bounds of the app’s window.

## See Also

### Related Documentation

- [sourceRect](sourcerect.md) — The rectangle, in the source view’s coordinate system, that responds to a 3D Touch by a user and remains visually sharp while surrounding content blurs. _(deprecated)_

### Accessing properties of a 3D Touch previewing view controller

- [delegate](delegate.md) — The previewing view controller’s delegate for managing preview (peek) and commit (pop) view controllers. _(deprecated)_
