---
title: 'previewingContext(_:viewControllerForLocation:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+（13.0 起废弃）, iPadOS 9.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 9.0+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiviewcontrollerpreviewingdelegate/previewingcontext(_:viewcontrollerforlocation:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollerpreviewingdelegate/previewingcontext(_:viewcontrollerforlocation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollerpreviewingdelegate/previewingcontext%28_%3Aviewcontrollerforlocation%3A%29.json'
content_hash: 'sha256:3a2c551661d441eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerPreviewingDelegate](../uiviewcontrollerpreviewingdelegate.md)

# previewingContext(_:viewControllerForLocation:)

<sub>Instance Method</sub>

Called when the user has pressed a source view in a previewing view controller, thereby obtaining a surrounding blur to indicate that a preview (peek) is available.

> [!warning] Deprecated
> For more information, see [UIViewControllerPreviewingDelegate](../uiviewcontrollerpreviewingdelegate.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func previewingContext(_ previewingContext: any UIViewControllerPreviewing, viewControllerForLocation location: CGPoint) -> UIViewController?
```

## Parameters

- `previewingContext` — The context object for the previewing view controller.

- `location` — The location of the touch in the source view’s coordinate system.

## Return Value

The view controller whose view you want to provide as the preview (peek), or `nil` to disable preview..

## Discussion

Implement this method to return the preview view controller.

To indicate that a particular portion of the source view is responding to the user’s force touch, set the context object’s [sourceRect](../uiviewcontrollerpreviewing/sourcerect.md) property to the desired rectangle. For example, if the context object’s [sourceView](../uiviewcontrollerpreviewing/sourceview.md) property is a table view, you can set the [sourceRect](../uiviewcontrollerpreviewing/sourcerect.md) property to the frame of the row indicated by the `location` parameter’s value. When the system presents the preview (peek), it appears to originate from the selected row.

You can disable preview by returning `nil` from this method.

## See Also

### Providing preview and commit views for 3D Touch

- [- previewingContext:commitViewController:](<previewingcontext(__commit_).md>) — Called to let you prepare the presentation of a commit (pop) view from your commit view controller. _(deprecated)_
