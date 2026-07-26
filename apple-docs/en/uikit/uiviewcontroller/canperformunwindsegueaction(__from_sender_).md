---
title: 'canPerformUnwindSegueAction(_:from:sender:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiviewcontroller/canperformunwindsegueaction(_:from:sender:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/canperformunwindsegueaction(_:from:sender:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/canperformunwindsegueaction%28_%3Afrom%3Asender%3A%29.json'
content_hash: 'sha256:a86bc125673bb7a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# canPerformUnwindSegueAction(_:from:sender:)

<sub>Instance Method</sub>

Called on a view controller to determine whether it responds to an unwind action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func canPerformUnwindSegueAction(_ action: Selector, from fromViewController: UIViewController, sender: Any?) -> Bool
```

## Parameters

- `action` — The unwind action to invoke on your view controller.

- `fromViewController` — The view controller that initiated the unwind action.

- `sender` — The object that triggered the action.

## Return Value

[true](../../swift/true.md) if the view controller handles the unwind action, otherwise [false](../../swift/false.md).

## Discussion

When an unwind segue is triggered, UIKit uses this method and the [- allowedChildViewControllersForUnwindingFromSource:](<allowedchildrenforunwinding(from_).md>) method to locate a suitable view controller to handle the unwind segue.

The default implementation of this method returns [true](../../swift/true.md) when the current view controller implements the `action` method and is not the same view controller as the one in the `fromViewController` parameter. You can override this method as needed to change the default behavior. For example, you might return [false](../../swift/false.md) if the current view controller does not make a suitable return target when unwinding from the specified view controller.

## See Also

### Performing segues

- [- shouldPerformSegueWithIdentifier:sender:](<shouldperformsegue(withidentifier_sender_).md>) — Determines whether the segue with the specified identifier should be performed.
- [- prepareForSegue:sender:](<prepare(for_sender_).md>) — Notifies the view controller that a segue is about to be performed.
- [- performSegueWithIdentifier:sender:](<performsegue(withidentifier_sender_).md>) — Initiates the segue with the specified identifier from the current view controller’s storyboard file.
- [- allowedChildViewControllersForUnwindingFromSource:](<allowedchildrenforunwinding(from_).md>) — Returns an array of child view controllers to search for an unwind segue destination.
- [- childViewControllerContainingSegueSource:](<childcontaining(__).md>) — Returns the child view controller that contains the source of the unwind segue.
- [- unwindForSegue:towardsViewController:](<unwind(for_towards_).md>) — Called when an unwind segue transitions to a new view controller.
