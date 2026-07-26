---
title: accessibilityTraits
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilityelement/accessibilitytraits
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilityelement/accessibilitytraits'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilityelement/accessibilitytraits.json'
content_hash: 'sha256:a53870570ab9347c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityElement](../uiaccessibilityelement.md)

# accessibilityTraits

<sub>Instance Property</sub>

The combination of traits that best characterize the accessibility element.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var accessibilityTraits: UIAccessibilityTraits { get set }
```

## Discussion

A trait describes a single aspect of an element’s behavior, state, or usage. Several traits are combined in this property (using an OR operation) to give a complete picture of the element to an assistive application. See “Accessibility Traits” in [UIAccessibility](../uiaccessibility-protocol.md) for a complete list of traits.

UIKit provides an appropriate combination of traits for all standard controls and views. When combining traits for a custom accessibility element, be sure to:

- Use common sense. Don’t combine traits that characterize the element in mutually exclusive ways, such as combining the button and search-field traits.
- Combine the traits you select with the superclass’s traits. Specifically, always combine your custom traits with `[super accessibilityTraits]` in the method you use to set a custom element’s traits.

## See Also

### Accessing the attributes of an accessibility element

- [accessibilityLabel](accessibilitylabel.md) — A string that succinctly identifies the accessibility element.
- [accessibilityHint](accessibilityhint.md) — A string that briefly describes the result of performing an action on the accessibility element.
- [accessibilityValue](accessibilityvalue.md) — A string that represents the current value of the accessibility element.
- [accessibilityFrame](accessibilityframe.md) — The frame of the accessibility element, in screen coordinates.
- [accessibilityFrameInContainerSpace](accessibilityframeincontainerspace.md) — The frame of the accessibility element, in the coordinate space of its container view.
