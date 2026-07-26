---
title: wantsInteractiveStart
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontrollerinteractivetransitioning/wantsinteractivestart
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollerinteractivetransitioning/wantsinteractivestart'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollerinteractivetransitioning/wantsinteractivestart.json'
content_hash: 'sha256:c1ee08b94e36b016'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerInteractiveTransitioning](../uiviewcontrollerinteractivetransitioning.md)

# wantsInteractiveStart

<sub>Instance Property</sub>

A Boolean value indicating whether the transition is interactive when it starts.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var wantsInteractiveStart: Bool { get }
```

## Discussion

The value of this property is [true](../../swift/true.md) when the transition is interactive from the moment it starts. The property is [false](../../swift/false.md) when the transition starts off as noninteractive. However, even a transition that starts off as noninteractive may become interactive later if it implements the [- interruptibleAnimatorForTransition:](<../uiviewcontrolleranimatedtransitioning/interruptibleanimator(using_).md>) method of the [UIViewControllerAnimatedTransitioning](../uiviewcontrolleranimatedtransitioning.md) protocol.

## See Also

### Starting an interactive transition

- [- startInteractiveTransition:](<startinteractivetransition(__).md>) — Called when the system needs to set up the interactive portions of a view controller transition and start the animations.
