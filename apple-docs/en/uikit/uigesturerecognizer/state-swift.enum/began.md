---
title: UIGestureRecognizer.State.began
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigesturerecognizer/state-swift.enum/began
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/state-swift.enum/began'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/state-swift.enum/began.json'
content_hash: 'sha256:f83d77dd959d2e7b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIGestureRecognizer](../../uigesturerecognizer.md) · [State](../state-swift.enum.md)

# UIGestureRecognizer.State.began

<sub>Case</sub>

The gesture recognizer has received touch objects recognized as a continuous gesture.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case began
```

## Discussion

The gesture recognizer sends its action message (or messages) at the next cycle of the run loop.

## See Also

### Constants

- [UIGestureRecognizerStatePossible](possible.md) — The gesture recognizer hasn’t yet recognized its gesture, but may be evaluating touch events.
- [UIGestureRecognizerStateChanged](changed.md) — The gesture recognizer has received touches recognized as a change to a continuous gesture.
- [UIGestureRecognizerStateEnded](ended.md) — The gesture recognizer has received touches recognized as the end of a continuous gesture.
- [UIGestureRecognizerStateCancelled](cancelled.md) — The gesture recognizer has received touches resulting in the cancellation of a continuous gesture.
- [UIGestureRecognizerStateFailed](failed.md) — The gesture recognizer has received a multi-touch sequence that it can’t recognize as its gesture.
- [UIGestureRecognizerStateRecognized](recognized.md) — The gesture recognizer has received a multitouch sequence that it recognizes as its gesture.
