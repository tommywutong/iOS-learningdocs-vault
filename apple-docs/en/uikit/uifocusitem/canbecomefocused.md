---
title: canBecomeFocused
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusitem/canbecomefocused
source_url: 'https://developer.apple.com/documentation/uikit/uifocusitem/canbecomefocused'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusitem/canbecomefocused.json'
content_hash: 'sha256:5239779a9372d605'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusItem](../uifocusitem.md)

# canBecomeFocused

<sub>Instance Property</sub>

A Boolean value that indicates whether the item can become focused.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var canBecomeFocused: Bool { get }
```

## Discussion

When the value of this property is [false](../../swift/false.md), the item is not focusable, even if it is visible in the user interface. For example, a subclass of [UIControl](../uicontrol.md) returns [false](../../swift/false.md) when it is not enabled.

Returning [true](../../swift/true.md) in this property means that the item is capable of being focused; it does not guarantee that the item is always focusable. Focusability is ultimately determined by the system. For example, if an item is visually obscured or offscreen, it may not be focusable. In addition, objects that conform to this protocol may have their own unique limitations. For example, a [UIView](../uiview.md) object is not focusable when user interaction is disabled, or when the view’s alpha value is equal to `0`.
