---
title: 'collapseSecondaryViewController(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/collapsesecondaryviewcontroller(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/collapsesecondaryviewcontroller(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/collapsesecondaryviewcontroller%28_%3Afor%3A%29.json'
content_hash: 'sha256:d3a79fd3a37a86b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# collapseSecondaryViewController(_:for:)

<sub>Instance Method</sub>

Called when a split view controller transitions to a compact-width size class.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func collapseSecondaryViewController(_ secondaryViewController: UIViewController, for splitViewController: UISplitViewController)
```

## Parameters

- `secondaryViewController` — The secondary view controller associated with the split view controller.

- `splitViewController` — The current split view controller.

## Discussion

This method provides default behavior when you do not overwrite the [- splitViewController:collapseSecondaryViewController:ontoPrimaryViewController:](<../uisplitviewcontrollerdelegate/splitviewcontroller(__collapsesecondary_onto_).md>) method. The primary view controller associated with the split view controller is displayed.

## See Also

### Adapting to environment changes

- [- separateSecondaryViewControllerForSplitViewController:](<separatesecondaryviewcontroller(for_).md>) — Called when a split view controller transitions to a regular-width size class.
