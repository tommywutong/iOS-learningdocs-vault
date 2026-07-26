---
title: 'systemLayoutFittingSizeDidChange(forChildContentContainer:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontentcontainer/systemlayoutfittingsizedidchange(forchildcontentcontainer:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontentcontainer/systemlayoutfittingsizedidchange(forchildcontentcontainer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentcontainer/systemlayoutfittingsizedidchange%28forchildcontentcontainer%3A%29.json'
content_hash: 'sha256:b99265b2b782212b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContentContainer](../uicontentcontainer.md)

# systemLayoutFittingSizeDidChange(forChildContentContainer:)

<sub>Instance Method</sub>

Notifies the container that a child view controller was resized using Auto Layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func systemLayoutFittingSizeDidChange(forChildContentContainer container: any UIContentContainer)
```

## Parameters

- `container` — The child view controller that received the resizing message.

## Discussion

This method is called when a view controller that doesn’t use Auto Layout has a child view controller that uses Auto Layout and the child view controller is resized. When the child view controller responds to the [- systemLayoutSizeFittingSize:](<../uiview/systemlayoutsizefitting(__).md>) method, the [- systemLayoutFittingSizeDidChangeForChildContentContainer:](<systemlayoutfittingsizedidchange(forchildcontentcontainer_).md>) method is sent to the parent view controller.

## See Also

### Responding to changes in child view controllers

- [- sizeForChildContentContainer:withParentContainerSize:](<size(forchildcontentcontainer_withparentcontainersize_).md>) — Returns the size of the specified child view controller’s content.
- [- preferredContentSizeDidChangeForChildContentContainer:](<preferredcontentsizedidchange(forchildcontentcontainer_).md>) — Notifies an interested controller that the preferred content size of one of its children changed.
- [preferredContentSize](preferredcontentsize.md) — The preferred size for the container’s content.
