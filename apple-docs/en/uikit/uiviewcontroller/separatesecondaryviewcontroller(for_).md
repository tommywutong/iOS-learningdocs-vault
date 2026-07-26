---
title: 'separateSecondaryViewController(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/separatesecondaryviewcontroller(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/separatesecondaryviewcontroller(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/separatesecondaryviewcontroller%28for%3A%29.json'
content_hash: 'sha256:6da4919fc30cd4ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# separateSecondaryViewController(for:)

<sub>Instance Method</sub>

Called when a split view controller transitions to a regular-width size class.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func separateSecondaryViewController(for splitViewController: UISplitViewController) -> UIViewController?
```

## Parameters

- `splitViewController` — The current split view controller.

## Return Value

The designated secondary view controller for the split view controller.

## Discussion

This method provides default behavior when you do not overwrite the [- splitViewController:separateSecondaryViewControllerFromPrimaryViewController:](<../uisplitviewcontrollerdelegate/splitviewcontroller(__separatesecondaryfrom_).md>) method. The previous secondary view controller is returned.

## See Also

### Adapting to environment changes

- [- collapseSecondaryViewController:forSplitViewController:](<collapsesecondaryviewcontroller(__for_).md>) — Called when a split view controller transitions to a compact-width size class.
