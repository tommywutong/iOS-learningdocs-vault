---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidynamicanimator/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicanimator/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicanimator/delegate.json'
content_hash: 'sha256:64204cc4a1af67ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicAnimator](../uidynamicanimator.md)

# delegate

<sub>Instance Property</sub>

The delegate for responding to pausing or resumption of animation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var delegate: (any UIDynamicAnimatorDelegate)? { get set }
```

## Discussion

The methods for a dynamic animator delegate are described in [UIDynamicAnimatorDelegate](../uidynamicanimatordelegate.md).

## See Also

### Responding to animation changes

- [UIDynamicAnimatorDelegate](../uidynamicanimatordelegate.md) — To respond to the pausing or resumption of UIKit dynamic animation, configure a custom class to adopt the [UIDynamicAnimatorDelegate](../uidynamicanimatordelegate.md) protocol. Then, in a dynamic animator (an instance of the [UIDynamicAnimator](../uidynamicanimator.md) class), set the delegate to be an instance of your custom class.
