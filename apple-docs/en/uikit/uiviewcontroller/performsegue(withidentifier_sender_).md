---
title: 'performSegue(withIdentifier:sender:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiviewcontroller/performsegue(withidentifier:sender:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/performsegue(withidentifier:sender:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/performsegue%28withidentifier%3Asender%3A%29.json'
content_hash: 'sha256:cec9f353bdf1cfdd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# performSegue(withIdentifier:sender:)

<sub>Instance Method</sub>

Initiates the segue with the specified identifier from the current view controller’s storyboard file.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func performSegue(withIdentifier identifier: String, sender: Any?)
```

## Parameters

- `identifier` — The string that identifies the triggered segue. In Interface Builder, you specify the segue’s identifier string in the attributes inspector. This method throws an [Exception handling](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ExceptionHandling.html#//apple_ref/doc/uid/TP40008195-CH18) if there is no segue with the specified identifier.

- `sender` — The object that you want to use to initiate the segue. This object is made available for informational purposes during the actual segue.

## Discussion

Normally, segues are initiated automatically and not using this method. However, you can use this method in cases where the segue could not be configured in your storyboard file. For example, you might call it from a custom action handler used in response to shake or accelerometer events.

The current view controller must have been loaded from a storyboard. If its [storyboard](storyboard.md) property is `nil`, perhaps because you allocated and initialized the view controller yourself, this method throws an exception.

## See Also

### Performing segues

- [- shouldPerformSegueWithIdentifier:sender:](<shouldperformsegue(withidentifier_sender_).md>) — Determines whether the segue with the specified identifier should be performed.
- [- prepareForSegue:sender:](<prepare(for_sender_).md>) — Notifies the view controller that a segue is about to be performed.
- [- allowedChildViewControllersForUnwindingFromSource:](<allowedchildrenforunwinding(from_).md>) — Returns an array of child view controllers to search for an unwind segue destination.
- [- childViewControllerContainingSegueSource:](<childcontaining(__).md>) — Returns the child view controller that contains the source of the unwind segue.
- [- canPerformUnwindSegueAction:fromViewController:sender:](<canperformunwindsegueaction(__from_sender_).md>) — Called on a view controller to determine whether it responds to an unwind action.
- [- unwindForSegue:towardsViewController:](<unwind(for_towards_).md>) — Called when an unwind segue transitions to a new view controller.
