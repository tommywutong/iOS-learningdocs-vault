---
title: 'size(forChildContentContainer:withParentContainerSize:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontentcontainer/size(forchildcontentcontainer:withparentcontainersize:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontentcontainer/size(forchildcontentcontainer:withparentcontainersize:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentcontainer/size%28forchildcontentcontainer%3Awithparentcontainersize%3A%29.json'
content_hash: 'sha256:c75cc7370440a948'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContentContainer](../uicontentcontainer.md)

# size(forChildContentContainer:withParentContainerSize:)

<sub>Instance Method</sub>

Returns the size of the specified child view controller’s content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func size(forChildContentContainer container: any UIContentContainer, withParentContainerSize parentSize: CGSize) -> CGSize
```

## Parameters

- `container` — The child view controller.

- `parentSize` — The size of the parent view controller.

## Return Value

The size to apply to the child view controller.

## Discussion

Container view controllers use this method to return the sizes for their child view controllers. UIKit calls the method as part of the default implementation of the [- viewWillTransitionToSize:withTransitionCoordinator:](<viewwilltransition(to_with_).md>) method for view controllers. It calls the method once for each child view controller embedded in the view controller. If you’re implementing a custom container view controller, you should override this method and use it to return the sizes of the contained children.

View controllers and presentation controllers return the value in `parentSize` by default.

## See Also

### Responding to changes in child view controllers

- [- preferredContentSizeDidChangeForChildContentContainer:](<preferredcontentsizedidchange(forchildcontentcontainer_).md>) — Notifies an interested controller that the preferred content size of one of its children changed.
- [- systemLayoutFittingSizeDidChangeForChildContentContainer:](<systemlayoutfittingsizedidchange(forchildcontentcontainer_).md>) — Notifies the container that a child view controller was resized using Auto Layout.
- [preferredContentSize](preferredcontentsize.md) — The preferred size for the container’s content.
