---
title: requiresExclusiveTouchType
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.2+, iPadOS 9.2+, Mac Catalyst 13.1+, tvOS 9.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigesturerecognizer/requiresexclusivetouchtype
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/requiresexclusivetouchtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/requiresexclusivetouchtype.json'
content_hash: 'sha256:29f31d600545601e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# requiresExclusiveTouchType

<sub>Instance Property</sub>

A Boolean value that indicates whether the gesture recognizer considers touches of different types simultaneously.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var requiresExclusiveTouchType: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md), the gesture recognizer automatically ignores new touches whose type doesn’t match the type of the initial touch. When the value is [false](../../swift/false.md), the gesture recognizer receives all touches whose types are listed in the [allowedTouchTypes](allowedtouchtypes.md) property.

## See Also

### Recognizing different gestures

- [allowedPressTypes](allowedpresstypes.md) — An array of press types used to distinguish the type of button press.
- [allowedTouchTypes](allowedtouchtypes.md) — An array of touch types used to distinguish type of touches.
