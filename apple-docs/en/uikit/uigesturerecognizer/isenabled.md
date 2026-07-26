---
title: isEnabled
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigesturerecognizer/isenabled
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/isenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/isenabled.json'
content_hash: 'sha256:7ff61813a475f403'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# isEnabled

<sub>Instance Property</sub>

A Boolean property that indicates whether the gesture recognizer is enabled.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isEnabled: Bool { get set }
```

## Discussion

Disables a gesture recognizers so it does not receive touches. The default value is [true](../../swift/true.md). If you change this property to [false](../../swift/false.md) while a gesture recognizer is currently recognizing a gesture, the gesture recognizer transitions to a cancelled state.

## See Also

### Getting the recognizer’s state and view

- [state](state-swift.property.md) — The current state of the gesture recognizer.
- [State](state-swift.enum.md) — Constants that represent the current state a gesture recognizer is in.
- [view](view.md) — The view the gesture recognizer is attached to.
- [buttonMask](buttonmask.md) — A bit mask of the buttons in the gesture represented by the gesture recognizer.
- [modifierFlags](modifierflags.md) — The bit mask of modifier flags in the gesture represented by the gesture recognizer.
