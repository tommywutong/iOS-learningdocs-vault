---
title: accessibilityFrame
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilityelement/accessibilityframe
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilityelement/accessibilityframe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilityelement/accessibilityframe.json'
content_hash: 'sha256:8df1d6cd18d3eb5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityElement](../uiaccessibilityelement.md)

# accessibilityFrame

<sub>Instance Property</sub>

The frame of the accessibility element, in screen coordinates.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var accessibilityFrame: CGRect { get set }
```

## Discussion

When you create an accessibility element to represent an element in your application, you must set this property to the `CGRect` structure that specifies the object’s screen location and size. (Objects that inherit from `UIView` include this information by default.)

Assigning a new value to this property changes the value of the [accessibilityFrameInContainerSpace](accessibilityframeincontainerspace.md) property to [CGRectNull](../../coregraphics/cgrectnull.md).

## See Also

### Related Documentation

- [UIAccessibilityConvertFrameToScreenCoordinates](<../uiaccessibility/converttoscreencoordinates(__in_)-9ziiu.md>) — Converts the specified rectangle from view coordinates to screen coordinates.

### Accessing the attributes of an accessibility element

- [accessibilityLabel](accessibilitylabel.md) — A string that succinctly identifies the accessibility element.
- [accessibilityHint](accessibilityhint.md) — A string that briefly describes the result of performing an action on the accessibility element.
- [accessibilityValue](accessibilityvalue.md) — A string that represents the current value of the accessibility element.
- [accessibilityFrameInContainerSpace](accessibilityframeincontainerspace.md) — The frame of the accessibility element, in the coordinate space of its container view.
- [accessibilityTraits](accessibilitytraits.md) — The combination of traits that best characterize the accessibility element.
