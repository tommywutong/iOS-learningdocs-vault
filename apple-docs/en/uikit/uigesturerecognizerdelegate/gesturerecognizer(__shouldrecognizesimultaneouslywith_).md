---
title: 'gestureRecognizer(_:shouldRecognizeSimultaneouslyWith:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer(_:shouldrecognizesimultaneouslywith:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer(_:shouldrecognizesimultaneouslywith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer%28_%3Ashouldrecognizesimultaneouslywith%3A%29.json'
content_hash: 'sha256:10ff15e33e751453'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizerDelegate](../uigesturerecognizerdelegate.md)

# gestureRecognizer(_:shouldRecognizeSimultaneouslyWith:)

<sub>Instance Method</sub>

Asks the delegate if two gesture recognizers should be allowed to recognize gestures simultaneously.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldRecognizeSimultaneouslyWith otherGestureRecognizer: UIGestureRecognizer) -> Bool
```

## Parameters

- `gestureRecognizer` — An instance of a subclass of the abstract base class [UIGestureRecognizer](../uigesturerecognizer.md). This is the object sending the message to the delegate.

- `otherGestureRecognizer` — An instance of a subclass of the abstract base class [UIGestureRecognizer](../uigesturerecognizer.md).

## Return Value

[true](../../swift/true.md) to allow both `gestureRecognizer` and `otherGestureRecognizer` to recognize their gestures simultaneously. The default implementation returns [false](../../swift/false.md)—no two gestures can be recognized simultaneously.

## Discussion

This method is called when recognition of a gesture by either `gestureRecognizer` or `otherGestureRecognizer` would block the other gesture recognizer from recognizing its gesture. Note that returning [true](../../swift/true.md) is guaranteed to allow simultaneous recognition; returning [false](../../swift/false.md), on the other hand, is not guaranteed to prevent simultaneous recognition because the other gesture recognizer’s delegate may return [true](../../swift/true.md).
