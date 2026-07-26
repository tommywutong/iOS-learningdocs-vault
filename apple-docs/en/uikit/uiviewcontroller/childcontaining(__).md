---
title: 'childContaining(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiviewcontroller/childcontaining(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/childcontaining(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/childcontaining%28_%3A%29.json'
content_hash: 'sha256:c5f79a1e5e5e8cea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# childContaining(_:)

<sub>Instance Method</sub>

Returns the child view controller that contains the source of the unwind segue.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func childContaining(_ source: UIStoryboardUnwindSegueSource) -> UIViewController?
```

## Parameters

- `source` — The unwind segue source object containing information about the unwind segue.

## Return Value

The view controller that contains the segue source.

## Discussion

Container view controllers call this method to identify the child view controller that is the source of the unwind segue. Typically, you call this method from your [- allowedChildViewControllersForUnwindingFromSource:](<allowedchildrenforunwinding(from_).md>) method so that you can remove the corresponding view controller from the returned list of children.

## See Also

### Performing segues

- [- shouldPerformSegueWithIdentifier:sender:](<shouldperformsegue(withidentifier_sender_).md>) — Determines whether the segue with the specified identifier should be performed.
- [- prepareForSegue:sender:](<prepare(for_sender_).md>) — Notifies the view controller that a segue is about to be performed.
- [- performSegueWithIdentifier:sender:](<performsegue(withidentifier_sender_).md>) — Initiates the segue with the specified identifier from the current view controller’s storyboard file.
- [- allowedChildViewControllersForUnwindingFromSource:](<allowedchildrenforunwinding(from_).md>) — Returns an array of child view controllers to search for an unwind segue destination.
- [- canPerformUnwindSegueAction:fromViewController:sender:](<canperformunwindsegueaction(__from_sender_).md>) — Called on a view controller to determine whether it responds to an unwind action.
- [- unwindForSegue:towardsViewController:](<unwind(for_towards_).md>) — Called when an unwind segue transitions to a new view controller.
