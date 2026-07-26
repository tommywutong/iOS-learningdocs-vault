---
title: 'removeGestureRecognizer(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/removegesturerecognizer(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/removegesturerecognizer(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/removegesturerecognizer%28_%3A%29.json'
content_hash: 'sha256:62a2c87d9c9b6955'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# removeGestureRecognizer(_:)

<sub>Instance Method</sub>

Detaches a gesture recognizer from the receiving view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func removeGestureRecognizer(_ gestureRecognizer: UIGestureRecognizer)
```

## Parameters

- `gestureRecognizer` — An object whose class descends from the [UIGestureRecognizer](../uigesturerecognizer.md) class.

## Discussion

This method releases `gestureRecognizer` in addition to detaching it from the view.

## See Also

### Managing gesture recognizers

- [- addGestureRecognizer:](<addgesturerecognizer(__).md>) — Attaches a gesture recognizer to the view.
- [gestureRecognizers](gesturerecognizers.md) — The gesture-recognizer objects currently attached to the view.
- [- gestureRecognizerShouldBegin:](<gesturerecognizershouldbegin(__).md>) — Asks the view if the gesture recognizer should continue tracking touch events.
