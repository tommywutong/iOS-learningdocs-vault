---
title: 'preferredContentSizeDidChange(forChildContentContainer:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontentcontainer/preferredcontentsizedidchange(forchildcontentcontainer:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontentcontainer/preferredcontentsizedidchange(forchildcontentcontainer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentcontainer/preferredcontentsizedidchange%28forchildcontentcontainer%3A%29.json'
content_hash: 'sha256:48caaaddab05133c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContentContainer](../uicontentcontainer.md)

# preferredContentSizeDidChange(forChildContentContainer:)

<sub>Instance Method</sub>

Notifies an interested controller that the preferred content size of one of its children changed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func preferredContentSizeDidChange(forChildContentContainer container: any UIContentContainer)
```

## Parameters

- `container` — The child view controller whose preferred content size has changed.

## Discussion

UIKit calls this method on a container view controller when the [preferredContentSize](preferredcontentsize.md) property of one of its child view controllers changes. Similarly, if the view controller is managed by a presentation controller, UIKit calls this method on the presentation controller to let it know of the change. The parent view controller or presentation controller can use this method to initiate layout adjustments based on the new size information.

## See Also

### Responding to changes in child view controllers

- [- sizeForChildContentContainer:withParentContainerSize:](<size(forchildcontentcontainer_withparentcontainersize_).md>) — Returns the size of the specified child view controller’s content.
- [- systemLayoutFittingSizeDidChangeForChildContentContainer:](<systemlayoutfittingsizedidchange(forchildcontentcontainer_).md>) — Notifies the container that a child view controller was resized using Auto Layout.
- [preferredContentSize](preferredcontentsize.md) — The preferred size for the container’s content.
