---
title: 'prepare(for:sender:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiviewcontroller/prepare(for:sender:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/prepare(for:sender:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/prepare%28for%3Asender%3A%29.json'
content_hash: 'sha256:31886f82e300b056'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# prepare(for:sender:)

<sub>Instance Method</sub>

Notifies the view controller that a segue is about to be performed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func prepare(for segue: UIStoryboardSegue, sender: Any?)
```

## Parameters

- `segue` — The segue object containing information about the view controllers involved in the segue.

- `sender` — The object that initiated the segue. You might use this parameter to perform different actions based on which control (or other object) initiated the segue.

## Discussion

The default implementation of this method does nothing. Subclasses override this method and use it to configure the new view controller prior to it being displayed. The segue object contains information about the transition, including references to both view controllers that are involved.

Because segues can be triggered from multiple sources, you can use the information in the `segue` and `sender` parameters to disambiguate between different logical paths in your app. For example, if the segue originated from a table view, the sender parameter would identify the table view cell that the user tapped. You could then use that information to set the data on the destination view controller.

## See Also

### Performing segues

- [- shouldPerformSegueWithIdentifier:sender:](<shouldperformsegue(withidentifier_sender_).md>) — Determines whether the segue with the specified identifier should be performed.
- [- performSegueWithIdentifier:sender:](<performsegue(withidentifier_sender_).md>) — Initiates the segue with the specified identifier from the current view controller’s storyboard file.
- [- allowedChildViewControllersForUnwindingFromSource:](<allowedchildrenforunwinding(from_).md>) — Returns an array of child view controllers to search for an unwind segue destination.
- [- childViewControllerContainingSegueSource:](<childcontaining(__).md>) — Returns the child view controller that contains the source of the unwind segue.
- [- canPerformUnwindSegueAction:fromViewController:sender:](<canperformunwindsegueaction(__from_sender_).md>) — Called on a view controller to determine whether it responds to an unwind action.
- [- unwindForSegue:towardsViewController:](<unwind(for_towards_).md>) — Called when an unwind segue transitions to a new view controller.
