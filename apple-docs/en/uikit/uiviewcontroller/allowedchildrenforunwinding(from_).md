---
title: 'allowedChildrenForUnwinding(from:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiviewcontroller/allowedchildrenforunwinding(from:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/allowedchildrenforunwinding(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/allowedchildrenforunwinding%28from%3A%29.json'
content_hash: 'sha256:dbc2a5755f5d8f23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# allowedChildrenForUnwinding(from:)

<sub>Instance Method</sub>

Returns an array of child view controllers to search for an unwind segue destination.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func allowedChildrenForUnwinding(from source: UIStoryboardUnwindSegueSource) -> [UIViewController]
```

## Parameters

- `source` — The unwind segue source object containing information about the unwind segue.

## Return Value

An array of view controllers representing the child view controllers to search. The order of the items in the array determines the search order.

## Discussion

UIKit calls this method when searching for the destination of an unwind segue. The default implementation returns the contents of the [childViewControllers](children.md) property minus the view controller returned by the [- childViewControllerContainingSegueSource:](<childcontaining(__).md>) method. You can override this method as needed in your custom container view controllers to change the search order. For example, a navigation controller reverses the order so that the search starts with the view controller at the top of the navigation stack.

## See Also

### Performing segues

- [- shouldPerformSegueWithIdentifier:sender:](<shouldperformsegue(withidentifier_sender_).md>) — Determines whether the segue with the specified identifier should be performed.
- [- prepareForSegue:sender:](<prepare(for_sender_).md>) — Notifies the view controller that a segue is about to be performed.
- [- performSegueWithIdentifier:sender:](<performsegue(withidentifier_sender_).md>) — Initiates the segue with the specified identifier from the current view controller’s storyboard file.
- [- childViewControllerContainingSegueSource:](<childcontaining(__).md>) — Returns the child view controller that contains the source of the unwind segue.
- [- canPerformUnwindSegueAction:fromViewController:sender:](<canperformunwindsegueaction(__from_sender_).md>) — Called on a view controller to determine whether it responds to an unwind action.
- [- unwindForSegue:towardsViewController:](<unwind(for_towards_).md>) — Called when an unwind segue transitions to a new view controller.
