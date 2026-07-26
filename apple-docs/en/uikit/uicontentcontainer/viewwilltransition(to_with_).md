---
title: 'viewWillTransition(to:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontentcontainer/viewwilltransition(to:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontentcontainer/viewwilltransition(to:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentcontainer/viewwilltransition%28to%3Awith%3A%29.json'
content_hash: 'sha256:8f298da0cbcd6711'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContentContainer](../uicontentcontainer.md)

# viewWillTransition(to:with:)

<sub>Instance Method</sub>

Notifies the container that the size of its view is about to change.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func viewWillTransition(to size: CGSize, with coordinator: any UIViewControllerTransitionCoordinator)
```

## Parameters

- `size` — The new size for the container’s view.

- `coordinator` — The transition coordinator object managing the size change. You can use this object to animate your changes or get information about the transition that is in progress.

## Discussion

UIKit calls this method before changing the size of a presented view controller’s view. You can override this method in your own objects and use it to perform additional tasks related to the size change. For example, a container view controller might use this method to override the traits of its embedded child view controllers. Use the provided `coordinator` object to animate any changes you make.

If you override this method in your custom view controllers, always call `super` at some point in your implementation so that UIKit can forward the size change message appropriately. View controllers forward the size change message to their views and child view controllers. Presentation controllers forward the size change to their presented view controller.

## See Also

### Related Documentation

- [- sizeForChildContentContainer:withParentContainerSize:](<size(forchildcontentcontainer_withparentcontainersize_).md>) — Returns the size of the specified child view controller’s content.

### Responding to environment changes

- [- willTransitionToTraitCollection:withTransitionCoordinator:](<willtransition(to_with_).md>) — Notifies the container that its trait collection changed.
