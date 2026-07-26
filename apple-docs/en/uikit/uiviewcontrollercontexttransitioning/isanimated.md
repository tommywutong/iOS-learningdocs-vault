---
title: isAnimated
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontrollercontexttransitioning/isanimated
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontrollercontexttransitioning/isanimated'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontrollercontexttransitioning/isanimated.json'
content_hash: 'sha256:bd4ee942e5176e31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewControllerContextTransitioning](../uiviewcontrollercontexttransitioning.md)

# isAnimated

<sub>Instance Property</sub>

A Boolean value indicating whether the transition should be animated.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isAnimated: Bool { get }
```

## Discussion

The value of this property is always [true](../../swift/true.md) for modal presentation styles other than the [UIModalPresentationCustom](../uimodalpresentationstyle/custom.md) style. When the modal presentation style is [UIModalPresentationCustom](../uimodalpresentationstyle/custom.md), the value is [true](../../swift/true.md) if the transition should be animated or [false](../../swift/false.md) if it should not. Use this value to determine whether you need to animate a custom transition into place, or whether you should install the final views into the container without animating the changes.

## See Also

### Getting the transition behaviors

- [interactive](isinteractive.md) — A Boolean value indicating whether the transition is currently interactive.
- [presentationStyle](presentationstyle.md) — Returns the presentation style for the view controller transition.
