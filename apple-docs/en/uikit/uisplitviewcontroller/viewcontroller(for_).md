---
title: 'viewController(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisplitviewcontroller/viewcontroller(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/viewcontroller(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/viewcontroller%28for%3A%29.json'
content_hash: 'sha256:9f079d9a8b991989'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewController](../uisplitviewcontroller.md)

# viewController(for:)

<sub>Instance Method</sub>

Returns the view controller associated with the specified column of the split view interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func viewController(for column: UISplitViewController.Column) -> UIViewController?
```

## Parameters

- `column` — The corresponding column of the split view interface. See [Column](column.md) for values.

## Return Value

The corresponding child view controller object.

## Discussion

This method doesn’t apply to classic split view controllers with a [style](style-swift.property.md) of [UISplitViewControllerStyleUnspecified](style-swift.enum/unspecified.md). For a classic split view controller, instead use the [viewControllers](viewcontrollers.md) property to get the view controllers in the split view interface.

## See Also

### Managing the child view controllers

- [Column](column.md) — Constants that describe the columns within the split view interface.
- [- setViewController:forColumn:](<setviewcontroller(__for_).md>) — Presents the provided view controller in the specified column of the split view interface.
- [viewControllers](viewcontrollers.md) — The array of view controllers the split view controller manages.
