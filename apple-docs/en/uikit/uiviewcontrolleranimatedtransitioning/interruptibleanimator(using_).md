---
title: 'interruptibleAnimator(using:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiviewcontrolleranimatedtransitioning/interruptibleanimator(using:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrolleranimatedtransitioning/interruptibleanimator(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrolleranimatedtransitioning/interruptibleanimator%28using%3A%29.json'
content_hash: 'sha256:83914d19322f00a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerAnimatedTransitioning](../uiviewcontrolleranimatedtransitioning.md)

# interruptibleAnimator(using:)

<sub>Instance Method</sub>

Returns the interruptible animator to use during the transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func interruptibleAnimator(using transitionContext: any UIViewControllerContextTransitioning) -> any UIViewImplicitlyAnimating
```

## Parameters

- `transitionContext` — The context object containing information to use during the transition.

## Return Value

An animator object that supports the modification of its running animations.

## Discussion

Implement this method when you want to perform your transitions using an interruptible animator object, such as a [UIViewPropertyAnimator](../uiviewpropertyanimator.md) object. You must return the same animator object for the duration of the transition.
