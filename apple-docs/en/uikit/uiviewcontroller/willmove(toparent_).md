---
title: 'willMove(toParent:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/willmove(toparent:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/willmove(toparent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/willmove%28toparent%3A%29.json'
content_hash: 'sha256:8974c2b03d749a84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# willMove(toParent:)

<sub>Instance Method</sub>

Called just before the view controller is added or removed from a container view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func willMove(toParent parent: UIViewController?)
```

## Parameters

- `parent` — The parent view controller, or `nil` if there is no parent.

## Discussion

Your view controller can override this method when it needs to know that it has been added to a container.

If you are implementing your own container view controller, it must call the [- willMoveToParentViewController:](<willmove(toparent_).md>) method of the child view controller before calling the [- removeFromParentViewController](<removefromparent().md>) method, passing in a parent value of `nil`.

When your custom container calls the [- addChildViewController:](<addchild(__).md>) method, it automatically calls the [- willMoveToParentViewController:](<willmove(toparent_).md>) method of the view controller to be added as a child before adding it.

## See Also

### Responding to containment events

- [- didMoveToParentViewController:](<didmove(toparent_).md>) — Called after the view controller is added or removed from a container view controller.
