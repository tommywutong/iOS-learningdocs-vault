---
title: 'transitionDuration(using:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontrolleranimatedtransitioning/transitionduration(using:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrolleranimatedtransitioning/transitionduration(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrolleranimatedtransitioning/transitionduration%28using%3A%29.json'
content_hash: 'sha256:a5b8af80df97c4ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerAnimatedTransitioning](../uiviewcontrolleranimatedtransitioning.md)

# transitionDuration(using:)

<sub>Instance Method</sub>

Asks your animator object for the duration (in seconds) of the transition animation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func transitionDuration(using transitionContext: (any UIViewControllerContextTransitioning)?) -> TimeInterval
```

## Parameters

- `transitionContext` — The context object containing information to use during the transition.

## Return Value

The duration, in seconds, of your custom transition animation.

## Discussion

UIKit calls this method to obtain the timing information for your animations. The value you provide should be the same value that you use when configuring the animations in your [- animateTransition:](<animatetransition(using_).md>) method. UIKit uses the value to synchronize the actions of other objects that might be involved in the transition. For example, a navigation controller uses the value to synchronize changes to the navigation bar.

When determining the value to return, assume there will be no user interaction during the transition—even if you plan to support user interactions at runtime.
