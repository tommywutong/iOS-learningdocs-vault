---
title: gestureRecognizers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/gesturerecognizers
source_url: 'https://developer.apple.com/documentation/uikit/uiview/gesturerecognizers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/gesturerecognizers.json'
content_hash: 'sha256:9d87fc3299da5d8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# gestureRecognizers

<sub>Instance Property</sub>

The gesture-recognizer objects currently attached to the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var gestureRecognizers: [UIGestureRecognizer]? { get set }
```

## Discussion

Each of these objects is an instance of a subclass of the abstract base class [UIGestureRecognizer](../uigesturerecognizer.md). The default value of this property is `nil`. If you add a gesture recognizer and then remove it, the value of the property is an empty array.

## See Also

### Managing gesture recognizers

- [- addGestureRecognizer:](<addgesturerecognizer(__).md>) — Attaches a gesture recognizer to the view.
- [- removeGestureRecognizer:](<removegesturerecognizer(__).md>) — Detaches a gesture recognizer from the receiving view.
- [- gestureRecognizerShouldBegin:](<gesturerecognizershouldbegin(__).md>) — Asks the view if the gesture recognizer should continue tracking touch events.
