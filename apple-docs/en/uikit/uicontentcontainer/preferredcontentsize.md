---
title: preferredContentSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentcontainer/preferredcontentsize
source_url: 'https://developer.apple.com/documentation/uikit/uicontentcontainer/preferredcontentsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentcontainer/preferredcontentsize.json'
content_hash: 'sha256:4fa39bf97f0dbc68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContentContainer](../uicontentcontainer.md)

# preferredContentSize

<sub>Instance Property</sub>

The preferred size for the container’s content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var preferredContentSize: CGSize { get }
```

## Discussion

The [UIViewController](../uiviewcontroller.md) class implements a writable version of this property.

## See Also

### Responding to changes in child view controllers

- [- sizeForChildContentContainer:withParentContainerSize:](<size(forchildcontentcontainer_withparentcontainersize_).md>) — Returns the size of the specified child view controller’s content.
- [- preferredContentSizeDidChangeForChildContentContainer:](<preferredcontentsizedidchange(forchildcontentcontainer_).md>) — Notifies an interested controller that the preferred content size of one of its children changed.
- [- systemLayoutFittingSizeDidChangeForChildContentContainer:](<systemlayoutfittingsizedidchange(forchildcontentcontainer_).md>) — Notifies the container that a child view controller was resized using Auto Layout.
