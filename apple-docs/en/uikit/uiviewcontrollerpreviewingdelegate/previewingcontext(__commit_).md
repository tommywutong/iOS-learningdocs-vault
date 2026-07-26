---
title: 'previewingContext(_:commit:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+（13.0 起废弃）, iPadOS 9.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 9.0+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiviewcontrollerpreviewingdelegate/previewingcontext(_:commit:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewingdelegate/previewingcontext(_:commit:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollerpreviewingdelegate/previewingcontext%28_%3Acommit%3A%29.json'
content_hash: 'sha256:ee8510bd73d24256'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerPreviewingDelegate](../uiviewcontrollerpreviewingdelegate.md)

# previewingContext(_:commit:)

<sub>Instance Method</sub>

Called to let you prepare the presentation of a commit (pop) view from your commit view controller.

> [!warning] Deprecated
> For more information, see [UIViewControllerPreviewingDelegate](../uiviewcontrollerpreviewingdelegate.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func previewingContext(_ previewingContext: any UIViewControllerPreviewing, commit viewControllerToCommit: UIViewController)
```

## Parameters

- `previewingContext` — The context object for the previewing view controller.

- `viewControllerToCommit` — The view controller whose view your implementation of this method is moving into place as a commit (pop) view.

## Discussion

Implement this method to configure and present the commit (pop) view controller, in a way that is appropriate for your app.

For example, to present the commit view controller’s view in a navigation controller, call the navigation controller’s [- showViewController:sender:](<../uinavigationcontroller/show(__sender_).md>) method; to present the view modally, you could call the [- presentViewController:animated:completion:](<../uiviewcontroller/present(__animated_completion_).md>) method.

## See Also

### Providing preview and commit views for 3D Touch

- [- previewingContext:viewControllerForLocation:](<previewingcontext(__viewcontrollerforlocation_).md>) — Called when the user has pressed a source view in a previewing view controller, thereby obtaining a surrounding blur to indicate that a preview (peek) is available. _(deprecated)_
