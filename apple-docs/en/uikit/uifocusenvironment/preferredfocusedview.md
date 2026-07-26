---
title: preferredFocusedView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（10.0 起废弃）, iPadOS 9.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 9.0+（10.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uifocusenvironment/preferredfocusedview
source_url: 'https://developer.apple.com/documentation/uikit/uifocusenvironment/preferredfocusedview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusenvironment/preferredfocusedview.json'
content_hash: 'sha256:69d965f6c982b297'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusEnvironment](../uifocusenvironment.md)

# preferredFocusedView

<sub>Instance Property</sub>

Specifies the view that should be focused if this environment is focused.

> [!warning] Deprecated
> Use [preferredFocusEnvironments](preferredfocusenvironments.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
weak optional var preferredFocusedView: UIView? { get }
```

## Discussion

Since [UIView](../uiview.md) conforms to [UIFocusEnvironment](../uifocusenvironment.md), any view returned from this property also has a preferred focused view. This creates a linked-list of views called the _preferred focus chain_. When focus updates to a new view, the focus engine will actually update focus to the deepest, focusable view in that new view’s preferred focus chain. Similarly, when setting initial focus, such as at application launch, the initial focused view is found by following the preferred focus chain from the root window.

By default, [UIView](../uiview.md) returns itself and [UIViewController](../uiviewcontroller.md) returns its root view. Returning `self` in a focusable view indicates that view should be focused. Returning `self` in an unfocusable view causes the focus engine to pick a default preferred focused view, by finding the closest focusable subview to the top-leading corner of the screen. Returning `nil` indicates that there is no preferred focused view.

## See Also

### Controlling user-generated focus movements

- [preferredFocusEnvironments](preferredfocusenvironments.md) — An array of focus environments, ordered by priority, to which this environment prefers focus to be directed during a focus update.
