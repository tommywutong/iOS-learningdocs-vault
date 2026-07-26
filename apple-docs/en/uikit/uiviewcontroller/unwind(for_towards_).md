---
title: 'unwind(for:towards:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiviewcontroller/unwind(for:towards:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/unwind(for:towards:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/unwind%28for%3Atowards%3A%29.json'
content_hash: 'sha256:4c23f38f00cad74d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# unwind(for:towards:)

<sub>Instance Method</sub>

Called when an unwind segue transitions to a new view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func unwind(for unwindSegue: UIStoryboardSegue, towards subsequentVC: UIViewController)
```

## Parameters

- `unwindSegue` — The unwind segue being performed.

- `subsequentVC` — The view controller closest to the current controller that represents the transition direction. Container view controllers should configure themselves so that this view controller is displayed.

## Discussion

During the execution of an unwind segue, UIKit calls this method on any view controllers in the unwind path to give them an opportunity to reconfigure themselves. Container view controllers must implement this method and use to display the view controller in the `subsequentVC` parameter. For example, a tab bar controller selects the tab containing the specified view controller. Noncontainer view controllers should not override this method.

## See Also

### Performing segues

- [- shouldPerformSegueWithIdentifier:sender:](<shouldperformsegue(withidentifier_sender_).md>) — Determines whether the segue with the specified identifier should be performed.
- [- prepareForSegue:sender:](<prepare(for_sender_).md>) — Notifies the view controller that a segue is about to be performed.
- [- performSegueWithIdentifier:sender:](<performsegue(withidentifier_sender_).md>) — Initiates the segue with the specified identifier from the current view controller’s storyboard file.
- [- allowedChildViewControllersForUnwindingFromSource:](<allowedchildrenforunwinding(from_).md>) — Returns an array of child view controllers to search for an unwind segue destination.
- [- childViewControllerContainingSegueSource:](<childcontaining(__).md>) — Returns the child view controller that contains the source of the unwind segue.
- [- canPerformUnwindSegueAction:fromViewController:sender:](<canperformunwindsegueaction(__from_sender_).md>) — Called on a view controller to determine whether it responds to an unwind action.
