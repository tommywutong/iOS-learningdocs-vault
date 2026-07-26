---
title: 'didMove(toParent:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontroller/didmove(toparent:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/didmove(toparent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/didmove%28toparent%3A%29.json'
content_hash: 'sha256:5108c3ba6b213850'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# didMove(toParent:)

<sub>Instance Method</sub>

Called after the view controller is added or removed from a container view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func didMove(toParent parent: UIViewController?)
```

## Parameters

- `parent` — The parent view controller, or `nil` if there is no parent.

## Discussion

Your view controller can override this method when it wants to react to being added to a container.

If you are implementing your own container view controller, it must call the [- didMoveToParentViewController:](<didmove(toparent_).md>) method of the child view controller after the transition to the new controller is complete or, if there is no transition, immediately after calling the [- addChildViewController:](<addchild(__).md>) method.

The [- removeFromParentViewController](<removefromparent().md>) method automatically calls the [- didMoveToParentViewController:](<didmove(toparent_).md>) method of the child view controller after it removes the child.

## See Also

### Responding to containment events

- [- willMoveToParentViewController:](<willmove(toparent_).md>) — Called just before the view controller is added or removed from a container view controller.
