---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigesturerecognizer/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/delegate.json'
content_hash: 'sha256:dbebaf6c6700a47b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# delegate

<sub>Instance Property</sub>

The delegate of the gesture recognizer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var delegate: (any UIGestureRecognizerDelegate)? { get set }
```

## Discussion

The gesture recognizer maintains a weak reference to its delegate. The delegate must adopt the [UIGestureRecognizerDelegate](../uigesturerecognizerdelegate.md) protocol and implement one or more of its methods.

## See Also

### Managing gesture-related interactions

- [UIGestureRecognizerDelegate](../uigesturerecognizerdelegate.md) — A set of methods implemented by the delegate of a gesture recognizer to fine-tune an app’s gesture-recognition behavior.
