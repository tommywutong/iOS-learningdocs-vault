---
title: allowedTouchTypes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigesturerecognizer/allowedtouchtypes
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/allowedtouchtypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/allowedtouchtypes.json'
content_hash: 'sha256:c76e87601810d3ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# allowedTouchTypes

<sub>Instance Property</sub>

An array of touch types used to distinguish type of touches.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var allowedTouchTypes: [NSNumber] { get set }
```

## Discussion

This property is an array of touch types that recognizes whether the touch is direct or indirect. For a list of all possible touch types, see [TouchType](../uitouch/touchtype.md) enumeration in [UITouch](../uitouch.md). The default value of this property contains all touch types.

## See Also

### Recognizing different gestures

- [allowedPressTypes](allowedpresstypes.md) — An array of press types used to distinguish the type of button press.
- [requiresExclusiveTouchType](requiresexclusivetouchtype.md) — A Boolean value that indicates whether the gesture recognizer considers touches of different types simultaneously.
