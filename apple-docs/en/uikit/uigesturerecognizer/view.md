---
title: view
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigesturerecognizer/view
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/view'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/view.json'
content_hash: 'sha256:642122e4c539c51a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# view

<sub>Instance Property</sub>

The view the gesture recognizer is attached to.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var view: UIView? { get }
```

## Discussion

You attach (or add) a gesture recognizer to a `UIView` object using the [- addGestureRecognizer:](<../uiview/addgesturerecognizer(__).md>) method.

## See Also

### Getting the recognizer’s state and view

- [state](state-swift.property.md) — The current state of the gesture recognizer.
- [State](state-swift.enum.md) — Constants that represent the current state a gesture recognizer is in.
- [enabled](isenabled.md) — A Boolean property that indicates whether the gesture recognizer is enabled.
- [buttonMask](buttonmask.md) — A bit mask of the buttons in the gesture represented by the gesture recognizer.
- [modifierFlags](modifierflags.md) — The bit mask of modifier flags in the gesture represented by the gesture recognizer.
