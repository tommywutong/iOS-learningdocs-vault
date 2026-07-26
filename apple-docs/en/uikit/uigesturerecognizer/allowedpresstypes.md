---
title: allowedPressTypes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigesturerecognizer/allowedpresstypes
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/allowedpresstypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/allowedpresstypes.json'
content_hash: 'sha256:3c67aaf49e5e03b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# allowedPressTypes

<sub>Instance Property</sub>

An array of press types used to distinguish the type of button press.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var allowedPressTypes: [NSNumber] { get set }
```

## Discussion

This property is an array of `UIPressTypes` that activates the gesture recognizer to distinguish the type of button press. The default press type is [UIPressTypeSelect](../uipress/presstype/select.md). When this property is set to an empty array, the gesture recognizer will respond to taps like a touch pad like surface. For a list of possible press types, see [PressType](../uipress/presstype.md) enumeration in the [UIPress](../uipress.md).

## See Also

### Recognizing different gestures

- [allowedTouchTypes](allowedtouchtypes.md) — An array of touch types used to distinguish type of touches.
- [requiresExclusiveTouchType](requiresexclusivetouchtype.md) — A Boolean value that indicates whether the gesture recognizer considers touches of different types simultaneously.
