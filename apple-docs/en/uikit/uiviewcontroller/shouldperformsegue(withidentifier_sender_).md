---
title: 'shouldPerformSegue(withIdentifier:sender:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiviewcontroller/shouldperformsegue(withidentifier:sender:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/shouldperformsegue(withidentifier:sender:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/shouldperformsegue%28withidentifier%3Asender%3A%29.json'
content_hash: 'sha256:d23efae536824974'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# shouldPerformSegue(withIdentifier:sender:)

<sub>Instance Method</sub>

Determines whether the segue with the specified identifier should be performed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func shouldPerformSegue(withIdentifier identifier: String, sender: Any?) -> Bool
```

## Parameters

- `identifier` — The string that identifies the triggered segue. In Interface Builder, you specify the segue’s identifier string in the attributes inspector. This string is used only for locating the segue inside the storyboard.

- `sender` — The object that initiated the segue. This object is made available for informational purposes during the actual segue.

## Return Value

[true](../../swift/true.md) if the segue should be performed or [false](../../swift/false.md) if it should be ignored.

## Discussion

Subclasses can override this method and use it to perform segues conditionally based on current conditions. If you do not implement this method, all segues are performed.

## See Also

### Performing segues

- [- prepareForSegue:sender:](<prepare(for_sender_).md>) — Notifies the view controller that a segue is about to be performed.
- [- performSegueWithIdentifier:sender:](<performsegue(withidentifier_sender_).md>) — Initiates the segue with the specified identifier from the current view controller’s storyboard file.
- [- allowedChildViewControllersForUnwindingFromSource:](<allowedchildrenforunwinding(from_).md>) — Returns an array of child view controllers to search for an unwind segue destination.
- [- childViewControllerContainingSegueSource:](<childcontaining(__).md>) — Returns the child view controller that contains the source of the unwind segue.
- [- canPerformUnwindSegueAction:fromViewController:sender:](<canperformunwindsegueaction(__from_sender_).md>) — Called on a view controller to determine whether it responds to an unwind action.
- [- unwindForSegue:towardsViewController:](<unwind(for_towards_).md>) — Called when an unwind segue transitions to a new view controller.
