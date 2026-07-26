---
title: 'printInteractionControllerParentViewController(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontrollerparentviewcontroller(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontrollerparentviewcontroller(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiprintinteractioncontrollerdelegate/printinteractioncontrollerparentviewcontroller%28_%3A%29.json'
content_hash: 'sha256:fec1731db1d03dc6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPrintInteractionControllerDelegate](../uiprintinteractioncontrollerdelegate.md)

# printInteractionControllerParentViewController(_:)

<sub>Instance Method</sub>

Returns a parent view controller for managing the printing-options view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func printInteractionControllerParentViewController(_ printInteractionController: UIPrintInteractionController) -> UIViewController?
```

## Parameters

- `printInteractionController` — The shared instance of [UIPrintInteractionController](../uiprintinteractioncontroller.md) that is managing the print job.

## Return Value

The view controller that is to be the parent of the print-interaction controller managing the printing-options view. Return `nil` for the standard presentation behavior.

## Discussion

This method allows an application to present the print-options view from a view controller of their own choosing. The parent view controller returned must be a [UIViewController](../uiviewcontroller.md) object, such as a [UINavigationController](../uinavigationcontroller.md) object or a generic view controller. A common strategy for embedding is to create a [UINavigationController](../uinavigationcontroller.md) object as the content view controller ([contentViewController](../uipopovercontroller/contentviewcontroller.md) property) of a [UIPopoverController](../uipopovercontroller.md) object and return that. UIKit can push the returned view controller onto the stack if its parent is a navigation controller or present it modally if it isn’t.

This method is invoked in any of the `present...` methods of the [UIPrintInteractionController](../uiprintinteractioncontroller.md) class (for example, [- presentAnimated:completionHandler:](<../uiprintinteractioncontroller/present(animated_completionhandler_).md>)).
