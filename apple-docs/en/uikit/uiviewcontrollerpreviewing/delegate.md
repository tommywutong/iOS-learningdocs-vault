---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（13.0 起废弃）, iPadOS 9.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 9.0+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiviewcontrollerpreviewing/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewing/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollerpreviewing/delegate.json'
content_hash: 'sha256:d19ff8b34b25e0e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerPreviewing](../uiviewcontrollerpreviewing.md)

# delegate

<sub>Instance Property</sub>

The previewing view controller’s delegate for managing preview (peek) and commit (pop) view controllers.

> [!warning] Deprecated
> For more information, see [UIViewControllerPreviewing](../uiviewcontrollerpreviewing.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var delegate: any UIViewControllerPreviewingDelegate { get }
```

## Discussion

Set a previewing view controller’s 3D Touch delegate when you register the view controller by calling its [- registerForPreviewingWithDelegate:sourceView:](<../uiviewcontroller/registerforpreviewing(with_sourceview_).md>) method.

For information on the methods the delegate can implement, read [UIViewControllerPreviewingDelegate](../uiviewcontrollerpreviewingdelegate.md).

## See Also

### Accessing properties of a 3D Touch previewing view controller

- [sourceView](sourceview.md) — A source view, in a previewing view controller’s view hierarchy, responds to a 3D Touch by the user. _(deprecated)_
