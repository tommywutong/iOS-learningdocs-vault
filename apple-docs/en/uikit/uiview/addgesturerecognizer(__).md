---
title: 'addGestureRecognizer(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/addgesturerecognizer(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/addgesturerecognizer(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/addgesturerecognizer%28_%3A%29.json'
content_hash: 'sha256:abffc6fb05a55bc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# addGestureRecognizer(_:)

<sub>Instance Method</sub>

Attaches a gesture recognizer to the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addGestureRecognizer(_ gestureRecognizer: UIGestureRecognizer)
```

## Parameters

- `gestureRecognizer` — An object whose class descends from the [UIGestureRecognizer](../uigesturerecognizer.md) class. This parameter must not be `nil`.

## Discussion

Attaching a gesture recognizer to a view defines the scope of the represented gesture, causing it to receive touches hit-tested to that view and all of its subviews. The view establishes a strong reference to the gesture recognizer.

## See Also

### Managing gesture recognizers

- [- removeGestureRecognizer:](<removegesturerecognizer(__).md>) — Detaches a gesture recognizer from the receiving view.
- [gestureRecognizers](gesturerecognizers.md) — The gesture-recognizer objects currently attached to the view.
- [- gestureRecognizerShouldBegin:](<gesturerecognizershouldbegin(__).md>) — Asks the view if the gesture recognizer should continue tracking touch events.
